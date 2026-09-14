import os
import sys
import argparse
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))
scripts_dir = Path(__file__).resolve().parent
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

try:
    from scripts.remove_bg import remove_white_background, parse_seeds_arg
    from scripts.convert_ico import convert_png_to_ico
    from scripts.update_preview import generate_dock_preview
except ImportError:
    from remove_bg import remove_white_background, parse_seeds_arg
    from convert_ico import convert_png_to_ico
    from update_preview import generate_dock_preview

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def process_single_icon(raw_path, icon_name, png_dir, ico_dir, tol=245, seeds=None, sticker=0):
    os.makedirs(png_dir, exist_ok=True)
    os.makedirs(ico_dir, exist_ok=True)

    png_path = os.path.join(png_dir, f"{icon_name}.png")
    ico_path = os.path.join(ico_dir, f"{icon_name}.ico")

    print(f"\n[Pipeline] Processing: {icon_name}")
    remove_white_background(raw_path, png_path, tol=tol, extra_seeds=seeds, add_sticker_border=sticker)
    convert_png_to_ico(png_path, ico_path)

    print(f"[Pipeline Done] Created:\n   PNG: {png_path}\n   ICO: {ico_path}")
    return png_path, ico_path

def main():
    parser = argparse.ArgumentParser(description='Anime Dock Icon End-to-End Pipeline (One-Click Build)')
    parser.add_argument('--input', '-i', required=True, help='Path to raw generated image (JPG/PNG)')
    parser.add_argument('--name', '-n', default=None, help='Target icon name (e.g. Steam, Chrome)')
    parser.add_argument('--png-dir', default='./PNG', help='Output directory for transparent PNGs (default: ./PNG)')
    parser.add_argument('--ico-dir', default='./ICO', help='Output directory for ICOs (default: ./ICO)')
    parser.add_argument('--tol', '-t', type=int, default=245, help='White tolerance (0-255, default 245)')
    parser.add_argument('--seeds', '-s', default=None, help='Extra seeds for enclosed holes (e.g. 120,340;200,450)')
    parser.add_argument('--sticker', type=int, default=0, help='White die-cut sticker outline width in pixels (default 0)')
    parser.add_argument('--preview', '-p', default=None, help='Optional output path to refresh dock_preview.html')
    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    if not os.path.exists(input_path):
        print(f"[Error] Input not found: {input_path}")
        return

    name = args.name or Path(input_path).stem
    process_single_icon(
        raw_path=input_path,
        icon_name=name,
        png_dir=os.path.abspath(args.png_dir),
        ico_dir=os.path.abspath(args.ico_dir),
        tol=args.tol,
        seeds=parse_seeds_arg(args.seeds),
        sticker=args.sticker
    )

    if args.preview:
        preview_path = os.path.abspath(args.preview)
        generate_dock_preview(os.path.abspath(args.png_dir), preview_path)

if __name__ == '__main__':
    main()
