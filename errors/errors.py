class ApplicationError(Exception):
    def __init__(self, message='', status_code=0):
        if message != '':
            self.message = message
        if status_code != 0:
            self.status_code = status_code


class NotFoundError(ApplicationError):
    message = 'Data not found'
    status_code = 400


class BadRequestError(ApplicationError):
    message = 'Bad Request Error'
    status_code = 400


class InternalServerError(ApplicationError):
    message = 'Internal Server Error'
    status_code = 500
