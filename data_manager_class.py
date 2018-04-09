import csv
import shutil
import os
from datetime import datetime, date
import unicodedata
import smtplib
from tempfile import NamedTemporaryFile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.templates import get_tempalte, render_context


host = 'smtp.gmail.com'
port = 587
username = '***@gmail.com'
password = '***'
from_email = username
to_list = ["***"]

# file_item_path = os.path.join(os.getcwd(), 'data.csv')
file_item_path = os.path.join(os.path.dirname(__file__), 'data.csv')


class User_Manager():

    def render_message(self, user_data):
        file_ = 'templates/email_message.txt'
        file_html = 'templates/email_message.html'
        template = get_tempalte(file_)
        template_html = get_tempalte(file_html)
        if isinstance(user_data, dict):
            context = user_data
            plain_ = render_context(template, context)
            html_ = render_context(template_html, context)
            return plain_, html_
        return None

    def message_user(self, edit_id=None, email=None,
                     Subject='Billing update there!'):
        user = self.get_user_data(edit_id=edit_id, email=email)
        if user:
            plain_, html_ = self.render_message(user)
            user_email = user.get('email', 'anton.skovpen@gmail.com')
            to_list.append(user_email)
            try:
                smt_connect = smtplib.SMTP(host, port)
                smt_connect.ehlo()
                smt_connect.starttls()
                smt_connect.login(username, password)
                the_messege = MIMEMultipart('alternative')
                the_messege['Subject'] = Subject
                the_messege["From"] = from_email
                the_messege["To"] = user_email
                part_1 = MIMEText(plain_, 'plain')
                part_2 = MIMEText(html_, 'plain')
                the_messege.attach(part_1)
                the_messege.attach(part_2)
                smt_connect.sendmail(from_email, to_list,
                                     the_messege.as_string())
                smt_connect.quit()
            except smtplib.SMTPException:
                print("an error sending message")

    def get_user_data(self, edit_id=None, email=None):
        filename = file_item_path
        print(file_item_path)
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            wrong_id = None
            wrong_email = None
            for row in reader:
                if edit_id is not None:
                    if int(edit_id) == int(row.get('id')):
                        return row
                    else:
                        wrong_id = edit_id
                if email is not None:
                    if email == row.get('email'):
                        return row
                    else:
                        wrong_email = email
            if wrong_id is not None:
                print('Wrong user id{edit_id}'.format(edit_id=edit_id))
            if wrong_email is not None:
                print('Wrong user id{wrong_email}'.format(
                    wrong_email=wrong_email))
