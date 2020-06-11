from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:////tmp/test.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first = Column(String)
    last = Column(String)
    email = Column(String)
    signature = Column(String)

    def __repr__(self):
        return "<User(first='%s', last='%s', email='%s', signature='%s')>" % \
               (self.first, self.last, self.email, self.signature)

Base.metadata.create_all(engine)

def main():
    return

if __name__ == "__main__":
    main()


