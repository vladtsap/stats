from sqlalchemy import Column, Integer, String

from database.base import Base


class Post(Base):
    __tablename__ = 'post'  # noqa: typo

    id = Column(Integer, primary_key=True, unique=True, )
    path = Column(String, index=True, )
    ip_address = Column(String, index=True, )
    views = Column(Integer, default=1, )
