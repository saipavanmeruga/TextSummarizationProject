import os
import wget
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        path = Path(self.config.local_data_dir)
        if not path.is_file():
            os.chdir(self.config.root_dir)
            filename = wget.download(self.config.source_URL)
            os.chdir("../../")
            logger.info(f"{filename} is downloaded!")            
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_dir))}")
  
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_dir, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        