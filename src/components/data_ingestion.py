import sys
import os
from src.exception import CustomException  # Custom exception handling class
from src.logger import logging  # Custom logging module
import pandas as pd  # Pandas for data handling

from sklearn.model_selection import train_test_split  # Function to split dataset into training and testing sets
from dataclasses import dataclass  # Decorator to automatically generate init and repr methods

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig



@dataclass
class DataIngestionConfig:  # Config class to define paths for saving datasets
    train_data_path: str = os.path.join('artifact', "train.csv")  # Path for train data
    test_data_path: str = os.path.join('artifact', "test.csv")  # Path for test data
    raw_data_path: str = os.path.join('artifact', "raw_data.csv")  # Path for raw data

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # Instantiate config with paths

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")  # Log start of the ingestion process
        try:
            df = pd.read_csv(r'notebook\data\stud.csv')  # Load CSV file into a DataFrame
            logging.info('Dataset loaded into a DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  # Create directories if they don't exist
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)  # Save the raw dataset

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)  # Split dataset into train and test sets

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)  # Save training set to CSV
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)  # Save test set to CSV

            logging.info("Data ingestion process completed")

            return (
                self.ingestion_config.train_data_path,  # Return the path of the train dataset
                self.ingestion_config.test_data_path  # Return the path of the test dataset
            )

        except Exception as e:
            raise CustomException(e, sys)  # Raise a custom exception if any error occurs

if __name__ == "__main__":
    obj = DataIngestion()  # Create an instance of DataIngestion class
    train_data,test_data=obj.initiate_data_ingestion()  # Call the ingestion process

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
