#!/usr/bin/python3
"""return app status"""

from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route("/status")
def status():
    """return app status in JSON object"""
    return jsonify({"status": "OK"})
