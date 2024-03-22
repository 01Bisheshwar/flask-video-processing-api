# Imports
from flask import Flask, request
from flask_cors import CORS
from modules.setup_module import setup
from modules.processing_module import process
import os

# For now it creates the folder
setup()

# Flask Instantiation
app = Flask(__name__)
CORS(app)

# Routes
@app.route("/", methods=['GET'])
def index():
    return {"status": True, "message": "API is working"}

@app.route("/process", methods=['GET', 'POST'])
def processController():
    if request.method == "GET":
        print("Process GET Request")
        return {"status": True, "message": "Process GET Request"}
    elif request.method == "POST":
        print("Process POST Request")
        print(request.files)
        video = request.files['video']
        video.save(os.path.join("static/videos", video.filename))
        process(video.filename)
        return {"status": True, "message": "Process POST Request"}

if __name__ == "__main__":
    app.run(debug=True)