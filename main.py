from flask import Flask, jsonify, request, flash
from database import db
from routes.book import book_route
from errors.errors import InternalServerError

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

app.register_blueprint(book_route, url_prefix='/book')


@app.route('/_status', methods=['GET'])
def status():
    return 'OK', 200


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path))
    return 'Path Not Found', 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return InternalServerError.message, InternalServerError.status_code


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=8000)