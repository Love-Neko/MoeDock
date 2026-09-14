import os
import argparse
from PIL import Image

def convert_png_to_ico(png_path, ico_path):
    """
    Converts a transparent PNG into a standard Windows multi-layer .ico file
    containing 256x256, 128x128, 64x64, 48x48, 32x32, 16x16 layers.
    Ensures square aspect ratio by padding transparent margins.
    Uses high-quality Lanczos resampling.
    """
    img = Image.open(png_path).convert('RGBA')
    if img.width == 0 or img.height == 0:
        raise ValueError('Input image has an invalid size')
    w, h = img.size
    max_side = max(w, h)
    sq = Image.new('RGBA', (max_side, max_side), (0, 0, 0, 0))
    sq.paste(img, ((max_side - w) // 2, (max_side - h) // 2))

    sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
    os.makedirs(os.path.dirname(os.path.abspath(ico_path)), exist_ok=True)
    sq.save(ico_path, format='ICO', sizes=sizes)
    print(f"[Converted] {os.path.basename(png_path)} -> {os.path.basename(ico_path)}")

def batch_convert(src_dir, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    pngs = sorted(f for f in os.listdir(src_dir) if f.lower().endswith('.png'))
    count = 0
    for f in pngs:
        src = os.path.join(src_dir, f)
        name = os.path.splitext(f)[0]
        dst = os.path.join(dst_dir, f"{name}.ico")
        try:
            convert_png_to_ico(src, dst)
            count += 1
        except Exception as e:
            print(f"[Error] Failed {f}: {e}")
    print(f"\nBatch conversion finished. Successfully created {count} ICO files in {dst_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PNG to Windows ICO Converter (Supports single file or directory batch)')
    parser.add_argument('--input', '-i', default='.', help='Input PNG file or directory containing PNGs (default: current directory)')
    parser.add_argument('--output', '-o', default=None, help='Output ICO file or directory for ICOs')
    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    if os.path.isfile(input_path):
        out_path = args.output or os.path.splitext(input_path)[0] + '.ico'
        convert_png_to_ico(input_path, out_path)
    elif os.path.isdir(input_path):
        out_dir = args.output or os.path.join(input_path, 'ICO')
        batch_convert(input_path, out_dir)
    else:
        print(f"[Error] Input path does not exist: {input_path}")
