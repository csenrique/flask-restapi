from flask import Flask
from database import setup
from resources.end_points import tasks_bp

app = Flask(__name__)
setup.create_tables()

app.register_blueprint(tasks_bp)

#Run
if __name__ == '__main__':
    app.run(debug=True, port= 3000)

