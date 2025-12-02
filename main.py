from src.config.configuration import ConfigurationManager
from src.data_i.data_ingestion import DataIngestion

def main():
    config_manager = ConfigurationManager()
    data_ingestion_config = config_manager.get_data_ingestion_config()

    ingestion = DataIngestion(data_ingestion_config)
    ingestion.main()

if __name__ == "__main__":
    main()
