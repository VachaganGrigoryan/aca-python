import json

from aca_scraper import LookUpACACourses
from models import engine, Course, Teacher, CourseTeacher
from sqlalchemy.orm import sessionmaker, Session

from mail_sender import send_email_for

NEW_DATA = {}


def db_append_teachers(session: Session, teachers: list, course: Course):

    for teacher_data in teachers:
        _teacher = session.query(Teacher).filter(Teacher.full_name == teacher_data.get('full_name')).one_or_none()

        if not _teacher:
            _teacher = Teacher(**{
                'full_name': teacher_data.get('full_name'),
                'company': teacher_data.get('company')
            })
            NEW_DATA['teacher'] = NEW_DATA.get('teacher', []) + [_teacher.full_name]
        else:
            _teacher.full_name = teacher_data.get('full_name')
            _teacher.company = teacher_data.get('company')

        _course_teacher = session.query(CourseTeacher).filter(
            CourseTeacher.course_id == course.course_id and CourseTeacher.teacher_id == _teacher.teacher_id
        ).one_or_none()
        if not _course_teacher:
            course_teacher = CourseTeacher(**{
                'course': course,
                'teacher': _teacher
            })
            session.add(course_teacher)
        session.add(_teacher)


def db_append_courses(session: Session, courses: list):

    for course_data in courses:
        _course = session.query(Course).filter(Course.course_id == course_data.get('course_id')).one_or_none()

        if not _course:
            _course = Course(**{
                "course_id": course_data.get('course_id'),
                "course_url": course_data.get('course_url'),
                "course_name": course_data.get('course_name'),
                "duration": course_data.get('duration:'),
                "effort": course_data.get('effort:'),
                "price": course_data.get('price:'),
                "level": course_data.get('level:'),
            })

            NEW_DATA['course'] = NEW_DATA.get('course', []) + [_course.course_id]
        else:
            _course.course_url = course_data.get('course_url')
            _course.course_name = course_data.get('course_name')
            _course.duration = course_data.get('duration:')
            _course.effort = course_data.get('effort:')
            _course.price = course_data.get('price:')
            _course.level = course_data.get('level:')

        db_append_teachers(session, course_data.get('teachers', []), _course)
        session.add(_course)


def run():
    # with open('./data.json', 'r', encoding='utf-8') as json_file:
    #     data = json.loads(json_file.read(), )

    ACA_URL = 'https://aca.am/en/'
    look_up = LookUpACACourses(ACA_URL)
    # look_up.save_as_html('./html')
    data = look_up.get_data()

    session = sessionmaker(engine)()
    # session.query(Course).delete()
    # session.query(Teacher).delete()
    db_append_courses(session, data)
    session.commit()

    send_email_for(NEW_DATA, session)

if __name__ == '__main__':

    run()

