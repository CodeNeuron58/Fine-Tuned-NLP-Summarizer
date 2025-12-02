import yaml
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    dataset: str
    data_path: str

class ConfigurationManager:
    def __init__(self, config_filepath="config/config.yaml"):
        with open(config_filepath) as f:
            self.config = yaml.safe_load(f)

    def get_data_ingestion_config(self):
        cfg = self.config["data_ingestion"]
        
        return DataIngestionConfig(
            dataset=cfg["dataset"],
            data_path=cfg["data_path"]
        )

    # def get_data_preprocessing_config(self):
    #     cfg = self.config["data_preprocessing"]
    #     return DataIngestionConfig(
    #         dataset=cfg["dataset"],
    #         data_path=cfg["data_path"]
    #     )