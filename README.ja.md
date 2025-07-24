<div align="center">

# 🚀 Rich Run

[![GitHub License](https://img.shields.io/github/license/tanganke/rich-run)](https://github.com/tanganke/rich-run/blob/main/LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/rich-run)](https://pypi.org/project/rich-run/)
[![Downloads](https://static.pepy.tech/badge/rich-run/month)](https://pepy.tech/project/rich-run)
[![GitHub stars](https://img.shields.io/github/stars/tanganke/rich-run?style=social)](https://github.com/tanganke/rich-run)

**美しく情報豊富な出力でコマンドライン体験を変革する**

[English](README.md) | [中文](README.zh.md) | 日本語

</div>

Rich Run は、コマンドを優雅でカラフルなパネルで包み、タイムスタンプ、明確な成功/失敗インジケーター、美しいフォーマットを提供することで、ターミナル体験を向上させるコマンドラインラッパーです。シンプルで退屈なコマンド出力とはお別れしましょう！

## 📋 目次

- [✨ 機能](#-機能)
- [📦 インストール](#-インストール)
- [🚀 使用方法](#-使用方法)
- [📸 サンプル](#-サンプル)
- [🎯 使用例](#-使用例)
- [🛠️ 開発](#️-開発)
- [❓ FAQ](#-faq)
- [🤝 コントリビューション](#-コントリビューション)
- [📄 ライセンス](#-ライセンス)
- [🙏 謝辞](#-謝辞)

<div align="center">
<img src="docs/images/example.png" alt="Rich Run デモ" width="350">
</div>

## ✨ 機能

- 🎨 **美しい出力**：コマンドが優雅でカラフルなパネルに包まれます
- ⏰ **タイムスタンプ**：コマンドの開始と終了時刻を正確に表示
- ✅ **ステータスインジケーター**：終了コードと共に成功/失敗の明確な視覚的フィードバック
- 🌈 **リッチフォーマット**：強力な `rich` ライブラリを活用した素晴らしいターミナル出力
- 📦 **簡単インストール**：pip または pipx でゼロ設定でインストール
- 🚀 **ドロップイン置換**：既存のコマンドに `rich-run` を前置するだけ
- 🔧 **汎用互換性**：あらゆるコマンドラインツールやスクリプトに対応
- 📊 **進行状況の可視化**：コマンド実行フローを一目で確認

## 📦 インストール

### オプション 1：pipx（推奨）

[pipx](https://pipx.pypa.io/) は分離された環境にパッケージをインストールし、依存関係の競合を防ぎます：

```bash
# pipx がインストールされていない場合は、`pip install pipx` で先にインストールできます
pipx install rich-run
```

### オプション 2：pip

```bash
pip install rich-run
```

### オプション 3：ソースから

```bash
git clone https://github.com/tanganke/rich-run.git
cd rich-run
pip install -e .
```

> [!NOTE]  
> Rich Run は `rich-cli` に依存しています。パッケージと一緒に自動的にインストールされますが、問題が発生した場合は手動でインストールできます：
>
> ```bash
> pipx install rich-cli  # または pip install rich-cli
> ```

## 🚀 使用方法

Rich Run は、あらゆるコマンドを実行するためのドロップイン置換として設計されています。既存のコマンドに `rich-run` を前置するだけです：

### 基本構文

```bash
rich-run <あなたのコマンド>
```

### クイックサンプル

```bash
# シンプルなコマンド
rich-run echo "Hello, Rich World!"
rich-run ls -la
rich-run pwd

# Python スクリプト
rich-run python my_script.py
rich-run python -c "print('Hello from Python!')"

# システムコマンド
rich-run wget https://example.com/file.zip

# パイプやリダイレクトを含む複雑なコマンド（引用符を使用）
rich-run "ls -la | grep .py | wc -l"
rich-run "echo 'data' > output.txt && cat output.txt"
```

## 📸 サンプル

### 表示される内容

Rich Run でコマンドを実行すると、以下が表示されます：

1. **📋 コマンドパネル**：正確なコマンドと開始タイムスタンプを表示する青いヘッダー
2. **📄 クリーンな出力**：コマンドの出力が明確に表示されます
3. **✅ ステータスパネル**：成功/失敗ステータスと実行時間を示すカラフルなフッター

### 出力サンプル

**成功したコマンド：**

```bash
rich-run echo "Success!"
```

終了コード 0 の緑色の成功パネルが表示されます。

**失敗したコマンド：**

```bash
rich-run ls /nonexistent
```

実際の終了コードと共に赤色のエラーパネルが表示されます。

**長時間実行されるコマンド：**

```bash
rich-run sleep 3 && echo "Done!"
```

実行時間を追跡するためのタイムスタンプが表示されます。

## 🎯 使用例

Rich Run は以下の用途に最適です：

- **📊 監視スクリプト**：自動化スクリプトの実行ステータスを追跡
- **🔍 デバッグ**：複雑なワークフローでコマンドの成功/失敗を明確に確認
- **📚 学習**：コマンド実行と終了コードをより良く理解
- **🎨 プレゼンテーション**：ターミナルデモをより視覚的に魅力的に
- **📝 ドキュメント**：クリーンでフォーマットされたコマンド例を生成
- **🔧 CI/CD**：ビルドスクリプト出力の読みやすさを向上
- **👥 チーム協力**：より情報豊富なコマンド出力を共有

## 🛠️ 開発

### 開発環境のセットアップ

```bash
# リポジトリをクローン
git clone https://github.com/tanganke/rich-run.git
cd rich-run

# 仮想環境を作成（オプションですが推奨）
python -m venv venv
source venv/bin/activate  # Windows では: venv\Scripts\activate

# 開発モードでインストール
pip install -e .

# 開発依存関係をインストール（追加した場合）
pip install -e ".[dev]"  # pyproject.toml に開発依存関係を追加した場合
```

### プロジェクト構造

```
rich-run/
├── rich_run/           # メインパッケージ
├── docs/               # ドキュメント資産
├── pyproject.toml      # プロジェクト設定
└── README.md
```

## ❓ FAQ

<details>
<summary><strong>Q: Rich Run はすべてのコマンドで動作しますか？</strong></summary>

A: はい！Rich Run はあらゆるコマンドラインツール、スクリプト、バイナリで動作します。実行とフォーマットをラップするだけです。
</details>

<details>
<summary><strong>Q: スクリプトや CI/CD で Rich Run を使用できますか？</strong></summary>

A: もちろんです！Rich Run は終了コードを保持し、自動化環境で正常に動作します。
</details>

<details>
<summary><strong>Q: Rich Run はコマンドのパフォーマンスに影響しますか？</strong></summary>

A: オーバーヘッドは最小限です - パネルのフォーマットと表示にかかる時間だけです。
</details>

<details>
<summary><strong>Q: 出力フォーマットをカスタマイズできますか？</strong></summary>

A: 現在、Rich Run は固定フォーマットを使用していますが、カスタマイズ機能は将来のバージョンで追加される可能性があります。
</details>

<details>
<summary><strong>Q: コマンドが対話型入力を必要とする場合はどうなりますか？</strong></summary>

A: Rich Run は stdin を通すため、対話型コマンドは正常に動作します。
</details>

## 🤝 コントリビューション

コントリビューションを歓迎します！以下の方法でお手伝いいただけます：

### コントリビューションの方法

- 🐛 **バグレポート**：問題を発見しましたか？[Issue を開く](https://github.com/tanganke/rich-run/issues)
- 📝 **ドキュメント**：ドキュメントの改善にご協力ください
- 🔧 **コード**：バグ修正や新機能のプルリクエストを送信

### 開発ワークフロー

1. リポジトリをフォーク
2. 機能ブランチを作成：`git checkout -b feature/amazing-feature`
3. 変更を加える
4. 該当する場合はテストを追加
5. 変更をコミット：`git commit -m 'Add amazing feature'`
6. ブランチにプッシュ：`git push origin feature/amazing-feature`
7. プルリクエストを開く

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています - 詳細は [LICENSE](LICENSE) ファイルをご覧ください。

## 🙏 謝辞

- **[Rich](https://github.com/Textualize/rich)**：美しいターミナル出力を支える素晴らしいライブラリ
- **[Rich-CLI](https://github.com/Textualize/rich-cli)**：Rich のコマンドラインインターフェース
- **コミュニティ**：Rich Run の改善に貢献するすべてのコントリビューターとユーザーに感謝
