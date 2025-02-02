from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    lessons = relationship("Lesson", back_populates="course")
    created_at = Column(DateTime, default=datetime.utcnow)

class Lesson(Base):
    __tablename__ = 'lessons'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    access_code = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("Course", back_populates="lessons")
    created_at = Column(DateTime, default=datetime.utcnow)
    questions = relationship("Question", back_populates="lesson")

class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    text = Column(String, nullable=False)
    lesson = relationship("Lesson", back_populates="questions")
    options = relationship("QuestionOption", back_populates="question")

class QuestionOption(Base):
    __tablename__ = 'question_options'
    
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)
    question = relationship("Question", back_populates="options")

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserProgress(Base):
    __tablename__ = 'user_progress'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    completed_at = Column(DateTime, default=datetime.utcnow)
    test_score = Column(Integer)  # Результат теста в процентах

def init_db():
    engine = create_engine('sqlite:///education_bot.db', connect_args={'check_same_thread': False})
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()