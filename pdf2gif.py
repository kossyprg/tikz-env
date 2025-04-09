import fitz # import PyMuPDF
from PIL import Image
import argparse

# 1インチ ~ 72 ポイント
# Ref https://pymupdf.readthedocs.io/ja/latest/rect.html#rect
BASE_DPI = 72.0

def pdf_to_images(pdf_path: str, dpi: int = 100):
    scale = dpi / BASE_DPI
    doc = fitz.open(pdf_path)
    images = []
    for page in doc:
        # Matrix の各引数は x,y 方向の拡大ファクター
        # Ref https://pymupdf.readthedocs.io/ja/latest/matrix.html#matrix
        # Ref https://pymupdf.readthedocs.io/ja/latest/page.html#Page.get_pixmap
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))

        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    return images

def save_gif(images, delay_ms = 100, output_path: str = "main.gif"):
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        loop=0,
        duration=delay_ms
    )

def main(args):
    images = pdf_to_images(args.input, dpi=args.dpi)
    save_gif(images, delay_ms=args.delay, output_path=args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",  default="./out/main.pdf", help="Path to PDF file")
    parser.add_argument("--output", default="main.gif",       help="Path to output GIF")
    parser.add_argument("--dpi",   type=int, default=150, help="DPI or scale factor")
    parser.add_argument("--delay", type=int, default=100, help="Frame delay in ms")
    args = parser.parse_args()
    main(args)