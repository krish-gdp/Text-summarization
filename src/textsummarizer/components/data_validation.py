import os
import urllib.request as request
import zipfile
from textsummarizer.logging import logger

from pathlib import Path
from src.textsummarizer.constants import *
from src.textsummarizer.utils.common import read_yaml,create_directories
from src.textsummarizer.entity import (DataValidationConfig)

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self)->bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file in all_files:
                    if file not in self.config.all_required_files:
                        validation_status =False
                        with open(self.config.status_file,'w') as f:
                            f.write(f"validation status: {validation_status}")
                        logger.info(f"data validation stage completed for file {file}: False")
                    else:
                        validation_status = True
                        with open(self.config.status_file,'w') as f:
                            f.write(f"validation status: {validation_status}")

                        logger.info(f"data validation stage completed for file {file}: True")

            return validation_status
        except Exception as e:
            raise e
    


   