import os.path
import sys
import yaml
import base64

from ppeDetection.logger import logging
from ppeDetection.exception import AppException


def read_yaml_file(filepath: str):
    try:
        with open(filepath, 'rb') as yaml_file:
            logging.info("Read YAML file successfully") 
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise AppException(e, sys)    
    

def decodeImage(imgstring, filename):
    imgData = base64.b64decode(imgstring)
    with open("./data/" + filename, 'wb') as f:
        f.write(imgData)
        f.close()


def encodeImageIntoBase64(coppedImagePath):
    with open(coppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())