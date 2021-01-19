from flask import jsonify, request, Blueprint
from repository.book import BookRepository
from errors.errors import ApplicationError, InternalServerError, BadRequestError
from utils.respond import make_err_response, make_response
book_route = Blueprint('book', __name__)


@book_route.route('/create', methods=['POST'])
def create_book():
    try:
        if not "book_name" in request.form or not "author_name" in request.form:
            return make_err_response(BadRequestError)

        book_name = request.form['book_name']
        author_name = request.form['author_name']

        if book_name == '' or author_name == '':
            return make_err_response(BadRequestError)

        new_book = BookRepository.create_book(book_name, author_name)
        return make_response(new_book, 'book created successfully')
    except Exception as err:
        print("err here", err)
        return make_err_response(InternalServerError)


@book_route.route('/', methods=['GET'])
def get_all_books():
    try:
        books = BookRepository.get_all_book()
        return make_response(books, 'books fetched successfully')
    except Exception as err:
        return make_err_response(InternalServerError)


@book_route.route('/update', methods=['PUT'])
def update():
    try:

        if not "book_name" in request.form or not "author_name" in request.form or not "id" in request.form:
            return make_err_response(BadRequestError)

        id = request.form['id']
        book_name = request.form['book_name']
        author_name = request.form['author_name']

        if id == '' or author_name == '' or book_name == '':
            return make_err_response(BadRequestError)

        updated_book = BookRepository.update_book(id, book_name, author_name)
        return make_response(updated_book, 'book updated successfully')
    except ApplicationError as err:
        return make_err_response(err)
    except Exception as err:
        return make_err_response(InternalServerError)


@book_route.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    try:
        deleted_book = BookRepository.delete_book(id)
        return make_response(deleted_book, 'book deleted successfully')
    except ApplicationError as err:
        return make_err_response(err)
    except Exception as err:
        return make_err_response(InternalServerError)
