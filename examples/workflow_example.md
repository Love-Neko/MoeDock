# 制作实战全流程示例 (Workflow Example)

以制作 **Adobe Photoshop** 图标为例，演示标准执行链路：

### 阶段一：提炼核心特征
1. **色彩确定**：主色锁定 Photoshop 皇家青蓝 (`#31A8FF`)，底座为暗夜深蓝 (`#001E36`)。
2. **符号实体化**：选择 3D 浮雕 Ps 立方体作为底座；角色职业设定为数字画师，手持星光数位魔杖笔，周围环绕图层卡片。

### 阶段二：组装 Prompt 并生成
```text
Anime chibi character dock icon for Adobe Photoshop (PS) graphic software, matching the art style, clean line art, and cute aesthetic. The character is an adorable chibi anime digital artist girl with sapphire-blue hair and a stylish cyan painter beret, wearing a cozy navy blue artist coat with cyan (#31A8FF) trim. She is sitting joyfully on top of a giant 3D dark navy-blue cube block embossed with the iconic glowing cyan letters 'Ps'. She holds a giant glowing magical digital stylus pen, playfully drawing a swirling, starry cyan luminous brush stroke in the air. Tiny floating holographic color picker swatches and layer cards gently hover around her. The dominant colors must be authentic Photoshop Royal Cyan Blue (#31A8FF) and deep navy (#001E36). High quality, crisp lines, cel-shaded anime sticker illustration, centered, on an isolated pure white background.
```

### 阶段三：执行扣图与生成透明底
```bash
python scripts/remove_bg.py --input raw_photoshop.jpg --output Photoshop.png
```
*自动清除白底并对边缘进行平滑羽化。*

### 阶段四：打包 Windows 高清 ICO 图标
```bash
python scripts/convert_ico.py --input-dir . --output-dir ./ICO
```
*生成包含从 16x16 到 256x256 多尺寸的高清 `Photoshop.ico`。*

### 阶段五：在 Dock 栏与动效预览台中实测
运行 `python scripts/update_preview.py --input-dir . --output ./dock_preview.html` 并双击打开 `dock_preview.html`，切换浅色和深色壁纸，检查在深浅底下的边缘纯净度与色彩表现。
