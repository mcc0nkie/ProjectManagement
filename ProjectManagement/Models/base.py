from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

base = declarative_base()

class Base(base):
    __table_args__ = {'extend_existing': True}
    __abstract__ = True


