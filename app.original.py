from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
# app = Flask(__name__, static_url_path='', static_folder='assets',)
# app = Flask(__name__, static_folder='static')
# app._static_folder = ''
# app = Flask(__name__, static_folder=<path>)

#fire_weed = "#FFFF00"
fire_weed = "#7D362E"
sha_green = "#CBC99D"

connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS BOOKS (name TEXT, \
    author TEXT)')

# @app.route('/join', methods=['GET', 'POST'])

@app.route('/')
def home():
    # return "<h1>Welcome to the Home Page!</h1><p>This is the main page of our application.</p>"
    # Renders index.html, which extends base.html and includes _nav.html
    
    return render_template('home.html', primary_bold_color=fire_weed, trim_color=sha_green)

@app.route('/blog')
def blog():
    # return "<h1>Our Blog</h1><p>Read our latest articles and updates here.</p>"
    return render_template('blog.html')

@app.route('/books')
def books():
    # return "<h1>Our Books Collection</h1><p>Explore our selection of books.</p>"
    return render_template('books.html')

@app.route('/info')
def info():
    # return f"Current route: {request.url_rule}"
    return f"Current endpoint: {request.url_rule.endpoint}"

if __name__ == '__main__':
    app.run(debug=True)