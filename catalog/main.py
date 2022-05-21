from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dataclasses import dataclass
import redis
import json

# -----------> Flask App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/catalog'
CORS(app)  # For frontend

# -----------> Redis
redis_obj = redis.Redis(host='cache', port=6379, db=0)

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
    response = dict()
    response['status'] = 1  # There is no control now
    response['data'] = dict()
    redis_obj.delete('catalog_list')
    if redis_obj.get('catalog_list') is None:
        # TODO: Find right solution for 'json.dumps(json.loads(jsonify(Catalog.query.all()).data)))'
        redis_obj.set('catalog_list', json.dumps(json.loads(jsonify(Catalog.query.all()).data)))
    response['data'] = json.loads(redis_obj.get('catalog_list'))
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')