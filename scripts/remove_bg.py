import os
import argparse
import numpy as np
from PIL import Image, ImageFilter, ImageOps
from collections import deque

def remove_white_background(img_path, out_path, tol=245, extra_seeds=None, add_sticker_border=0):
    """
    Removes white background using BFS flood-fill from edges with edge-feathering.
    Properly handles RGBA and RGB source formats without creating black artifacts.
    Supports extra seeds for enclosed background holes.
    Optionally adds a clean white die-cut sticker outline.
    """
    source = Image.open(img_path)
    w, h = source.size
    
    # 1. Normalize image for white detection
    # If source has an alpha channel, paste over pure white so transparent pixels become white
    # and don't turn into black [0, 0, 0] which would break the flood fill.
    bg_white = Image.new('RGB', (w, h), (255, 255, 255))
    orig_alpha = None
    if 'A' in source.getbands():
        orig_alpha = source.getchannel('A')
        bg_white.paste(source, mask=orig_alpha)
    else:
        bg_white.paste(source)

    arr = np.array(bg_white)

    # 2. Identify background candidates based on tolerance
    is_white = (arr[:, :, 0] >= tol) & (arr[:, :, 1] >= tol) & (arr[:, :, 2] >= tol)

    visited = np.zeros((h, w), dtype=bool)
    q = deque()

    # Seed with all 4 outer borders
    for y in range(h):
        for x in (0, w - 1):
            if is_white[y, x] and not visited[y, x]:
                visited[y, x] = True
                q.append((y, x))
    for x in range(w):
        for y in (0, h - 1):
            if is_white[y, x] and not visited[y, x]:
                visited[y, x] = True
                q.append((y, x))

    # Add extra seeds if specified: (y, x)
    if extra_seeds:
        for sy, sx in extra_seeds:
            if 0 <= sy < h and 0 <= sx < w and not visited[sy, sx]:
                visited[sy, sx] = True
                q.append((sy, sx))

    # Flood fill
    while q:
        cy, cx = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and is_white[ny, nx]:
                visited[ny, nx] = True
                q.append((ny, nx))

    # Foreground mask: 255 for character, 0 for removed background
    fg_mask = (~visited).astype(np.uint8) * 255
    mask_img = Image.fromarray(fg_mask, mode='L')
    
    # Smooth edge with subtle gaussian blur
    mask_feathered = mask_img.filter(ImageFilter.GaussianBlur(radius=0.7))

    # Combine with original alpha if present
    if orig_alpha is not None:
        from PIL import ImageChops
        final_alpha = ImageChops.multiply(orig_alpha, mask_feathered)
    else:
        final_alpha = mask_feathered

    # 3. Optional: Add clean die-cut sticker border
    rgba = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    source_rgb = source.convert('RGB')
    rgba.paste(source_rgb, (0, 0))
    rgba.putalpha(final_alpha)

    if add_sticker_border > 0:
        # Create dilated solid white mask for sticker effect
        dilated = mask_img.filter(ImageFilter.MaxFilter(int(add_sticker_border * 2 + 1)))
        sticker_base = Image.new('RGBA', (w, h), (255, 255, 255, 255))
        sticker_base.putalpha(dilated)
        sticker_base.paste(rgba, (0, 0), rgba)
        rgba = sticker_base

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    rgba.save(out_path, 'PNG')
    print(f"[Success] Saved transparent icon: {out_path}")
    return rgba

def parse_seeds_arg(seeds_str):
    """Parses seed string formatted as 'y,x;y,x' or 'x,y;x,y'"""
    if not seeds_str:
        return None
    seeds = []
    for item in seeds_str.split(';'):
        item = item.strip()
        if not item:
            continue
        parts = item.split(',')
        if len(parts) == 2:
            try:
                y, x = int(parts[0].strip()), int(parts[1].strip())
                seeds.append((y, x))
            except ValueError:
                pass
    return seeds

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Anime Dock Icon Background Remover')
    parser.add_argument('--input', '-i', required=True, help='Path to input image (JPG/PNG)')
    parser.add_argument('--output', '-o', required=True, help='Path to output transparent PNG')
    parser.add_argument('--tol', '-t', type=int, default=245, help='White tolerance (0-255, default 245)')
    parser.add_argument('--seeds', '-s', default=None, help='Extra seeds for enclosed holes (e.g. "120,340;200,450")')
    parser.add_argument('--sticker', type=int, default=0, help='Pixel width of white die-cut sticker outline (default 0, off)')
    args = parser.parse_args()

    seeds = parse_seeds_arg(args.seeds)
    remove_white_background(args.input, args.output, tol=args.tol, extra_seeds=seeds, add_sticker_border=args.sticker)
