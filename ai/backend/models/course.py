from flask_sqlalchemy import SQLAlchemy
from models.user import db
import json

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    instructor = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    difficulty = db.Column(db.String(50))
    estimated_hours = db.Column(db.Integer)
    total_lessons = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "instructor": self.instructor,
            "description": self.description,
            "category": self.category,
            "difficulty": self.difficulty,
            "estimated_hours": self.estimated_hours,
            "total_lessons": self.total_lessons
        }

class Lesson(db.Model):
    __tablename__ = 'lessons'
    
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(20))
    lesson_type = db.Column(db.String(50), default='video')
    order_index = db.Column(db.Integer, default=0)
    
    course = db.relationship('Course', backref=db.backref('lessons', lazy=True))
    
    def to_dict(self):
        return {
            "id": self.id,
            "course_id": self.course_id,
            "title": self.title,
            "duration": self.duration,
            "type": self.lesson_type,
            "order_index": self.order_index
        }

class Assignment(db.Model):
    __tablename__ = 'assignments'
    
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.String(20))
    status = db.Column(db.String(50), default='upcoming')  # upcoming, pending, completed
    grade = db.Column(db.String(10))
    
    course = db.relationship('Course', backref=db.backref('assignments', lazy=True))
    
    def to_dict(self):
        return {
            "id": self.id,
            "course_id": self.course_id,
            "title": self.title,
            "dueDate": self.due_date,
            "status": self.status,
            "grade": self.grade
        }

