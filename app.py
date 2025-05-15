from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        input_text = request.form["text"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは優秀な日本語の要約アシスタントです。"},
                {"role": "user", "content": f"次の文章を要約してください：{input_text}"}
            ]
        )
        summary = response.choices[0].message.content
    return render_template("index.html", summary=summary)


if __name__ == "__main__":
    app.run(debug=True)
