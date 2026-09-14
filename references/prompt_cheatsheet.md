# 二次元卡通 Dock 栏图标标准提示词工程手册 (Prompt Cheatsheet)

## 🎯 黄金生图提示词模板 (Golden Formula)

```text
Anime chibi character dock icon for [软件英文名与简称], in the style of a cute 2.5D mascot app icon sticker. 
The character is an adorable chibi anime girl with [角色发色与发型, 必须含软件标志性色彩] hair, styled as a cute [角色身份/职业设定, 如 gamer/video editor/painter/hacker], wearing a [服饰描述, 必须为软件主色调与白色/深色搭配] outfit. 
She is playfully [交互动作, 如 sitting on / hugging / riding / casting magic over] a giant 3D [软件标志性Logo实体化造型, 如 cube block / crankshaft / origami paper plane / ribbon] in [软件核心色彩与材质]. 
Small floating [周围微型符号/彩蛋挂件, 如 2-3 个微型浮空道具] gently float around her. 
The dominant colors MUST be [软件核心主色十六进制与英文, 需占70%视觉比例], making the app instantly recognizable from its color. 
High quality, crisp outlines, vibrant cel-shaded digital anime illustration, centered composition, on an isolated pure solid white background.
```

---

## 🔑 关键词模块库 (Modular Keywords Library)

### 1. 构图与背景约束词（必须保留）
* `centered composition`（居中构图，防止裁切）
* `on an isolated pure solid white background`（纯净实心白底，用于后续算法 100% 完美抠图）
* `2.5D mascot app icon sticker`（Q版拟人化应用图标贴纸风格）
* `crisp clean outlines, cel-shaded digital anime illustration`（利落线稿、赛璐珞二次元平涂与柔和高光）

# 二次元卡通 Dock 栏图标标准提示词工程手册 (Prompt Cheatsheet)

## 🎯 黄金生图提示词模板 (Golden Formula)

```text
Anime chibi character dock icon for [软件英文名与简称], in the style of a cute 2.5D mascot app icon sticker. 
The character is an adorable chibi anime girl with [角色发色与发型, 必须含软件标志性色彩] hair, styled as a cute [角色身份/职业设定, 如 gamer/video editor/painter/hacker], wearing a [服饰描述, 必须为软件主色调与白色/深色搭配] outfit. 
She is playfully [交互动作, 如 sitting on / hugging / riding / casting magic over] a giant 3D [软件标志性Logo实体化造型, 如 cube block / crankshaft / origami paper plane / ribbon] in [软件核心色彩与材质]. 
Small floating [周围微型符号/彩蛋挂件, 如 2-3 个微型浮空道具] gently float around her. 
The dominant colors MUST be [软件核心主色十六进制与英文, 需占70%视觉比例], making the app instantly recognizable from its color. 
High quality, crisp outlines, vibrant cel-shaded digital anime illustration, centered composition, on an isolated pure solid white background.
```

---

## 🔑 关键词模块库 (Modular Keywords Library)

### 1. 构图与背景约束词（必须保留）
* `centered composition`（居中构图，防止裁切）
* `on an isolated pure solid white background`（纯净实心白底，用于后续算法 100% 完美抠图）
* `2.5D mascot app icon sticker`（Q版拟人化应用图标贴纸风格）
* `crisp clean outlines, cel-shaded digital anime illustration`（利落线稿、赛璐珞二次元平涂与柔和高光）

### 2. 交互动作词（Interaction Verbs）
* `sitting joyfully on top of`（欢快端坐在...顶部，适合 3D 方块/底座）
* `hugging tightly with both hands`（双手紧抱，适合抱枕/猫咪盾牌/玩偶）
* `playfully riding on`（欢快骑乘在...上滑翔，适合纸飞机/飞艇/机械轴）
* `holding a giant glowing ... tool`（手持发光的巨大工具，如剪刀/数位笔/钢笔/扳手）

### 3. 周围氛围微型道具词（Floating Props）
* 代码类：`glowing cyan curly brackets { }, semicolon ;, pixel cat`
* 视频类：`holographic play/pause buttons, colorful audio waveform bars, film reels`
* 绘图类：`floating layer stack cards, holographic color swatches, starry magic sparkle trails`
* 游戏类：`miniature game controllers, golden coin stars, fluffy white steam puffs`

---

## 🤖 针对三大多模态 AI 平台的实战提示词模板 (Platform-Specific Prompts)

### 1. ChatGPT (DALL-E 3) 专用模板（防扩写 & 强制纯白底）
> **注意**：DALL-E 3 会自动重写 Prompt 导致增加杂乱地板/阴影。请在提示词前加上强制约束声明：
```text
I need to generate a 2.5D app icon sticker. Do NOT add detailed backgrounds, floors, or realistic textures.
Prompt: Die-cut chibi anime sticker icon for [软件名], 2.5D mascot style. An adorable anime girl with [主色] hair wearing [主色搭配服饰], joyfully sitting on top of a giant 3D [标志性实体道具]. Floating 2-3 tiny [周围彩蛋道具]. The dominant color is [品牌色HEX与英文], occupying 70% of visual space. Crisp clean outlines, vibrant cel-shaded anime colors, completely isolated on a flat pure solid white #FFFFFF background, zero drop shadows on the floor, flat lighting, centered composition.
```

### 2. Claude (辅助用户生成 Midjourney v6 提示词)
> **注意**：Claude 原生无图像生成，应直接为用户生成可直接粘贴到 Midjourney / Nijijourney 的标准命令：
```text
/imagine prompt: Anime chibi character dock icon for [软件名], cute 2.5D mascot app sticker style, [角色与发色服饰描述], interacting with a giant 3D [品牌实体道具], floating [微型彩蛋道具], dominant [品牌主色HEX] color scheme, crisp vector outlines, cel shaded, sticker die-cut contour, centered composition, on isolated pure solid white background --ar 1:1 --v 6.0 --style raw --s 50 --no background, floor shadow, gradient, realistic textures
```

### 3. Antigravity 自动化生图工具提示词
> **注意**：直接传入 `generate_image` 工具，长句英文描述配合 `AspectRatio: '1:1'`：
```text
Anime chibi character dock icon for [软件名], in the style of a cute 2.5D mascot app icon sticker. The character is an adorable chibi anime girl with [品牌主色] hair, wearing a [品牌主色+白色] outfit. She is playfully sitting on top of a giant 3D [实体化Logo造型] in glossy [品牌核心色]. Small floating [2-3个微型道具] gently float around her. The dominant colors MUST be [品牌主色HEX], vibrant cel-shaded digital anime illustration, centered composition, on an isolated pure solid white background.
```
