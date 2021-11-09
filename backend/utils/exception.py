"""
    exception
"""


class ParamError(Exception):
    def __init__(self, key, message):
        self.key = key
        self.message = message
        self.error = {key: [message]}


class PermError(Exception):
    def __init__(self, message):
        self.message = message


class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message


class FormError(Exception):
    def __init__(self, errors):
        self.error = errors
