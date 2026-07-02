import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join(os.getcwd(), 'notebooks', 'data', 'train.csv')
    test_data_path: str = os.path.join(os.getcwd(), 'notebooks', 'data', 'test.csv')
    raw_data_path: str = os.path.join(os.getcwd(), 'notebooks', 'data', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            logging.info(f"Reading raw data from {self.ingestion_config.raw_data_path}")
            df = pd.read_csv(self.ingestion_config.raw_data_path, index_col=0)
            logging.info(f"Dataset shape: {df.shape}")
            
            logging.info("Data ingestion completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        
        except Exception as e:
            logging.error(f"Error in data ingestion: {str(e)}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path, raw_path = ingestion.initiate_data_ingestion()
    print(f"Train path: {train_path}")
    print(f"Test path: {test_path}")
    print(f"Raw path: {raw_path}")