# 🎨 MoeDock · Anime Dock Icon Workshop

<p align="center"><a href="./README.md">简体中文</a> · <a href="./README.en.md">English</a> · <a href="./README.ja.md">日本語</a></p>

<p align="center"><img src="./preview.gif" alt="MoeDock preview" width="100%" /></p>

<p align="center"><strong>Give your everyday apps a personality.</strong><br>From transparent PNGs to multi-size ICO files and an interactive Dock preview, MoeDock provides a complete offline workflow.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Style-2.5D%20Chibi%20Anime-ff69b4.svg" alt="Style" />
  <img src="https://img.shields.io/badge/Assets-PNG%20%7C%20ICO-8a2be2.svg" alt="Assets" />
  <a href="https://github.com/Love-Neko/MoeDock/actions/workflows/ci.yml"><img src="https://github.com/Love-Neko/MoeDock/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" /></a>
</p>

## 📖 What is MoeDock?

MoeDock is a collection of anime-style, anthropomorphic Dock icons and the tools used to produce them. Brand colors and visual symbols are transformed into expressive chibi characters while keeping silhouettes clear at small sizes.

The repository includes transparent PNG assets, native Windows ICO files (16–256 px), a self-contained offline preview page, and an automated background-removal, conversion, and preview pipeline.

## ✨ Features

- **Brand-color first:** keep each app recognizable at a glance.
- **Logo propification:** turn logos into 3D props, vehicles, or accessories.
- **Clean alpha:** anti-aliased transparent backgrounds with optional sticker borders.
- **Multi-size ICO:** package 16, 32, 48, 64, 128, and 256 px layers in one file.
- **Offline Dock preview:** search icons, switch wallpapers, and preview hover zoom in a browser.
- **One-command pipeline:** remove white backgrounds, create PNG/ICO assets, and refresh the preview.

## 🧭 Project structure

```text
MoeDock/
├─ 例图/                  # Example PNG and ICO assets
├─ dock_preview.html      # Self-contained interactive preview
├─ scripts/               # Production and packaging scripts
├─ references/            # Prompt and color references
├─ examples/              # Workflow examples
└─ tests/                 # Regression tests
```

## ⚡ Quick start

```bash
git clone https://github.com/Love-Neko/MoeDock.git
cd MoeDock
pip install -r requirements.txt
```

Open `dock_preview.html` directly in a browser. To process a new icon:

```bash
python scripts/pipeline.py -i input.jpg -n Steam --png-dir ./例图/PNG图标 --ico-dir ./例图/ICO图标 -p ./dock_preview.html
```

For individual steps, see `scripts/remove_bg.py`, `scripts/convert_ico.py`, and `scripts/update_preview.py`.

## 🖥️ Using the icons

- **Windows:** Shortcut → Properties → Change Icon, then choose an ICO file.
- **MyDockFinder / BitDock:** assign a PNG from `例图/PNG图标/`.
- **macOS:** open an app’s Get Info window and drag a PNG onto its icon.

## 🤝 Contributing

Issues and pull requests are welcome. You can contribute new app concepts, brand colors, prompts, or pipeline improvements.

## 📄 License

Code is released under the [MIT License](./LICENSE). App trademarks and logos belong to their respective owners.
