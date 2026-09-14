# 🎨 MoeDock 萌坞 · 二次元卡通拟人 Dock 栏图标生产工坊

<p align="center">
  <img src="./图标预览.gif" alt="MoeDock 图标预览" width="100%" />
</p>

<p align="center">
  <strong>把常用软件变成有性格的桌面伙伴。</strong><br />
  从透明 PNG 到多尺寸 ICO，再到可交互的 Dock 预览，一套素材与工具即可完成。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Style-2.5D%20Chibi%20Anime-ff69b4.svg" alt="Style" />
  <img src="https://img.shields.io/badge/Assets-PNG%20%7C%20ICO-8a2be2.svg" alt="Assets" />
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776ab.svg" alt="Python" />
  <img src="https://img.shields.io/badge/Preview-Offline-22c55e.svg" alt="Preview" />
</p>

---

## 📖 什么是 MoeDock？

**MoeDock（萌坞）** 是一套面向桌面 Dock 和应用启动器的二次元图标资源与生产工作流。它将软件品牌的颜色、符号和气质转译成更有角色感的卡通图标，同时保留小尺寸下清晰、易认、耐看的轮廓。

项目包含高清透明 PNG、Windows 原生多尺寸 ICO、交互式网页预览，以及去背景、格式转换和预览页更新脚本。你可以直接使用现成图标，也可以把它当作自己的图标生产模板。

## ✨ 核心特色

- **品牌色优先**：用主色块和轮廓保持软件辨识度
- **道具拟人化**：将 Logo 转成角色服装、装备或互动道具
- **透明底输出**：适合深色、浅色和半透明 Dock 背景
- **多尺寸 ICO**：一次生成 16、32、48、64、128、256 px 图层
- **本地交互预览**：无需部署服务，双击 HTML 即可查看悬停放大效果
- **可复用脚本**：支持从原图到 PNG、ICO、预览页的分步处理

## 🧭 项目结构

```text
MoeDock/
├─ 例图/
│  ├─ PNG图标/          # 高清透明 PNG 素材
│  └─ ICO图标/          # 多尺寸 Windows ICO 素材
├─ dock_preview.html    # 图库与 Dock 动效预览台
├─ 图标预览.gif         # 快速浏览项目效果
├─ scripts/             # 去背景、转 ICO、更新预览页
├─ references/          # 色卡与提示词参考
├─ examples/            # 工作流示例
└─ tests/               # 基础流程测试
```

## ⚡ 快速开始

### 1. 获取项目

```bash
git clone https://github.com/Love-Neko/MoeDock.git
cd MoeDock
pip install -r requirements.txt
```

### 2. 打开预览台

直接双击 `dock_preview.html`。页面支持图库浏览、壁纸切换，以及 Dock 图标的平滑悬停缩放。

### 3. 使用生产脚本

```bash
# 去除白底并导出透明 PNG
python scripts/remove_bg.py -i input.jpg -o output.png

# 将 PNG 封装为多尺寸 ICO
python scripts/convert_ico.py -i output.png -o output.ico

# 根据 PNG 图标目录更新交互式预览页
python scripts/update_preview.py -i ./例图/PNG图标 -o ./dock_preview.html
```

## 🎨 已收录图标

当前示例覆盖创作、开发、社交、影音和数字资产等常用软件：

| 分类 | 图标示例 |
| --- | --- |
| Adobe 创作 | Photoshop、Premiere、After Effects、Illustrator、Lightroom、Media Encoder |
| 创作与开发 | Blender、DaVinci Resolve、VS Code |
| 社交与网络 | Google、Google Chrome、Telegram、微信、QQ、Clash Verge |
| 娱乐与资产 | Steam、OKX |

更多颜色和设计思路见 [`references/color_palette.md`](./references/color_palette.md)。

### 🖼️ 图标小样

<p align="center">
  <img src="./例图/PNG图标/Photoshop.png" alt="Photoshop" width="96" />
  <img src="./例图/PNG图标/Blender.png" alt="Blender" width="96" />
  <img src="./例图/PNG图标/Steam.png" alt="Steam" width="96" />
  <img src="./例图/PNG图标/Telegram.png" alt="Telegram" width="96" />
  <img src="./例图/PNG图标/VSCode.png" alt="VS Code" width="96" />
  <img src="./例图/PNG图标/微信.png" alt="微信" width="96" />
</p>

## 🖥️ 预览体验

预览台围绕 Dock 使用场景做了三点优化：

1. **悬停放大**：中心图标放大，左右图标同步退让，保持节奏感
2. **玻璃质感**：半透明容器、柔和阴影和多种背景方便检查对比度
3. **小尺寸检验**：图库卡片帮助快速确认图标在常见尺寸下是否清晰

## 🤝 贡献与反馈

欢迎提交 Issue 或 Pull Request，补充新的软件色卡、图标方案和处理脚本。提交素材时请尽量说明来源、授权范围和推荐使用场景。

## 📄 许可与素材说明

脚本和示例代码采用 MIT License。图标及品牌标识的版权归其原作者或对应品牌所有；本项目主要用于个人桌面美化、学习和设计展示，请在遵循相关授权条款的前提下使用。
