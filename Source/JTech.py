from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, AdminForm
#from wtforms import Form, BooleanField, TextField, PasswordField, validators

app = Flask(__name__)

app.config['SECRET_KEY'] = '2fc491ad67ee3df280626236c529e510'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.Name.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form )

@app.route("/admin",  methods=['GET', 'POST'])
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        if form.email.data == 'jtech@website.com' and form.password.data == 'password':
            flash("You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('admin.html', title='Admin', form=form )


if __name__ == '__main__':
    app.run(debug=True)