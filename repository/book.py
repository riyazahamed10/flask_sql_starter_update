from models.book import Book
from database import db
from errors.errors import NotFoundError


class BookRepository():

    @staticmethod
    def create_book(book_name, author_name):
        new_book = Book(book_name, author_name)
        db.session.add(new_book)
        db.session.commit()
        return Book.serialize(new_book.id, new_book.book_name, new_book.author_name)

    @staticmethod
    def get_all_book():
        books = Book.query.all()
        res = []
        for book in books:
            res.append(Book.serialize(
                book.id, book.book_name, book.author_name))
        return res

    @staticmethod
    def update_book(id, book_name='', author_name=''):
        book = Book.query.get(id)
        if book == None:
            raise NotFoundError('book id not found')
        if book_name != '':
            book.book_name = book_name
        if author_name != '':
            book.author_name = author_name
        db.session.commit()
        return Book.serialize(book.id, book.book_name, book.author_name)

    @staticmethod
    def delete_book(id):
        book = Book.query.get(id)
        if book == None:
            raise NotFoundError('book id not found')
        db.session.delete(book)
        db.session.commit()
        return Book.serialize(book.id, book.book_name, book.author_name)
