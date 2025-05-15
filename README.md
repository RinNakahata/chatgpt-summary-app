# ChatGPT要約アプリ（Flask × OpenAI API連携）

このアプリは、Flaskを用いて構築された日本語文章の要約アプリです。
OpenAIのChatGPT API（gpt-3.5-turbo）と連携し、入力された文章を自動で要約します。

## 🛠 使用技術

- Python 3.x
- Flask
- OpenAI API（gpt-3.5-turbo）
- HTML（Jinja2テンプレート）
- dotenv（APIキー管理）

## 🔧 セットアップ方法

1. リポジトリをクローン

```bash
git clone https://github.com/your-username/chatgpt-summary-app.git
cd chatgpt-summary-app
```

2. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

3. `.env` ファイルを作成し、OpenAI APIキーを記述

```
OPENAI_API_KEY=sk-xxxxxxx...
```

4. アプリケーションを起動

```bash
python app.py
```

5. 以下のURLにアクセス

```
http://127.0.0.1:5000/
```

## 📄 使用方法

- テキストボックスに要約したい日本語の文章を入力し、「送信」ボタンをクリックします。
- ChatGPTが文章の要点を抽出し、簡潔に要約した内容が画面に表示されます。

## 🧠 ロジック概要

- Flaskがフォーム入力を受け取り、POSTリクエストとして処理
- 入力文をOpenAI APIへ送信し、`gpt-3.5-turbo`モデルで要約を取得
- 取得した要約をHTMLテンプレートへ渡して画面に表示

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたは優秀な日本語の要約アシスタントです。"},
        {"role": "user", "content": f"次の文章を要約してください：{input_text}"}
    ]
)
summary = response.choices[0].message.content
```

## 📁 ファイル構成

chatgpt-summary-app/
├── app.py  ← メインアプリケーション
├── .env    ← OpenAI APIキーを設定
└── templates/
    └── index.html  ← 入力・出力フォーム

## 💡 補足

- `.env`ファイルを使用することで、APIキーを安全に管理しています。
- 実行には有効なOpenAI APIキーが必要です。無料枠を超えた場合は課金が必要です。
- 本アプリは学習およびポートフォリオ目的で制作されています。

## ✍ 作者
- 名前：Rin Nakahata
- 技術ブログ（note）：[note記事はこちら](https://note.com/rin_nakahata/n/n903afd29672f)

## 📜 ライセンス

このプロジェクトはMITライセンスの下で提供されています。

