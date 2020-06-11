""" User information """

from database.generator import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////tmp/test.db')
Session = sessionmaker(bind=engine)
session = Session()

class EndUser():
    def __init__(self, first, last, email, signature, location):
        session.add(User(first=first, last=last, email=email, signature=signature))
        self.last=last
        # self.phone=phone
        # self.address=address
        # self.office=office

    def updateName(self, first, last):
        self.first=first
        self.last=last

    def updatePhone(self, phone):
        self.phone=phone

    def updateAddress(self, address):
        self.address=address

    def updateOffice(self, office):
        self.office=office