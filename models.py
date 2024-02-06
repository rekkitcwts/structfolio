from app import db
from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer,     nullable=False, unique=True, primary_key=True)
    date_created = Column(DateTime(timezone=True), default=func.now())
    date_updated = Column(DateTime(timezone=True), default=func.now())
    project_name = Column(String(150), nullable=False, unique=True)
    project_link = Column(String(300), nullable=True, unique=False)
    project_desc = Column(String(500), nullable=True, unique=False)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,     nullable=False, unique=True, primary_key=True)
    date_created = Column(DateTime(timezone=True), default=func.now())
    date_updated = Column(DateTime(timezone=True), default=func.now())
    username = Column(String(150), nullable=False, unique=True)
    passhash = Column(String(300), nullable=True, unique=False)
    
    def hash_password(self, password):
        self.passhash = pwd_context.encrypt(password)
    
    def verify_password(self, password):
        return pwd_context.verify(password, self.passhash)