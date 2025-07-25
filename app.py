from flask import Flask, render_template, session, redirect, url_for
from config import Config
from auth.routes import auth_bp
from auth.users import create_user_table
from auth.audit import create_audit_table

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth_bp)

# Inisialisasi DB
create_user_table()
create_audit_table()

@app.route("/")
def dashboard():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)

