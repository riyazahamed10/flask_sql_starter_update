from database import db


class Book(db.Model):
    __tablename__ = 'book_details'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(30), nullable=False)
    author_name = db.Column(db.String(30), nullable=False)

    def __init__(self, book_name, author_name):
        self.book_name = book_name
        self.author_name = author_name

    @staticmethod
    def serialize(id, book_name, author_name):
        return {"id": id,
                "book_name": book_name.strip(),
                "author_name": author_name.strip()}
