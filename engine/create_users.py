import sys
sys.path.append("/Users/divergencia/Documents/Programming/OSS_SOS2/OSS_SOS")
from database.generator import User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_call import start_session
import click

@click.command()
@click.option('-f', '--first', help="First name", type=str)
@click.option('-l', '--last', help="Last name", type=str)
@click.option('-e', '--email', help="Email address", type=str)
@click.option('-s', '--sign', help="Email signature", type=str)
def create_user(first, last, email, sign):
    session = start_session()
    session.add(User(first=first, last=last,
                     email=email, signature=sign))
    session.commit()



if __name__ == "__main__":
    create_user()