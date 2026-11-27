from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/members")
def members():
    return render_template("members_page.html")

if __name__ == "__main__":
    app.run(debug=True)