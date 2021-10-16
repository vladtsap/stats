from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from config import engine

Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'  # noqa: typo

    id = Column(Integer, primary_key=True, unique=True, )
    path = Column(String, index=True, )
    ip_address = Column(String, index=True, )
    views = Column(Integer, default=1, )


Base.metadata.create_all(bind=engine)
