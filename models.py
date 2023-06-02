import atexit
import os
from datetime import datetime
from flask_login import UserMixin
from dotenv import load_dotenv
from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database

load_dotenv()

DNS = f"{os.getenv('DB_ENGINE')}://{os.getenv('DB_USER')}:" \
      f"{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:" \
      f"{os.getenv('DB_PORT')}/{os.getenv('DB_BASE')}"


engine = create_engine(DNS)
# drop_database(engine.url)
if not database_exists(engine.url):
    create_database(engine.url)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)  # Автоматическое удаление движка при завершении работы


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    advertisements = relationship('Advertisement', back_populates="users")


class Advertisement(Base):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True)
    header = Column(String(100), nullable=False)
    description = Column(String(100))
    created_on = Column(DateTime(), default=datetime.now)
    author_id = Column(ForeignKey('users.id'), nullable=False)
    users = relationship('User', back_populates="advertisements")


Base.metadata.create_all(engine)
