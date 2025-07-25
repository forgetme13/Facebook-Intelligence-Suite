from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from auth.users import verify_user
from auth.audit import log_action
from config import Config
import smtplib
from email.mime.text import MIMEText

auth_bp = Blueprint("auth", __name__)

def send_login_email(user):
    msg = MIMEText(f"User '{user}' berhasil login ke sistem OSINT.")
    msg["Subject"] = "Notifikasi Login OSINT"
    msg["From"] = Config.MAIL_DEFAULT_SENDER
    msg["To"] = Config.MAIL_USERNAME

    try:
        server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
        server.starttls()
        server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"[!] Gagal kirim email notifikasi: {e}")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if verify_user(username, password):
            session["user"] = username
            log_action(username, "Login berhasil")
            send_login_email(username)
            return redirect(url_for("dashboard"))
        else:
            flash("Login gagal. Username atau password salah.", "danger")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    user = session.pop("user", None)
    if user:
        log_action(user, "Logout")
    flash("Anda telah logout.", "info")
    return redirect(url_for("auth.login"))

