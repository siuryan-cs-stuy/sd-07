from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "SECRET KEY"

USERNAME = 'test'
PASSWORD = 'pwd'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return redirect(url_for('welcome'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME:
            if password == PASSWORD:
                session['username'] = username
                return redirect('/welcome')
            else:
                return render_template('index.html', error = 'password')
        else:
            return render_template('index.html', error = 'username')
        
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username = session['username'])
    else:
        return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
