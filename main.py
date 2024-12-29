from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '111111111111'  # Replace with a secure key

# Dummy user data for demonstration
users = {
    'admin': 'admin',
    'user': 'user'
}

@app.route('/')
def home():
    if 'username' in session:
        return f"Hello, {session['username']}! <br><a href='/logout'>Logout</a>"
    return "<a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists and the password matches
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials! Please try again.<br><a href='/login'>Login</a>"

    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


