SECRET_KEY = '12345abcdef'
FLASK_DEBUG = 1
# ENABLE THE PARAMETER BELOW IF YOU WANT TO RUN IT ON THE SQLLITE DB (development purposes) and disable the mysql database uri
#SQLALCHEMY_DATABASE_URI = 'sqlite:///data/test.db'
DATABASE_NAME= 'test'
# ENABLE THE PARAMETER BELOW IF YOU WANT TO RUN IT ON THE MYSQL DB  and disable the sqLite database uri
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@mysql/' + DATABASE_NAME
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO=True
SMTP_SERVER = 'localhost'
SMTP_PORT = 8025
SMTP_LOGIN_NAME = ''
SMTP_PASSWORD = ''
EMAIL_SEND_FROM = 'test@fairyfly.dev'
