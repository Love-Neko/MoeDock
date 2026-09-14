import os
import base64
import io
import argparse
from PIL import Image

def generate_dock_preview(dock_dir, output_html):
    files = [f for f in sorted(os.listdir(dock_dir)) if f.lower().endswith('.png')]
    icons_data = []
    for f in files:
        path = os.path.join(dock_dir, f)
        try:
            img = Image.open(path).convert('RGBA')
            img.thumbnail((128, 128), Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            b64 = base64.b64encode(buf.getvalue()).decode('ascii')
            name = os.path.splitext(f)[0]
            icons_data.append({'name': name, 'b64': b64})
        except Exception as e:
            print(f"Error loading {f}: {e}")

    grid_html = ""
    for icon in icons_data:
        name = icon['name']
        b64 = icon['b64']
        grid_html += f'''
          <div class="icon-card group relative flex flex-col items-center justify-center p-3 rounded-xl bg-slate-800/40 border border-slate-700/40 hover:bg-slate-800/80 hover:border-pink-500/50 transition cursor-pointer" data-name="{name}">
            <img src="data:image/png;base64,{b64}" alt="{name}" class="w-14 h-14 object-contain drop-shadow-md group-hover:scale-110 transition duration-200" />
            <span class="mt-2 text-[11px] font-medium text-slate-300 truncate max-w-full group-hover:text-pink-300">{name}</span>
          </div>'''

    dock_html = ""
    for icon in icons_data:
        name = icon['name']
        b64 = icon['b64']
        dock_html += f'''
          <div class="dock-item relative flex flex-col items-center cursor-pointer" data-name="{name}">
            <div class="tooltip absolute -top-8 px-2 py-0.5 rounded-md bg-slate-900/90 text-white text-[11px] whitespace-nowrap shadow-lg border border-slate-700">
              {name}
            </div>
            <img src="data:image/png;base64,{b64}" alt="{name}" class="w-11 h-11 object-contain drop-shadow-lg pointer-events-none" />
          </div>'''

    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <title>Dock 栏二次元图标实时交互预览</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    /* 离线基础兜底样式 (Fallback for offline / CDN failure) */
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; background: #0f172a; color: #f8fafc; }}
    .dock-container {{ perspective: 1000px; display: flex; align-items: flex-end; gap: 6px; }}
    .dock-item {{ transition: all 0.2s cubic-bezier(0.25, 1, 0.5, 1); transform-origin: bottom center; cursor: pointer; }}
    .dock-item:hover {{ transform: scale(1.6) translateY(-14px); z-index: 50; }}
    .dock-item:hover + .dock-item {{ transform: scale(1.3) translateY(-7px); z-index: 40; }}
    .dock-item:has(+ .dock-item:hover) {{ transform: scale(1.3) translateY(-7px); z-index: 40; }}
    .dock-glass {{ background: rgba(255, 255, 255, 0.12); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35); }}
    .tooltip {{ opacity: 0; pointer-events: none; transition: opacity 0.15s ease; }}
    .dock-item:hover .tooltip {{ opacity: 1; }}
  </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col items-center justify-between p-4 selection:bg-pink-500 selection:text-white">
  <header class="w-full max-w-5xl flex flex-wrap items-center justify-between gap-4 py-3 px-5 rounded-2xl bg-slate-800/80 border border-slate-700/60 backdrop-blur">
    <div>
      <h1 class="text-lg font-bold bg-gradient-to-r from-pink-400 via-purple-300 to-indigo-400 bg-clip-text text-transparent">✨ Dock 栏手绘图标预览台</h1>
      <p class="text-xs text-slate-400">已载入 <span id="count">{len(icons_data)}</span> 枚透明底高清图标 · 支持平滑悬停动效与多壁纸切换</p>
    </div>
    <div class="flex items-center gap-3 text-xs">
      <input id="searchInput" type="text" oninput="filterIcons(this.value)" placeholder="🔍 搜索图标..." class="px-3 py-1 rounded-lg bg-slate-950 border border-slate-700 text-slate-200 placeholder-slate-500 focus:outline-none focus:border-pink-500 transition" />
      <span class="text-slate-400">模拟壁纸:</span>
      <button onclick="setBg('dark')" class="px-3 py-1 rounded-lg bg-slate-950 border border-slate-700 hover:border-pink-500 transition">极夜黑</button>
      <button onclick="setBg('acrylic')" class="px-3 py-1 rounded-lg bg-gradient-to-br from-indigo-950 to-slate-900 border border-slate-700 hover:border-pink-500 transition">深邃紫</button>
      <button onclick="setBg('sunset')" class="px-3 py-1 rounded-lg bg-gradient-to-br from-rose-900 via-purple-900 to-slate-900 border border-slate-700 hover:border-pink-500 transition">霞光红</button>
      <button onclick="setBg('light')" class="px-3 py-1 rounded-lg bg-slate-200 text-slate-900 border border-slate-300 hover:border-pink-500 transition">浅色壁纸</button>
    </div>
  </header>

  <main class="w-full max-w-5xl my-6 flex-1 flex flex-col justify-center">
    <div class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-7 gap-3">
      {grid_html}
    </div>
  </main>

  <footer class="w-full flex flex-col items-center justify-center pb-4">
    <div class="text-center text-xs text-slate-400 mb-2">👇 鼠标划过体验 Dock 栏缩放动效</div>
    <div class="dock-container dock-glass px-4 py-2.5 rounded-2xl flex items-end gap-1.5 max-w-full overflow-x-auto shadow-2xl">
      {dock_html}
    </div>
  </footer>

  <script>
    function setBg(type) {{
      const b = document.body;
      if (type === 'dark') b.className = 'bg-slate-950 text-slate-100 min-h-screen flex flex-col items-center justify-between p-4 transition-all duration-300';
      else if (type === 'acrylic') b.className = 'bg-gradient-to-br from-indigo-950 via-slate-900 to-slate-950 text-slate-100 min-h-screen flex flex-col items-center justify-between p-4 transition-all duration-300';
      else if (type === 'sunset') b.className = 'bg-gradient-to-br from-rose-950 via-purple-950 to-slate-950 text-slate-100 min-h-screen flex flex-col items-center justify-between p-4 transition-all duration-300';
      else if (type === 'light') b.className = 'bg-slate-200 text-slate-800 min-h-screen flex flex-col items-center justify-between p-4 transition-all duration-300';
    }}

    function filterIcons(query) {{
      const q = (query || '').toLowerCase().trim();
      let visible = 0;
      document.querySelectorAll('.icon-card').forEach(card => {{
        const name = (card.getAttribute('data-name') || '').toLowerCase();
        const match = !q || name.includes(q);
        card.style.display = match ? '' : 'none';
        if (match) visible++;
      }});
      const countEl = document.getElementById('count');
      if (countEl) countEl.innerText = visible;
    }}
  </script>
</body>
</html>'''

    os.makedirs(os.path.dirname(os.path.abspath(output_html)), exist_ok=True)
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"[Success] Updated preview HTML at: {output_html}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a local Dock icon preview page')
    parser.add_argument('--input-dir', '-i', default='.', help='Directory containing PNG icons (default: current directory)')
    parser.add_argument('--output', '-o', default='./dock_preview.html', help='Output HTML path (default: ./dock_preview.html)')
    args = parser.parse_args()
    generate_dock_preview(args.input_dir, args.output)
