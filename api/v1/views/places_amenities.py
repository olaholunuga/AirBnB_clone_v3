#!/usr/bin/python3
"""place amenities api"""

from crypt import methods
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models import storage_t

if storage_t == "db":
    from models.engine.db_storage import classes
else:
    from models.engine.file_storage import classes

@app_views.route("/places/<place_id>/amenities")
@app_views.route("/places/<place_id>/amenities/<amenity_id>", methods=["POST", "DELETE"])
def place_amenities_view(place_id=None, amenity_id=None):
    if place_id:
        place_obj = storage.get(classes["Place"], place_id)
        if not place_obj:
            abort(404)

        if not amenity_id:
            amenities_list = []
            if storage_t == "db":
                for amenity in place_obj.amenities:
                    amenity_dict = amenity.to_dict()
                    amenities_list.append(amenity_dict)

                return jsonify(amenities_list)
            else:
                for place_amenity_id in place_obj.amenity_ids:
                    amenity_obj = storage.get(classes["Amenity"], place_amenity_id)
                    amenity_dict = amenity_obj.to_dict()
                    amenities_list.append(amenity_dict)

                return jsonify(amenities_list)
        else:
            amenity_obj = storage.get(classes["Amenity"], amenity_id)
            if not amenity_obj:
                abort(404)
            if request.method == "DELETE":

                if storage_t == "db":
                    if amenity_obj not in place_obj.amenities:
                        abort(404)

                    place_obj.amenities.pop(amenity_obj)
                else:
                    if amenity_id not in place_obj.amenity_ids:
                        abort(404)

                    place_obj.amenity_ids.pop(amenity_id)
            else:
                if storage_t == "db":
                    if amenity_obj in place_obj.amenities:
                        return jsonify(amenity_obj.to_dict()), 200
                    else:
                        place_obj.amenities.append(amenity_obj)
                else:
                    if amenity_id in place_obj.amenity_ids:
                        return jsonify(amenity_obj.to_dict()), 200
                    else:
                        place_obj.amenity_ids.append(amenity_id)