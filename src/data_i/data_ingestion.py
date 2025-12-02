import os
from datasets import load_dataset
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.data_path = config.data_path
        self.dataset = config.dataset

        self.train_data = None
        self.test_data = None
        self.valid_data = None
        
    def load_data(self):
        loaded_df = load_dataset(self.dataset)
        return loaded_df

    
    def split_data(self, loaded_df):
        
        train_data = loaded_df.get('train', None)
        test_data = loaded_df.get('test', None)
        valid_data = loaded_df.get('validation', None)
        
        self.train_data = train_data
        self.test_data = test_data
        self.valid_data = valid_data

        return train_data, test_data, valid_data
    
    def save_data(self, train_data, test_data, valid_data):
        
        os.makedirs(self.data_path, exist_ok=True)
        
        train_data.save_to_disk(os.path.join(self.data_path, 'train'))
        test_data.save_to_disk(os.path.join(self.data_path, 'test'))

        valid_data.save_to_disk(os.path.join(self.data_path, 'validation'))
        
    def main(self):
        loaded_df = self.load_data()
        train_data, test_data, valid_data = self.split_data(loaded_df)
        self.save_data(train_data, test_data, valid_data)
        
        logger.info("Data ingestion pipeline completed")