from flask import Flask, render_template, url_for,  flash, redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] ='38d95e32c11f1ae9bc751c5834b7924ecf1c91860cb7da22b577b2b9d064fe6b'

posts = [
    {'author':'bas', 'title':'test', 'content':'dumsdklfmsld slkdmfcs'},
    {'author':'ram', 'title':'prod', 'content':'sdkjcs sdjcfnsdjfkjsd'},
    ]

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', posts=posts, title='jolio-gymkana')

@app.route('/about')
@app.route('/ABOUT')
def about():
    return render_template('about.html', posts=posts, title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)