import smtplib
import sys
import python_test_project


def send_message(email_address, message_body):
    with python_test_project.app.app_context():
        sent_from = python_test_project.app.config['SMTP_SERVER']
        try:
            server = smtplib.SMTP(python_test_project.app.config['SMTP_SERVER'], python_test_project.app.config['SMTP_PORT'])
            server.ehlo()
            if python_test_project.app.config['SMTP_SERVER'] != 'localhost':
                server.login(python_test_project.app.config['SMTP_LOGIN_NAME'], python_test_project.app.config['SMTP_PASSWORD'])
            server.sendmail(sent_from, email_address, message_body)
            server.close()
        except Exception as e:
            print(e, sys.stderr)