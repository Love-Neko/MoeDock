"""Generate a self-contained, offline Dock icon preview page."""

from base64 import b64encode
from html import escape
from pathlib import Path
import argparse

from PIL import Image


def _data_url(path: Path) -> str:
    with Image.open(path) as image:
        image = image.convert("RGBA")
        image.thumbnail((128, 128), Image.Resampling.LANCZOS)
        from io import BytesIO

        buffer = BytesIO()
        image.save(buffer, format="PNG", optimize=True)
    return "data:image/png;base64," + b64encode(buffer.getvalue()).decode("ascii")


def generate_dock_preview(dock_dir, output_html):
    """Build an HTML preview from PNG files in *dock_dir*."""
    source = Path(dock_dir)
    icons = [(path.stem, _data_url(path)) for path in sorted(source.glob("*.png"))]
    cards = "\n".join(
        f'<article class="icon-card" data-name="{escape(name.lower())}">'
        f'<img src="{url}" alt="{escape(name)}" loading="lazy"><span>{escape(name)}</span></article>'
        for name, url in icons
    )
    dock_items = "\n".join(
        f'<div class="dock-item" data-name="{escape(name.lower())}"><img src="{url}" alt="{escape(name)}">'
        f'<span class="tooltip">{escape(name)}</span></div>'
        for name, url in icons
    )
    count = len(icons)
    html = f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>图标实时交互预览</title>
<style>
:root {{ color-scheme: dark; --accent:#f472b6; --text:#f8fafc; --muted:#a5b4fc; --panel:rgba(15,23,42,.72); }}
* {{ box-sizing:border-box; }} body {{ margin:0; min-height:100vh; color:var(--text); font-family:"Segoe UI","Microsoft YaHei",sans-serif; background:radial-gradient(circle at 12% 8%,#312e81 0,transparent 34%),radial-gradient(circle at 88% 92%,#701a75 0,transparent 30%),#020617; transition:background .3s; }}
.page {{ width:min(1120px,100%); margin:auto; padding:24px 18px 44px; }} .topbar {{ display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:18px; padding:18px 22px; border:1px solid #ffffff1c; border-radius:24px; background:var(--panel); backdrop-filter:blur(18px); box-shadow:0 20px 50px #02061766; }}
h1 {{ margin:0; font-size:clamp(1.15rem,2vw,1.5rem); background:linear-gradient(90deg,#f9a8d4,#c4b5fd,#93c5fd); color:transparent; background-clip:text; }} .subtitle {{ margin:6px 0 0; color:#cbd5e1; font-size:.86rem; }}
.toolbar {{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; }} input,button {{ border:1px solid #ffffff26; border-radius:12px; background:#ffffff12; color:inherit; padding:9px 12px; font:inherit; }} input {{ min-width:180px; outline:none; }} input:focus {{ border-color:var(--accent); }} button {{ cursor:pointer; transition:.2s; }} button:hover {{ border-color:var(--accent); transform:translateY(-1px); }}
.section-title {{ display:flex; justify-content:space-between; align-items:center; margin:30px 2px 12px; color:#e2e8f0; }} .section-title small {{ color:#94a3b8; }} .gallery {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(116px,1fr)); gap:12px; }}
.icon-card {{ display:flex; min-height:132px; flex-direction:column; align-items:center; justify-content:center; gap:8px; padding:14px 8px; border:1px solid #ffffff14; border-radius:18px; background:#0f172a99; transition:.25s; }} .icon-card:hover {{ transform:translateY(-5px); border-color:#f472b680; box-shadow:0 14px 28px #02061766; }} .icon-card img {{ width:76px; height:76px; object-fit:contain; filter:drop-shadow(0 8px 8px #02061766); }} .icon-card span {{ max-width:100%; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; color:#cbd5e1; font-size:.82rem; }}
.dock-stage {{ position:relative; overflow:visible; padding:58px 20px 20px; border:1px solid #ffffff1f; border-radius:28px; background:linear-gradient(180deg,#33415566,#0f172a55); box-shadow:inset 0 1px #ffffff18,0 24px 60px #02061766; }} .dock-stage::before {{ content:"悬停图标，体验 Dock 缩放"; position:absolute; top:18px; left:22px; color:#cbd5e1; font-size:.78rem; }} .dock-container {{ display:flex; justify-content:center; align-items:flex-end; gap:12px; min-height:112px; overflow:visible; isolation:isolate; }} .dock-item {{ position:relative; flex:0 0 56px; transform-origin:bottom center; transition:transform .24s cubic-bezier(.25,1,.5,1),filter .24s; will-change:transform; z-index:1; }} .dock-item img {{ display:block; width:56px; height:56px; object-fit:contain; }} .dock-item:hover {{ transform:scale(1.65) translateY(-10px); z-index:10; filter:drop-shadow(0 14px 12px #02061799); }} .dock-item:hover + .dock-item, .dock-item:has(+ .dock-item:hover) {{ transform:scale(1.25) translateY(-4px); z-index:5; }} .tooltip {{ position:absolute; left:50%; bottom:calc(100% + 14px); transform:translateX(-50%); opacity:0; pointer-events:none; white-space:nowrap; padding:5px 8px; border-radius:8px; background:#020617dd; color:#f8fafc; font-size:.72rem; transition:opacity .15s; }} .dock-item:hover .tooltip {{ opacity:1; }}
body.light {{ color:#1e293b; background:linear-gradient(135deg,#e0e7ff,#fce7f3); }} body.light .topbar, body.light .icon-card, body.light .dock-stage {{ background:#ffffff99; border-color:#33415526; }} body.light .subtitle, body.light .icon-card span, body.light .section-title small {{ color:#475569; }}
@media(max-width:640px) {{ .page {{ padding:12px 10px 28px; }} .topbar {{ padding:16px; }} .dock-stage {{ padding-inline:8px; }} .dock-container {{ gap:5px; }} .dock-item {{ flex-basis:40px; }} .dock-item img {{ width:40px; height:40px; }} }}
</style></head>
<body><div class="page"><header class="topbar"><div><h1>✨ 图标实时交互预览</h1><p class="subtitle">{count} 枚透明底高清图标 · 平滑悬停动效 · 完全离线</p></div><div class="toolbar"><input id="search" type="search" placeholder="搜索图标…" aria-label="搜索图标"><button onclick="setTheme('dark')">极夜黑</button><button onclick="setTheme('purple')">深邃紫</button><button onclick="setTheme('sunset')">霞光红</button><button onclick="setTheme('light')">浅色</button></div></header>
<main><div class="section-title"><strong>图标图库</strong><small id="count">{count} 个结果</small></div><section class="gallery">{cards}</section>
<div class="section-title"><strong>Dock 动效</strong><small>放大效果完整包裹在展示框内</small></div><section class="dock-stage"><div class="dock-container">{dock_items}</div></section></main></div>
<script>
const search=document.querySelector('#search'), cards=[...document.querySelectorAll('.icon-card')], items=[...document.querySelectorAll('.dock-item')], count=document.querySelector('#count');
search.addEventListener('input',()=>{{const q=search.value.trim().toLowerCase(); let visible=0; cards.forEach((el,i)=>{{const match=!q||el.dataset.name.includes(q); el.hidden=!match; items[i].hidden=!match; if(match) visible++;}}); count.textContent=visible+' 个结果';}});
function setTheme(theme){{document.body.className=theme==='light'?'light':''; if(theme==='purple')document.body.style.background='radial-gradient(circle at 10% 10%,#4338ca,transparent 35%),#111827'; else if(theme==='sunset')document.body.style.background='radial-gradient(circle at 85% 85%,#be123c,transparent 35%),#1e1b4b'; else if(theme==='dark')document.body.style.background='radial-gradient(circle at 12% 8%,#312e81,transparent 34%),radial-gradient(circle at 88% 92%,#701a75,transparent 30%),#020617'; else document.body.style.background='';}}
</script></body></html>'''
    output = Path(output_html)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    print(f"[Preview] Generated {output} with {count} icons")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an offline Dock preview")
    parser.add_argument("--input", "-i", "--input-dir", dest="input_dir", default="./PNG")
    parser.add_argument("--output", "-o", default="./dock_preview.html")
    args = parser.parse_args()
    generate_dock_preview(args.input_dir, args.output)
