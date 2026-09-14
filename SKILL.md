---
name: anime-dock-icon
description: >-
  Comprehensive workflow and production pipeline for designing, generating, transparent
  background processing, and multi-format packaging of anime chibi Dock and desktop icons.
  Use this skill whenever creating, modifying, converting, or batch-processing anime-themed
  app icons for Dock bars (MyDockFinder, BitDock, macOS Dock) or Windows desktop shortcuts.
---

# 二次元卡通 Dock 栏图标设计与生产工作流技能 (Anime Dock Icon Skill)

本技能提供了一套标准化的**二次元卡通拟人化 Dock 栏应用图标**完整制作管线。涵盖从**软件品牌色彩提炼**、**图标实体道具化构思**、**标准中英文生图 Prompt 编写**、**自动化抗锯齿透明底扣图**、**Windows 原生多层级 .ico 生成**到**本地交互式 Dock 栏动效预览**的完整流程。

---

## 目录结构 (Directory Structure)

```text
anime-dock-icon/
├── SKILL.md                          # 本技能主指引文件（含多平台适配指南）
├── requirements.txt                  # Python 环境依赖清单
├── scripts/
│   ├── pipeline.py                   # 一键端到端全自动生产总装流水线（抠图+打包+预览）
│   ├── remove_bg.py                  # 自动化白底抠图脚本（带抗锯齿、种子内孔与贴纸白边）
│   ├── convert_ico.py                # Windows 多尺寸高清 .ico 打包转换脚本（单文件/批量双模）
│   └── update_preview.py             # 生成/热更新本地交互式 Dock 预览网页（离线兜底+搜索）
├── references/
│   ├── prompt_cheatsheet.md          # 标准化中英文生图提示词工程模板与修饰词库
│   └── color_palette.md              # 常用软件品牌专属色卡（HEX）与核心视觉符号表（已扩展）
├── examples/
│   └── workflow_example.md           # 完整端到端制作实战案例（以 Photoshop 与 Blender 为例）
└── tests/
    └── test_pipeline.py              # 全管线自动化回归测试集
```

## 环境要求 (Requirements)

- Python 3.9+
- Pillow >= 9.0
- NumPy >= 1.21

安装依赖：

```bash
python -m pip install -r requirements.txt
```

---

## 🌐 三大 AI 平台协同与执行矩阵 (Platform Matrix)

本 Skill 可用于具备图像生成、文本生成或本地代码执行能力的 AI 宿主。各平台的具体能力以当前环境为准：

| 平台维度 | 对话式图像生成平台 | 支持本地执行的智能体环境 | 可生成提示词和代码的文本模型环境 |
| :--- | :--- | :--- | :--- |
| **核心定位** | 生成图像并配合本地脚本处理 | 端到端运行脚本并写入项目目录 | 设计提示词、审查结果并给出命令 |
| **生图方案** | 使用宿主实际提供的图像模型与参数 | 使用宿主实际提供的图像工具 | 输出适配目标图像平台的提示词 |
| **代码执行** | 若宿主支持则运行 `pipeline.py` | 直接运行 Python 脚本 | 由用户或连接的开发工具执行脚本 |
| **结果呈现** | 展示 PNG、ICO 和本地预览页 | 写入目标目录并刷新预览页 | 以内嵌预览或本地浏览器查看结果 |

> 具体模型、图像工具和代码执行能力以当前宿主平台实际提供的工具为准；本 Skill 不要求某个固定模型或工具名称。

---

## 核心设计三大准则 (Three Core Design Principles)

在 Dock 栏环境（通常尺寸仅为 48px ~ 96px）中，为了确保**“即使不仔细看角色，仅凭大色块和外轮廓也能瞬间秒认出是什么软件”**，必须贯彻以下三条准则：

1. **色彩第一识别性（70% Color Dominance）**：
   - 绝不使用随意的角色发色和服饰颜色。
   - 角色的**发色、核心服饰（外套/工装裙/连帽衫）以及巨型互动底座/坐骑**，必须严格提取该软件的官方品牌主色。
   - 例如：Blender 必须是亮橙发+橙白工装；VS Code 必须是钴蓝卫衣；Steam 必须是深空蓝黑工装+蒸汽蓝光。

2. **图标符号“3D实体道具化”（Logo Propification）**：
   - 拒绝扁平贴图！必须将软件的原生 Logo 实体化为角色正在互动的 3D 道具：
     - **底座/坐骑类**：3D 浮雕立方体（如 Adobe 系列）、巨型机械曲柄阀门（Steam）、巨型折纸飞机（Telegram）、三叉射线底盘（Blender）。
     - **手持/互动物**：星光数位笔与图层（Ps）、金色剪刀与胶片时间轴（Pr）、关键帧菱形钻石（Ae）、贝塞尔金色钢笔（Ai）、3D 甜甜圈（Blender）、赛博猫猫防伪盾（Clash Verge）。

3. **高纯净透明通道与贴纸轮廓（Clean Alpha & Sticker Silhouette）**：
   - Dock 图标必须是高质量的透明背景（RGBA PNG）。
   - 边缘带有平滑抗锯齿羽化（或细腻的白边贴纸 Die-cut 轮廓），保证在深色、浅色或杂乱动态壁纸下均能清晰凸显。
   - 内部封闭空隙（如丝带内孔、曲线环内孔、机械轴承缝隙）必须彻底透空。

---

## 标准制作执行步骤 (Standard Production Pipeline)

### 第一步：色彩与道具方案策划 (Conceptualization)
1. 查阅 [color_palette.md](./references/color_palette.md) 获取目标软件的标准 Hex 色值与标志性道具（涵盖 Adobe 全家桶、Google Chrome、Steam、Discord 等）。
2. 确定角色职业人设（如剪辑师、黑客、工匠、画师、信使）。

### 第二步：生成专业英文生图 Prompt
1. 查阅 [prompt_cheatsheet.md](./references/prompt_cheatsheet.md) 选择对应平台的专用模板：
   - **图像生成平台**：使用带防扩写与 `#FFFFFF` 强制纯白底的前缀。
   - **提示词模型**：获取适配目标平台的参数与负面约束。
   - **本地智能体**：调用当前环境可用的图像工具并生成 1:1 图像。

### 第三步：一键流水线总装 (推荐)
只需一条命令，自动完成背景抠图、多层级 ICO 打包并热更新预览台：
```bash
python scripts/pipeline.py --input raw_icon.jpg --name Chrome --png-dir ./PNG --ico-dir ./ICO --preview ./dock_preview.html
```

---

### 分步执行命令备忘 (Modular Commands)

若需要对各环节进行精细微调，可独立调用各模块：

* **自动化抗锯齿透明底抠图**：
  ```bash
  python scripts/remove_bg.py --input <input.jpg> --output <output.png> --tol 245 --seeds "150,200;300,400" --sticker 2
  ```
  - `--tol`：纯白容差（默认 245）。
  - `--seeds`：指定封闭内孔的种子点坐标 `y,x`，自动透空环形孔隙。
  - `--sticker`：可选，生成像素宽度的纯白贴纸描边（极大增强深色壁纸辨识度）。

* **Windows 多分辨率原生 `.ico` 打包**（单文件或目录双模）：
  ```bash
  # 单文件转换
  python scripts/convert_ico.py -i Chrome.png -o Chrome.ico
  # 批量转换
  python scripts/convert_ico.py -i ./PNG -o ./ICO
  ```

* **刷新本地交互式 Dock 预览台**：
  ```bash
  python scripts/update_preview.py --input ./PNG --output ./dock_preview.html
  ```

---

## 验收清单 (QA Checklist)

- [ ] **色彩比例**：软件核心品牌色在角色发型、服装或道具上占据 70% 视觉比例。
- [ ] **透明通道**：PNG 严格为 RGBA 模式，外沿平滑无脏灰边，封闭内孔透空。
- [ ] **极小尺寸辨识度**：图标缩放至 16px/32px/48px 时轮廓清晰可辨。
- [ ] **ICO 规格完整**：单文件打包内置 256/128/64/48/32/16 全层级分辨率。
- [ ] **双壁纸兼容**：在极夜黑与浅色壁纸下均有良好对比度（推荐搭配 2px 贴纸微白边）。
- [ ] **离线可访问**：`dock_preview.html` 在完全无网络环境下仍保持完整网格与 Dock 缩放动效。
