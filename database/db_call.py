from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB = 'sqlite:////tmp/test.db';

def start_session():
    engine = create_engine(DB)
    Session = sessionmaker(bind=engine)
    return Session()