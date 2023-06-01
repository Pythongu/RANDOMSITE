from flask import Flask
from views import views
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

run_with_ngrok(app)

app.register_blueprint(views, urlprefix="/")
if __name__ == '__main__':
    app.run()