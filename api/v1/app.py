#!/usr/bin/python3
"""Your first endpoint (route) will be to 
return the status of your API"""

from flask import Flask, make_reponse, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import views
import os

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r'/*': {'origins': '0.0.0.0'}})

@app.teardown_appcontext
def teardown(exception):
    """method for tearing down app"""
    if storage is not None:
        storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_HOST", "5000")
    app.run(host=host, port=port, threaded=True)
