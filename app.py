from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# theme
fire_weed = "#7D362E"
sha_green = "#CBC99D"

# define sqlite db, create books table
connect = sqlite3.connect('numb.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS BOOKS (name TEXT, \
    author TEXT)')

@app.route('/')
def home():
    return render_template('home.html', primary_bold_color=fire_weed, trim_color=sha_green)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        with sqlite3.connect("numb.db") as books:
            cursor = books.cursor()
            cursor.execute("INSERT INTO BOOKS \
            (name,author) VALUES (?,?)",
                           (name, author))
            books.commit()
        return render_template("books.html")
    else:
        return render_template('book_form.html')
    
@app.route('/list_books')
def list_books():
    connect = sqlite3.connect('numb.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM BOOKS')

    data = cursor.fetchall()
    return render_template("list_books.html", data=data)

@app.route('/info')
def info():
    # return f"Current route: {request.url_rule}"
    return f"Current endpoint: {request.url_rule.endpoint}"

if __name__ == '__main__':
    app.run(debug=True)