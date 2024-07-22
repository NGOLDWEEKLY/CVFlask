from flask import Blueprint, Response, request, jsonify, render_template, send_from_directory, current_app
from werkzeug.utils import secure_filename
from models.yolo_model import defect_detect
from config import Config
import os

# Configure upload folder and allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
api_blueprint = Blueprint('api', __name__)
live_sessions = []

if not os.path.exists(Config.UPLOAD_FOLDER):
    os.makedirs(Config.UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@api_blueprint.route('/')
def index():
    return render_template('index.html')

@api_blueprint.route('/defect/detector', methods=['POST'])
def defect_detect_wrapper():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(file_path)

        caption = defect_detect(file_path)
        return jsonify({"file_path": caption})

    return jsonify({"error": "Invalid file type"}), 400

@api_blueprint.route('/files/<path:name>', methods=['GET'])
def get_file(name): 
    return send_from_directory(Config.USER_FOLDER, name, as_attachment=False)

