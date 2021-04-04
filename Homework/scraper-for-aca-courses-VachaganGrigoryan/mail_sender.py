from smtplib import SMTP_SSL
from ssl import create_default_context
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from models import Course

default_context = create_default_context()


def send_email_for(new_data: dict, session):

    courses = session.query(
        Course.course_name,
        Course.course_url,
        Course.level
    ).filter(Course.course_id.in_(new_data.get('course', []))).all()

    pswd = getpass()
    with SMTP_SSL('smtp.gmail.com', context=default_context) as smtp_server:
        smtp_server.login('vachagan.grigoryan.it@gmail.com', pswd)

        course_text = "\n".join(f"{course_name}-{level}" for course_name, _, level in courses)
        text_content = f"""
        Hi, 
        Check out new Courses from ACA.am:
        {course_text}
        Have a nice day!
        """

        course_html_div_list = []
        for course_name, course_url, level in courses:
            html = f"""
            <div><a href="{course_url}">{course_name}</a> {level}</div>
            """
            course_html_div_list.append(html)
        course_html = '\n'.join(course_html_div_list)
        html_content = f"""
        <h2>Hi</h2>
        <p>Check out new Courses from ACA.am:</p>
        {course_html}
        <p>Have a nice day!</p>
        """

        message = MIMEMultipart('altrnative')
        message['Subject'] = 'Testing'
        message['To'] = 'vachagan.grigoryan.it@gmail.com'

        text = MIMEText(text_content, 'plane')
        html = MIMEText(html_content, 'html')

        message.attach(html)
        message.attach(text)

        smtp_server.sendmail('vachagan.grigoryan.it@gmail.com', 'vachagan.grigoryan.it@gmail.com',
                             msg=message.as_string())


