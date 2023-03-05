## Kyle Shumate
#  SDEV 220
## Module 4 Lab - Case Study Python APIs
#
## Description:  CRUD API for Book model containing an ID, book name, author and publisher.




#class Drink(db.Model):
#    id - db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(80), unique=True, nullable=False)
#    description = db.Column(db.String(120))
#    drink = "Jameson"
#    def __repr__(self):
#        return f"{self.name} - {self.description}"
    
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return 'Hello!'

#@app.route('/drinks')
#def get_drinks():

#    return {"drinks", "drink data"}

# import modules




from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# create Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Book {self.book_name}>"

# create a new book
@app.route('/books', methods=['POST'])
def create_book():
    book_name = request.json['book_name']
    author = request.json['author']
    publisher = request.json['publisher']
    book = Book(book_name=book_name, author=author, publisher=publisher)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully', 'book_id': book.id}), 201

# get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher} for book in books]), 200

# get a single book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}), 200

# update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    book.book_name = request.json.get('book_name', book.book_name)
    book.author = request.json.get('author', book.author)
    book.publisher = request.json.get('publisher', book.publisher)
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'}), 200

# delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)