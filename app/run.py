from python_test_project import app
from model import db
import ssl
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ctx.load_cert_chain('static/cert/certificate.crt', 'static/cert/private.key')
db.init_app(app)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', ssl_context=ctx)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

