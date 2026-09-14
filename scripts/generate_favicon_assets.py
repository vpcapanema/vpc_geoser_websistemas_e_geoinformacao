from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "identidade-visual" / "favicon"
SOURCE = ROOT / "assets" / "identidade-visual" / "simbolo-vpc-satelite-transparente-limpo.png"
SIZES = (16, 32, 48, 180, 192, 512)


def prepare_master() -> Image.Image:
    """Crop and pad the approved artwork without redrawing or changing it."""
    with Image.open(SOURCE) as source_file:
        source = source_file.convert("RGBA")
    bbox = source.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError(f"Matriz sem conteúdo visível: {SOURCE}")
    cropped = source.crop(bbox)
    side = max(cropped.size)
    padding = max(1, round(side * 0.04))
    canvas = Image.new("RGBA", (side + 2 * padding, side + 2 * padding), (0, 0, 0, 0))
    canvas.alpha_composite(cropped, ((canvas.width - cropped.width) // 2, (canvas.height - cropped.height) // 2))
    return canvas


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    master = prepare_master()
    images = {}
    for size in SIZES:
        image = master.resize((size, size), Image.Resampling.LANCZOS)
        images[size] = image
        image.save(OUTPUT / f"favicon-{size}x{size}.png", "PNG", optimize=True)

    images[48].save(
        OUTPUT / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=[images[32], images[16]],
    )
    print(f"Generated {len(SIZES)} PNG favicons and favicon.ico in {OUTPUT}")


if __name__ == "__main__":
    main()
