class DataBaseException(Exception):
    status_code = 500
    default_detail = 'The Proxy returns an error'
    default_code = 'generic_error'


class UserNotAuthorize(Exception):
    status_code = 401
    default_detail = 'The user is not authorized'
    default_code = 'not_authorized'


class BadRequest(Exception):
    status_code = 400
    default_detail = 'The request could not be understood'
    default_code = 'bad_request'

    def _init_(self, code=None, extra_data=None):
        self.code = code
        self.extra_data = extra_data