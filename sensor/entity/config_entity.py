import os
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime 
 

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"


class TrainingPipelineConfig:


#Trainging pipeline config is to store each file we generate
#  and all the outputs of our model like model o/p,graph, metrics in a folder(artifact) 
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
class DataIngestionConfig:
    #We have to pass object of TrainingPipeLineConfig to every component in training pipeline
    # so that o/p folder for each component will be created in the object of the class TrainingPipelineConfig(self.artifact_dir)
    # i.e., path:arifact/time stamp/data_ingestion
    # Data ingestion o/p we have to generate here  
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name="aps"
        self.collection_name="sensor"
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion",FILE_NAME)
        #To store the dataframe that we created by loading data from Mongo DB,we have to create a path
        self.feature_store_dir=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
        #In Data Ingestion part,we have to devide our data set into train,test,evaluation parts
        self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
    def to_dict(self,)->dict:
    # To convert all the data into dictionary format
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)       

# "..." is for pass
class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...






