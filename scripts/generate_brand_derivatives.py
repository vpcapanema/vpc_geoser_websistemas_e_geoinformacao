from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import vtracer
from brand_typography import font, svg_text


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "identidade-visual"
SOURCE_ORIGINAL = ASSETS / "simbolo-vpc-satelite-transparente.png"
SOURCE = ASSETS / "simbolo-vpc-satelite-transparente-limpo.png"
VECTOR = ASSETS / "vetorial"
FAVICON = ASSETS / "favicon"
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def clean_master() -> Path:
    """Remove residual matte pixels without changing the approved artwork."""
    with Image.open(SOURCE_ORIGINAL) as source_file:
        image = source_file.convert("RGBA")
    alpha = image.getchannel("A")
    # Pixels this faint are extraction residue, not visible artwork. Remaining
    # edge pixels are rescaled to preserve antialiasing without dirty halos.
    alpha = alpha.point(lambda value: 0 if value <= 24 else (255 if value >= 248 else round((value - 24) * 255 / 224)))
    # Contract the extraction mask by two pixels to discard the cyan/black
    # matte embedded in the outermost edge, then restore a clean antialias.
    alpha = alpha.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(0.55))
    image.putalpha(alpha)
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError("A limpeza removeu todo o conteúdo da matriz")
    image.save(SOURCE, "PNG", optimize=True)
    return SOURCE


def vectorize_master() -> Path:
    output = VECTOR / "simbolo-vpc-satelite.svg"
    # The library defaults are stable on Windows/Python 3.14 and retain the
    # approved artwork's color layers without introducing a new drawing.
    vtracer.convert_image_to_svg_py(str(SOURCE), str(output))
    return output


def svg_symbol(trace_root, x: int, y: int, size: int, monochrome: bool = False):
    nested = ET.Element(f"{{{NS}}}svg", {
        "x": str(x), "y": str(y), "width": str(size), "height": str(size),
        "viewBox": trace_root.attrib.get("viewBox", "0 0 1280 1280"),
        "preserveAspectRatio": "xMidYMid meet",
    })
    for child in trace_root:
        item = deepcopy(child)
        if monochrome:
            for node in item.iter():
                if "fill" in node.attrib and node.attrib["fill"] != "none":
                    node.attrib["fill"] = "#000000"
                if "stroke" in node.attrib and node.attrib["stroke"] != "none":
                    node.attrib["stroke"] = "#000000"
        nested.append(item)
    return nested


def make_signature(trace_root, filename: str, background: str | None, mono: bool = False):
    width, height = 1600, 360
    root = ET.Element(f"{{{NS}}}svg", {
        "viewBox": f"0 0 {width} {height}", "role": "img",
        "aria-label": "VPC WebSistemas e Geoinformação",
    })
    ET.SubElement(root, f"{{{NS}}}title").text = "Assinatura horizontal VPC WebSistemas & Geoinformação"
    if background:
        ET.SubElement(root, f"{{{NS}}}rect", {"width": str(width), "height": str(height), "fill": background})
    root.append(svg_symbol(trace_root, 20, 10, 340, monochrome=mono))
    text_color = "#000000" if mono else ("#FFFFFF" if background else "#071B45")
    accent = "#000000" if mono else "#67B900"
    root.append(svg_text("VPC-", 385, 169, 88, accent))
    offset = font(352).getlength("VPC-") / 4 + 4
    root.append(svg_text("WEBSISTEMAS", 385 + offset, 169, 88, text_color))
    root.append(svg_text("E GEOINFORMAÇÃO", 385, 265, 76, text_color))
    ET.ElementTree(root).write(VECTOR / filename, encoding="utf-8", xml_declaration=True)


def make_png_signature(filename: str, dark: bool = False):
    width, height = 1600, 360
    background = (7, 27, 69, 255) if dark else (255, 255, 255, 0)
    canvas = Image.new("RGBA", (width, height), background)
    with Image.open(SOURCE) as source_file:
        symbol = source_file.convert("RGBA")
    symbol.thumbnail((340, 340), Image.Resampling.LANCZOS)
    canvas.alpha_composite(symbol, (20 + (340 - symbol.width) // 2, 10 + (340 - symbol.height) // 2))
    draw = ImageDraw.Draw(canvas)
    font1 = font(88)
    font2 = font(76)
    primary = "#FFFFFF" if dark else "#071B45"
    draw.text((385, 91), "VPC-", font=font1, fill="#67B900")
    offset = draw.textlength("VPC-", font=font1)
    draw.text((385 + offset, 91), "WEBSISTEMAS", font=font1, fill=primary)
    draw.text((385, 190), "E GEOINFORMAÇÃO", font=font2, fill=primary)
    canvas.save(ASSETS / filename, "PNG", optimize=True)


def main():
    VECTOR.mkdir(parents=True, exist_ok=True)
    clean_master()
    trace_path = vectorize_master()
    trace_root = ET.parse(trace_path).getroot()
    make_signature(trace_root, "assinatura-vpc-horizontal-fundo-claro.svg", None)
    make_signature(trace_root, "assinatura-vpc-horizontal-fundo-escuro.svg", "#071B45")
    make_signature(trace_root, "assinatura-vpc-horizontal-monocromatica.svg", None, mono=True)
    make_png_signature("assinatura-vpc-horizontal-fundo-claro.png")
    make_png_signature("assinatura-vpc-horizontal-fundo-escuro.png", dark=True)
    (FAVICON / "favicon.svg").write_bytes(trace_path.read_bytes())
    print("Derivados gerados exclusivamente da matriz aprovada:", SOURCE)


if __name__ == "__main__":
    main()
