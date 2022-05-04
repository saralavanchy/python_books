from typing import Optional

class InvalidEmailError(Exception):
    """"Custom error that is raised when the email is not valid."""

    def __int__(self, message: str, value: Optional[str]):
        self.value = value
        self.message = message
        super(message)

class InvalidId(Exception):
    def __int__(self, message: str):
        super(message)