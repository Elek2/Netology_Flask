from datetime import datetime
import atexit
import os

from sqlalchemy import create_engine, Integer, String, \
    Column, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from dotenv import load_dotenv
from sqlalchemy_utils import database_exists, create_database


load_dotenv()

DNS = f"{os.getenv('DB_ENGINE')}://{os.getenv('DB_USER')}:" \
      f"{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:" \
      f"{os.getenv('DB_PORT')}/{os.getenv('DB_BASE')}"


engine = create_engine(DNS)
if not database_exists(engine.url):
    create_database(engine.url)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)  # Автоматическое удаление движка при завершении работы

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    advertisements = relationship('Advertisement', back_populates="users")


class Advertisement(Base):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True)
    header = Column(String(100), nullable=False)
    description = Column(String(100))
    created_on = Column(DateTime(), default=datetime.now)
    author_id = Column(ForeignKey('users.id'))
    users = relationship('User', back_populates="advertisements")


Base.metadata.create_all(engine)
