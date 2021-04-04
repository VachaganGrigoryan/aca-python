from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

DB_NAME = 'aca.db'
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True)

Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    company = Column(String)
    courses = relationship("CourseTeacher", back_populates="teacher")

    def update(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"<Teacher(full_name='{self.full_name}', company='{self.company}')>"


class CourseTeacher(Base):
    __tablename__ = 'course_teacher'
    course_id = Column(Integer, ForeignKey('course.course_id'), primary_key=True)
    course = relationship("Course", back_populates="teachers")
    teacher_id = Column(Integer, ForeignKey('teacher.teacher_id'), primary_key=True)
    teacher = relationship("Teacher", back_populates="courses")

    def __repr__(self):
        return f"<CourseTeacher(course_id='{self.course_id}', teacher_id='{self.teacher_id}')>"


class Course(Base):
    __tablename__ = 'course'
    course_id = Column(String, primary_key=True)
    course_url = Column(String)
    course_name = Column(String)
    duration = Column(String)
    effort = Column(String)
    price = Column(String)
    level = Column(String)
    teachers = relationship('CourseTeacher', back_populates="course")

    def update(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"<Course(course_id='{self.course_id}', course_name='{self.course_name}')>"


metadata = Base.metadata


if __name__ == '__main__':
    metadata.create_all(engine)
