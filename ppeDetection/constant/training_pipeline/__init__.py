ARTIFICATS_DIR: str = "artifacts" 

"""
    Data Ingestion related constant start with DATA_INGESTION VAR NAME 
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion" 

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "'https://drive.google.com/file/d/1xkn87SRvjp9J7CVpp0y36vTOzRhRz_SE/view?usp=drive_link'"

"""
    Data Validation Related constant start with DATA_VALIDATION VAR NAME 
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = "staturs.txt" 

DATA_VALIDATION_ALL_REQUIRED_FILES = ['train','valid','data.yaml']


"""
    Model Trainer related constant start with MODEL_TRAINER VAR NAME 
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = 'yolov8n.pt'

MODEL_TRAINER_IMAGE_SIZE: int = 640 

MODEL_TRAINER_TASK: str = 'detect'

MODEL_TRAINER_MODE: str = 'train'

MODEL_TRAINER_NO_EPOCHS: int = 1 

MODEL_TRAINER_BATCH_SIZE: int = 16 

TRAINING_CLASSES = [0,5,7]

