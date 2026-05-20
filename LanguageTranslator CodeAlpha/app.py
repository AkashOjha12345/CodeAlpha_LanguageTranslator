from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    error_message = None
    text = ""
    source_lang = "auto"
    target_lang = "hi"

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        source_lang = request.form.get("source", "auto")
        target_lang = request.form.get("target", "hi")

        try:
            translated_text = GoogleTranslator(
                source=source_lang,
                target=target_lang
            ).translate(text)
        except Exception as exc:
            translated_text = ""
            error_message = f"Translation failed: {exc}"

    return render_template(
        "index.html",
        translated_text=translated_text,
        error_message=error_message,
        text=text,
        source_lang=source_lang,
        target_lang=target_lang
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)