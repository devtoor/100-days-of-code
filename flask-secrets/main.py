from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Email, InputRequired, Length

app = Flask(__name__)
app.secret_key = "dnlkv4cxnvf123ksljnmnio1wokjon"
Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[InputRequired(), Email()])
    password = PasswordField(
        label="Password",
        validators=[InputRequired(), Length(min=8)],
    )
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
