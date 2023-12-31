from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<database_name>"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker()

Base = declarative_base()
