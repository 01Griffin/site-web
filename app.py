from flask import Flask


from resources.methods import tasks_bp
from database import setup


app = Flask(__name__)


app.register_blueprint(tasks_bp)
setup.create_tables()


if __name__ == '__main__':
    app.run(debug=True)