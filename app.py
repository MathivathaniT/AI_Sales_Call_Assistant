
from flask import Flask, render_template, request
from analyzer import analyze_call

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        conversation = request.form.get("conversation")
        result = analyze_call(conversation)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
