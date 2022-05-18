from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dataclasses import dataclass

# -----------> Flask App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/catalog'
CORS(app)  # For frontend

# -----------> Database Models
db = SQLAlchemy(app)

@dataclass
class Catalog(db.Model):
    id:          int
    name:        str
    description: str
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(100))
    description = db.Column(db.String(255))


@app.route('/catalog/list')
def catalog_list_view():
    return jsonify(Catalog.query.all())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')