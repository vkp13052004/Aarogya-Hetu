from flask import Flask, render_template, request
from app.rag_engine import get_medical_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        query = request.form.get("query", "")
        if request.files.get("audio"):
            audio_file = request.files["audio"]
            audio_file.save("user_input.wav")
            query = "user_input.wav"
        result = get_medical_response(query)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
