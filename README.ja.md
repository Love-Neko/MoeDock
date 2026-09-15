# 🎨 MoeDock · アニメ Dock アイコン制作ワークショップ

<p align="center"><a href="./README.md">简体中文</a> · <a href="./README.en.md">English</a> · <a href="./README.ja.md">日本語</a></p>

<p align="center"><img src="./preview.gif" alt="MoeDock プレビュー" width="100%" /></p>

<p align="center"><strong>いつものアプリを、個性あふれるデスクトップパートナーに。</strong><br>透明 PNG、多サイズ ICO、インタラクティブな Dock プレビューまで、オフラインで使える制作ワークフローを提供します。</p>

<p align="center">
  <img src="https://img.shields.io/badge/Style-2.5D%20Chibi%20Anime-ff69b4.svg" alt="Style" />
  <img src="https://img.shields.io/badge/Assets-PNG%20%7C%20ICO-8a2be2.svg" alt="Assets" />
  <a href="https://github.com/Love-Neko/MoeDock/actions/workflows/ci.yml"><img src="https://github.com/Love-Neko/MoeDock/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" /></a>
</p>

## 📖 MoeDock とは？

MoeDock は、デスクトップ Dock やアプリランチャー向けのアニメ風・擬人化アイコン素材と制作ツールです。ブランドカラーやロゴの特徴を、 小さなサイズでも見分けやすいちびキャラクターとして表現します。

透明 PNG、Windows 用の 16～256 px ICO、完全オフラインのプレビュー、一括の背景除去・変換・プレビュー更新パイプラインを収録しています。

## ✨ 主な機能

- **ブランドカラーを優先:** アプリをひと目で識別できます。
- **ロゴの立体化:** ロゴを道具、乗り物、アクセサリーとして表現します。
- **きれいなアルファ:** アンチエイリアス付き透明背景と、任意のステッカー縁取り。
- **多サイズ ICO:** 16、32、48、64、128、256 px を 1 ファイルに格納。
- **オフラインプレビュー:** 検索、壁紙切替、ホバー拡大をブラウザで確認できます。
- **ワンコマンド制作:** 背景除去、PNG/ICO 作成、プレビュー更新を自動化。

## 🧭 プロジェクト構成

```text
MoeDock/
├─ 例图/                  # PNG / ICO のサンプル素材
├─ dock_preview.html      # 単体で動作するプレビュー
├─ scripts/               # 制作・パッケージ用スクリプト
├─ references/            # プロンプトとカラーレファレンス
├─ examples/              # ワークフロー例
└─ tests/                 # 回帰テスト
```

## ⚡ クイックスタート

```bash
git clone https://github.com/Love-Neko/MoeDock.git
cd MoeDock
pip install -r requirements.txt
```

`dock_preview.html` をブラウザで直接開いてください。新しいアイコンを制作するには:

```bash
python scripts/pipeline.py -i input.jpg -n Steam --png-dir ./例图/PNG图标 --ico-dir ./例图/ICO图标 -p ./dock_preview.html
```

個別の処理は `scripts/remove_bg.py`、`scripts/convert_ico.py`、`scripts/update_preview.py` を参照してください。

## 🖥️ アイコンの利用方法

- **Windows:** ショートカットのプロパティ → アイコンの変更で ICO を選択。
- **MyDockFinder / BitDock:** `例图/PNG图标/` の PNG を指定。
- **macOS:** アプリの情報を見るを開き、PNG をアイコンへドラッグ。

## 🤝 コントリビューション

新しいアプリのデザイン、ブランドカラー、プロンプト、パイプライン改善の Issue / Pull Request を歓迎します。

## 📄 ライセンス

コードは [MIT License](./LICENSE) で公開しています。アプリの商標・ロゴは各権利者に帰属します。
