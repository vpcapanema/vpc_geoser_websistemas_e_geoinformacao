from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import csv
import zipfile
from brand_typography import font


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "identidade-visual"
OUTPUT = ASSETS / "monocromaticas"

SOURCES = {
    "satelite": ASSETS / "simbolo-vpc-satelite-transparente.png",
    "monitor": ASSETS / "simbolo-vpc-monitor-transparente.png",
}

COLORS = {
    "preto": "#000000",
    "branco": "#FFFFFF",
    "azul-marinho": "#071B45",
    "azul-tecnologico": "#0878D1",
    "verde-geoinformacao": "#67B900",
    "ciano-tecnologico": "#11B8D8",
    "cinza-prata": "#9AAABC",
}

SIZES = (16, 24, 32, 48, 64, 96, 128, 256, 512, 1024)


def detail_alpha(im,name):
    a=np.array(im.convert('RGBA'),dtype=float)
    navy=(a[:,:,2]>a[:,:,0]*1.2)&(a[:,:,2]>a[:,:,1]*1.2)
    g=a[:,:,1]
    cut=navy & (g<85) & (a[:,:,2]<165)
    y,x=np.indices(g.shape)
    x=x*(1254/im.width)
    y=y*(1254/im.height)
    if name=='monitor':
        frame=(x<145)|(x>1110)|(y<170)|(y>900)
        cut[frame]=False
        circuit=(x>680)&(x<1030)&(y>590)&(y<900)&(a[:,:,0]>180)&(g>180)&(a[:,:,2]>180)
        cut |= circuit
    else:
        cavity=(x>420)&(x<900)&(y>300)&(y<550)
        cut |= cavity&navy&(g<145)
    keep=(~cut)&(a[:,:,3]>=192)
    return Image.fromarray(np.uint8(keep)*255).filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(0.65))


def solid_monochrome(alpha: Image.Image, color: str) -> Image.Image:
    """Create a true single-RGB image while preserving a supplied alpha mask."""
    rgb = tuple(int(color[i : i + 2], 16) for i in (1, 3, 5))
    layer = Image.new("RGBA", alpha.size, (*rgb, 255))
    layer.putalpha(alpha)
    return layer


def checkerboard(size: tuple[int, int], cell: int = 16) -> Image.Image:
    im = Image.new("RGB", size, "#AAB4C3")
    draw = ImageDraw.Draw(im)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#75849A")
    return im


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    rows = []
    previews = []

    for symbol_name, source_path in SOURCES.items():
        with Image.open(source_path) as source_file:
            source_alpha = detail_alpha(source_file, symbol_name)
            for color_name, hex_color in COLORS.items():
                master = solid_monochrome(source_alpha, hex_color)
                target_dir = OUTPUT / symbol_name / color_name
                target_dir.mkdir(parents=True, exist_ok=True)

                for size in SIZES:
                    # Resize only the mask. Resizing colored RGBA pixels can
                    # introduce RGB fringes, breaking true monochrome output.
                    resized_alpha = source_alpha.resize((size, size), Image.Resampling.LANCZOS)
                    resized = solid_monochrome(resized_alpha, hex_color)
                    filename = f"simbolo-vpc-{symbol_name}-{color_name}-{size}px.png"
                    path = target_dir / filename
                    temporary = path.with_suffix(".png.tmp")
                    resized.save(temporary, "PNG", optimize=False)
                    temporary.replace(path)
                    rows.append((symbol_name, color_name, hex_color, size, path.relative_to(OUTPUT)))

                preview_alpha = source_alpha.resize((220, 220), Image.Resampling.LANCZOS)
                preview = solid_monochrome(preview_alpha, hex_color)
                board = checkerboard((220, 250))
                board.paste(preview, (0, 0), preview)
                d = ImageDraw.Draw(board)
                label = f"{symbol_name} | {color_name} | {hex_color}"
                d.rectangle((0, 220, 220, 250), fill="white")
                label_font = font(10, 400)
                while d.textlength(label, font=label_font) > 208:
                    label_font = font(label_font.size - 1, 400)
                d.text((6, 230), label, fill="black", font=label_font)
                previews.append(board)

    manifest = OUTPUT / "MANIFESTO.csv"
    with manifest.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(("simbolo", "cor", "hexadecimal", "dimensao_px", "arquivo"))
        writer.writerows(rows)

    readme = OUTPUT / "LEIA-ME.txt"
    readme.write_text(
        "VPC-WEBSISTEMAS E GEOINFORMAÇÃO\n"
        "Pacote de símbolos monocromáticos\n\n"
        "Conteúdo: 2 símbolos x 7 cores x 10 dimensões = 140 PNGs.\n"
        "Todos os arquivos possuem fundo transparente e uma única cor RGB. As divisões internas das matrizes aprovadas são reproduzidas por recortes transparentes, com antisserrilhamento nas bordas.\n\n"
        "Cores:\n"
        + "\n".join(f"- {name}: {value}" for name, value in COLORS.items())
        + "\n\nDimensões: "
        + ", ".join(f"{size}px" for size in SIZES)
        + ".\n",
        encoding="utf-8",
    )

    columns = 4
    rows_count = (len(previews) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * 220, rows_count * 250), "white")
    for i, preview in enumerate(previews):
        sheet.paste(preview, ((i % columns) * 220, (i // columns) * 250))
    sheet.save(OUTPUT / "PREVIA-MONOCROMATICAS.png", "PNG", optimize=True)

    zip_path = ASSETS / "VPC-SIMBOLOS-MONOCROMATICOS.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(OUTPUT.rglob("*")):
            if path.is_file():
                zf.write(path, Path("VPC-SIMBOLOS-MONOCROMATICOS") / path.relative_to(OUTPUT))

    print(f"Generated {len(rows)} PNG files")
    print(manifest)
    print(OUTPUT / "PREVIA-MONOCROMATICAS.png")
    print(zip_path)


if __name__ == "__main__":
    main()
