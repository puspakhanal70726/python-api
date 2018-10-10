from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'apidb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def home():
    return redirect(url_for('index'))

# route used for getting all the books within the table to creating a new entry to the table
@app.route('/books')
def index():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    return render_template('booksPage.html', books=books)

# route is used to get a book by its id from the table
@app.route('/books/<int:book_id>')
def show(book_id):
    cursor.execute('SELECT * FROM books WHERE id = %d' % book_id)
    book = cursor.fetchone()
    return render_template('bookShow.html', book=book)

# route is used to delete a row in the table based on the give id
@app.route('/delete/<int:book_id>')
def delete(book_id):
    cursor.execute('DELETE FROM books WHERE id = %d' % book_id)
    conn.commit()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    return render_template('booksPage.html', books=books)

# route is used to update a row within the table
@app.route('/update/<int:book_id>', methods=('GET', 'POST'))
def update(book_id):
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        year = request.form['year']
        cursor.execute("UPDATE books SET name = '{}', year = '{}', author='{}' WHERE id = '{}'".format(name, int(year), author, book_id))
        conn.commit()
        return redirect(url_for('index'))
    cursor.execute('SELECT * FROM books WHERE id = %d' % book_id)
    book = cursor.fetchone()
    return render_template('bookEdit.html', book=book)

# route is used to create a new entry into the table
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        year = request.form['year']
        cursor.execute("INSERT INTO books (name, year, author) VALUES ('{}','{}','{}')".format(name, int(year), author))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('bookForm.html')
