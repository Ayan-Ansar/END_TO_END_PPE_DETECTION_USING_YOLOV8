import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

projectName = 'ppeDetection'

list_of_files = [
    ".gitignore",
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{projectName}/__init__.py",
    f"{projectName}/components/__init__.py",
    f"{projectName}/components/data_ingestion.py",
    f"{projectName}/components/model_trainer.py",
    f"{projectName}/constant/__init__.py",
    f"{projectName}/constant/training_pipeline/__init__.py",
    f"{projectName}/constant/application.py",
    f"{projectName}/entity/config_entity.py",
    f"{projectName}/entity/artifacts_entity.py",
    f"{projectName}/exception/__init__.py",
    f"{projectName}/logger/__init__.py",
    f"{projectName}/pipeline/__init__.py",
    f"{projectName}/pipeline/__init__.py",
    f"{projectName}/pipeline/training_pipeline.py",
    f"{projectName}/utils/__init__.py",
    f"{projectName}/utils/main_utils.py",
    "research/.gitkeep"
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath) # to convert it to windows path 
    
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True) # create folder if it does not exist 
        logging.info(f"Creating directory: {filedir} for the {filename}")
        
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0): 
        with open(filepath, "w") as f:
            pass 
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} already exists in {filedir}")
    
        