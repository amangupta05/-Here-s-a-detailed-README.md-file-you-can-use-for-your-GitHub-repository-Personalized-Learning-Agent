from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import config

engine = create_engine(config.DB_URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define models
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    preferences = Column(JSON)

class LearningHistory(Base):
    __tablename__ = 'learning_history'
    record_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(TIMESTAMP)
    content = Column(String)

# Initialize tables
Base.metadata.create_all(engine)