"""Batch Image Watermark & Pencil-Sketch Filter Utility (Pillow)"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageOps

def add_watermark(input_path: str, output_path: str, text="RiseAhead"):
    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    w, h = img.size
    draw.text((w - 140, h - 36), text, fill=(249, 115, 22, 180))
    Image.alpha_composite(img, overlay).convert("RGB").save(output_path)

def to_pencil_sketch(input_path: str, output_path: str):
    gray = ImageOps.grayscale(Image.open(input_path))
    edges = gray.filter(ImageFilter.FIND_EDGES)
    ImageOps.invert(edges).save(output_path)

if __name__ == "__main__":
    print("Watermark & Sketch utility ready. Call add_watermark('in.jpg', 'out.jpg', 'YourBrand').")
