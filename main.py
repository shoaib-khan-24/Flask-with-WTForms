import wtforms.validators
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5

CORRECT_EMAIL = "admin@email.com"
CORRECT_PASSWORD = "12345678"

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "rangeen billi"


class LoginForm(FlaskForm):
    email = EmailField("Enter your email: ", validators=[DataRequired(message="Email must be filled!"), Email()])
    password = PasswordField("Enter your password: ",
                             validators=[DataRequired("Password must be filled!"), wtforms.validators.Length(min=8)])
    submit = SubmitField("log in")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        entered_email = form.email.data
        entered_password = form.password.data

        if entered_email == CORRECT_EMAIL and entered_password == CORRECT_PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
