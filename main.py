# pip install python-dotenv
# pip install flask
# pip freeze > requirements.txt
# $env:FLASK_APP = "main"

# BUILDING DOCKER IMAGE
# docker build -t flask_api_ex .

# RUNNING DOCKER
# docker run -p 5000:5000 flask_api_ex

# RUNNING DOCKER IN THE BACKGROUND
# docker run -dp 5000:5000 flask_api_ex

# DOCKER CONTAINER
# docker run -dp 5000:5000 -w /app -v "/c/Users/mahmo/PycharmProjects/flask_smorest_api_ex:/app" flask_api_ex

import uuid
from flask import Flask, request, redirect
from flask_smorest import abort, Api
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from db import db
import models
import os
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.docs import blp as DocsBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(DocsBlueprint)

    return app

# @app.get('/stores')
# def get_stores():
#     return {"stores": list(stores.values())}


# @app.get('/items')
# def get_items():
#     return {"items": list(items.values())}


# @app.post("/stores")
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201


# @app.post('/item')
# def create_item():
#     item_data = request.get_json()
#     if item_data["store_id"] not in stores:
#         abort(404, message="Store not found!")
#         # return {"message": "Store not found!"}, 404
#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item
#     return item, 201


# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     if stores.get(store_id) is not None:
#         return stores[store_id]
#     abort(404, message="Store not found!")
#     # return {"message": "Store not found!"}, 404


# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     if items.get(item_id) is not None:
#         return items[item_id]
#     abort(404, message="Item not found!")
#     # return {"message": "Item not found!"}, 404


# @app.delete('/item/<string:item_id>')
# def delete_item(item_id):
#     if items.get(item_id) is not None:
#         del items[item_id]
#         return {"message": "Item Deleted!"}
#     abort(404, message="Item not found!")


# @app.delete('/store/<string:store_id>')
# def delete_store(store_id):
#     if stores.get(store_id) is not None:
#         del stores[store_id]
#         return {"message": "Store Deleted!"}
#     abort(404, message="Store not found!")


# @app.put('/item/<string:item_id>')
# def update_item(item_id):
#     item_data = request.get_json()
#     if items.get(item_id) is not None:
#         item = items[item_id]
#         item |= item_data
#         return {"message": "Item Updated!"}
#     abort(404, message="Item not found!")


# @app.get('/')
# def main():
#     return redirect("/swagger-ui", code=302)
