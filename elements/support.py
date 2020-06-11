""" Support information """

class Support():
    def __init__(self, first, last, email, signature, useFirst=True):
        self.first=first
        self.last=last
        self.email=email
        self.signature=signature
        self.useFirst=useFirst

    def useFirstName(self, _condition: bool):
        self.useFirst=_condition