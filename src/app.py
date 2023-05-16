"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


# create the jackson family object
jackson_family = FamilyStructure("Jackson")



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_get_all_members():
    members = jackson_family.get_all_members()
    response = jackson_family.get_all_members()
    return response


@app.route('/member/<int:member_id>')
def handle_get_single_member(member_id):
    response = jackson_family.get_member(member_id)
    return response



@app.route('/members', methods=["POST"])
def handle_new_member():
    member_data = request.json
    response = jackson_family.add_member(member_data)
    return response


@app.route('/member/<int:member_id>', methods=["DELETE"])
def handle_delete_member(member_id):
    response = jackson_family.delete_member(member_id)
    return response


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
