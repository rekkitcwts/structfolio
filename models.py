from app import db
from sqlalchemy import func, select

class Project(db.Model):
    __tablename__ = "projects"
    
    id = db.Column(db.Integer,     nullable=False, unique=True, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    date_updated = db.Column(db.DateTime(timezone=True), default=func.now())
    project_name = db.Column(db.String(150), nullable=False, unique=True)
    project_link = db.Column(db.String(300), nullable=True, unique=False)