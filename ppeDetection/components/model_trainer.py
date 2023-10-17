import os 
import sys 
import yaml 
import ppeDetection.utils.main_utils as read_yaml_file 
from ppeDetection.logger import logging 
from ppeDetection.exception import AppException 
from ppeDetection.entity.config_entity import ModelTrainerConfig
from ppeDetection.entity.artifacts_entity import ModelTrainerArtifact 
from ultralytics import YOLO
import zipfile, shutil


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig) -> None:
        try:
            self.model_trainer_config = model_trainer_config 
        
        except Exception as e: 
            raise AppException(e,sys)


    def initiate_model_trainer(self) -> str:
        logging.info("Initiated model training process")
        try:
            logging.info("Unzipping data.zip")
            
            with zipfile.ZipFile('data.zip', 'r') as z:
                z.extractall()
            
            os.remove('data.zip')
            
            """ 
            Code to read num classes from the yaml file as we are training for custom classes intialized in constants
                with open("data.yaml", 'r') as stream:
                    num_classes = str(yaml.safe_load(stream)['nc'])
            """   
            model_config_file_name = self.model_trainer_config.weight_name.split('.')[0]
            print(model_config_file_name)
            
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.makedirs('yolov8', exist_ok=True)
            
            model = YOLO(self.model_trainer_config.weight_name)
            
            # model.train(
            #     data="data.yaml",
            #     task=self.model_trainer_config.task,
            #     imgsz=self.model_trainer_config.img_size,
            #     epochs=self.model_trainer_config.no_epochs,
            #     mode=self.model_trainer_config.mode,
            #     name='trained',
            #     classes=self.model_trainer_config.class_list,
            # ) 
            
            shutil.copyfile('runs/detect/trained/weights/best.pt', 'yolov8/best.pt')
            shutil.copyfile('runs/detect/trained/weights/best.pt', self.model_trainer_config.model_trainer_dir + '/best.pt')
            
            shutil.rmtree('train')
            shutil.rmtree('valid')
            shutil.rmtree('test')
            os.remove('data.yaml')
            os.remove('README.dataset.txt')
            os.remove('README.roboflow.txt')
            os.remove('yolov8n.pt')
            shutil.rmtree('runs')
                
            
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov8/best.pt"
            )
            
            logging.info("Exited model training process")
            logging.info(f"Model trainer Artifact: {model_trainer_artifact}")
            
            return model_trainer_artifact 
        except Exception as e:
            raise AppException(e, sys)
            
            
             
                
         
                
    