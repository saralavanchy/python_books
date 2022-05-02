from app.model.errors import InvalidEmailError

class Email:
    def __init__(self, prefix: str, domain: str):
        self.prefix = prefix
        self.domain = domain

    def address(self) -> str:
        #if(not self.prefix is None or not self.domain is None):
        #    raise InvalidEmailError("the prefix and domain are required")
        return f"{self.prefix}@{self.domain}"

