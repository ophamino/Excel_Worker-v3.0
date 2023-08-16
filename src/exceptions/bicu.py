import logging

class FileStatementNotFound(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            logging.INFO(self.message)
        else:
            self.message = None
