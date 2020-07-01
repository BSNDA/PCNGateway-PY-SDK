"""
    exceptions.py
    ~~~~~~~~~~

"""


class BsnException(Exception):
    def __init__(self, code, message):
        self.__code = code
        self.__message = message

    def to_unicode(self):
        return "BsnException: code:{}, message:{}".format(self.__code, self.__message)

    def __str__(self):
        return self.to_unicode()

    def __repr__(self):
        return self.to_unicode()


class BsnValidationError(Exception):
    pass
