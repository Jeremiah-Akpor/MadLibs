"""Contains all my custom exceptions for this project"""


class StoryException(Exception):
    """ an exception for invalid number"""
    def __init__(self, msg) -> None:
        super().__init__(msg)
