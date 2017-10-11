from flask import Flask, render_template, request, redirect, flash, session, url_for

app = Flask(__name__)
app.secret_key = "SECRET KEY"

USERNAME = 'test'
PASSWORD = 'pwd'

# Returns 0 for success, 1 for incorrect user, 2 for incorrect password
def auth(input_user, input_pass):
    if input_user == USERNAME:
       if input_pass == PASSWORD:
           session['username'] = input_user
           flash('Logged in')
           return 0
       else:
           flash('Incorrect password')
           return 2
    else:
        flash('Incorrect username')
        return 1

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return redirect(url_for('welcome'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if auth(username, password) == 0:
            return redirect(url_for('welcome'))
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username = session['username'])
    else:
        flash('You need to be logged in')
        return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session.pop('username')
    flash('Logged out')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
