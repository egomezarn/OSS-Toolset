""" User information """

class User():
    def __init__(self, first, last, phone=None, address=None, office=None):
        self.first=first
        self.last=last
        self.phone=phone
        self.address=address
        self.office=office

    def updateName(self, first, last):
        self.first=first
        self.last=last

    def updatePhone(self, phone):
        self.phone=phone

    def updateAddress(self, address):
        self.address=address

    def updateOffice(self, office):
        self.office=office