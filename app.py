from flask import Flask, render_template

app = Flask(__name__)

@app.route("/design")
def design():
    return render_template("design.html")


