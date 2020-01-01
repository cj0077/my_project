# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
app.config['SECRET_KEY'] = '4e6301face61813dc43a7a96d8bf7ead'

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

posts = [
    {
        'author': 'Margaret Atwood',
        'title': 'The Testaments',
        'content': "Atwood 'more urgent than ever'",
        'date_posted': '01/01/2019'
    },

    {
        'author': 'Bernardine Evaristo',
        'title': 'Girl Woman Other',
        'content': "'Evaristo's 'groundbreaking' characters'",
        'date_posted': '01/01/2019'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
