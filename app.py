from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# theme
fire_weed = "#7D362E"
sha_green = "#CBC99D"

# define sqlite db, create books table
connect = sqlite3.connect('numb.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS BOOKS (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, \
    author TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)')

@app.route('/')
def home():
    return render_template('home.html', primary_bold_color=fire_weed, trim_color=sha_green)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/books')
def books():
    connect = sqlite3.connect('numb.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM BOOKS')

    data = cursor.fetchall()
    connect.close()
    return render_template("books.html", data=data)
    
@app.route('/add_book',  methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        with sqlite3.connect("numb.db") as books:
            cursor = books.cursor()
            cursor.execute("INSERT INTO BOOKS \
            (name,author) VALUES (?,?)",
                           (name, author))
            books.commit()
            # books.close()
        return render_template("books.html")
    else:
        return render_template('book_form.html')
    
# Endpoint for deleting a book record
@app.route("/del_book/<int:id>", methods=["GET"])
def del_book(id):
    #return f'Book id: {id}'
    try:
        connect = sqlite3.connect('numb.db')
        connect.execute('DELETE FROM BOOKS WHERE id = ?', (id,))
        connect.commit()
        connect.close()
        ##return f'Book id: {id}'
        #return render_template("books.html", data=data)
        return redirect(url_for('books'))
        ##return render_template('home.html', primary_bold_color=fire_weed, trim_color=sha_green)
        #return '', 204  # No Content, successful deletion
    except sqlite3.Error as e:
        return f"Database error: {e}", 500


@app.route('/info')
def info():
    # return f"Current route: {request.url_rule}"
    return f"Current endpoint: {request.url_rule.endpoint}"

if __name__ == '__main__':
    app.run(debug=True)