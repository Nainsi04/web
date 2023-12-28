from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mydatabase'
mysql = MySQL(app)

# Routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Handle login logic and database connection
    if request.method == 'POST':
        # Fetch username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Implement your login logic here, e.g., querying the database
        # If login is successful, redirect to the dashboard
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Implement logout logic
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission and database connection
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save the data to the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        mysql.connection.commit()
        cur.close()

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
