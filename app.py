# Flaskから必要な関数をインポート（Webアプリの基本機能）
from flask import Flask, render_template, request

# OpenAIのAPIライブラリ
import openai

# 環境変数（APIキーなど）を扱うための標準ライブラリ
import os

# .envファイルから環境変数を読み込むためのライブラリ
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()

# OpenAIクライアントを初期化（APIキーを環境変数から取得）
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Flaskアプリのインスタンスを作成
app = Flask(__name__)


# ルートURL（"/"）にアクセスしたときの処理を定義（GET/POST対応）
@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""  # 初期状態では要約は空
    if request.method == "POST":
        # フォームから送信された文章を取得
        input_text = request.form["text"]

        # OpenAIのChat APIを呼び出して要約を依頼
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 使用するAIモデル
            messages=[
                {"role": "system", "content": "あなたは優秀な日本語の要約アシスタントです。"},
                {"role": "user", "content": f"次の文章を要約してください：{input_text}"}
            ]
        )

        # AIからの返答（要約文）を取得
        summary = response.choices[0].message.content

    # 結果をHTMLテンプレートに渡して表示
    return render_template("index.html", summary=summary)


# このファイルが直接実行された場合のみ、開発用サーバーを起動
if __name__ == "__main__":
    app.run(debug=True)
