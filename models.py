from app import db
from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer,     nullable=False, unique=True, primary_key=True)
    date_created = Column(DateTime(timezone=True), default=func.now())
    date_updated = Column(DateTime(timezone=True), default=func.now())
    project_name = Column(String(150), nullable=False, unique=True)
    project_link = Column(String(300), nullable=True, unique=False)
    project_desc = Column(String(500), nullable=True, unique=False)