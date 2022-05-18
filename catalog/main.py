from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# -----------> Flask App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/catalog'
CORS(app)  # For frontend

# -----------> Database Models
db = SQLAlchemy(app)

class Catalog(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(100))
    description = db.Column(db.String(255))


@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')