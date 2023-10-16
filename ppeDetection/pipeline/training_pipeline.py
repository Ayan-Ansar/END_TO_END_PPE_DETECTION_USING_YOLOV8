import sys, os 
from ppeDetection.logger import logging 
from ppeDetection.exception import AppException 
from ppeDetection.components.data_ingestion import DataIngestion

from ppeDetection.entity.config_entity import (DataIngestionConfig)
from ppeDetection.entity.artifacts_entity import (DataIngestionArtifact) 


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig() 
        
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from the url") 
            
            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config 
            )
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from url")
            logging.info(
                "Exited the start_data_ingestion method of the TrainPipeline class"
            )
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise AppException(e, sys) 
        
    def run_pipeline(self)-> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion() 
        
        except Exception as e:
            raise AppException(e, sys)