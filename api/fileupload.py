from flask import Blueprint, jsonify, request
import os
class uploadFile(object):
    FOLDER_UPLOAD_NAME = 'upload'
    ROOT_PATH = os.path.join(os.path.dirname(__file__),FOLDER_UPLOAD_NAME)
    EXTENSIONS ={'txt', 'csv','xls','xlsx','jpg','jpeg','mp4','mp3'}
    upload_bp = Blueprint('upload')

    @upload_bp.route('/', methods = ['POST','PUT'])
    def __init__():

        pass

    def uploadFile():
        client_path = request.form.get('file_path_name')

        pass
