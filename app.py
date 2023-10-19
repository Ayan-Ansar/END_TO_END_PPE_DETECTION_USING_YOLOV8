import sys, os
from ppeDetection.pipeline.training_pipeline import TrainPipeline
from ppeDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from ppeDetection.exception import AppException
from ppeDetection.constant.application import APP_HOST, APP_PORT
from ultralytics import YOLO
import shutil

app = Flask(__name__, template_folder='templates')
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputimage.jpg"
       
       
clapp = ClientApp() 

@app.route('/')
def home():
    return render_template('index.html') 


@app.route('/predict',  methods=["POST", "GET"])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clapp.filename)
        
        model = YOLO('yolov8/best.pt')
        
        img_path = 'data/inputimage.jpg'
        model.predict(img_path, save=True)
        
        opencodedbase64 = encodeImageIntoBase64('runs/detect/predict/inputimage.jpg')
        
        result = {'image': opencodedbase64.decode('utf-8')}
        
        shutil.rmtree('runs')
        return jsonify(result)
    
    except Exception as e:
        AppException(e,sys)


# if __name__ == '__main__':  
#     app.run(APP_HOST, APP_PORT)        
