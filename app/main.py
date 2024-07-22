from flask import Flask
import os
from config import Config
from api.routes import api_blueprint

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    if not os.path.exists(Config.UPLOAD_FOLDER):
        os.makedirs(Config.UPLOAD_FOLDER)
    app.run(host="0.0.0.0", port=5000, debug=True)
