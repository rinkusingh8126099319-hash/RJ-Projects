
from flask import Flask, render_template
from email_sender import send_email

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home_dashboard_page.html")


@app.route("/login_page")
def login_page():
    return render_template("login_page.html")


@app.route("/create_a_new_account_page")
def create_account():
    return render_template("create_a_new_account_page.html")


@app.route("/otp_varification_page")
def otp_verification():
    return render_template("otp_varification_page.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
