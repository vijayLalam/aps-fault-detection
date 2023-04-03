import os
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime 
 

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
TRANSFORMER_OBJECT_FILE_NAME = "transformer.pkl"
TARGET_ENCODER_OBJECT_FILE_NAME = "target_encoder.pkl"
MODEL_FILE_NAME = "model.pkl"


class TrainingPipelineConfig:


#Trainging pipeline config is to store each file we generate
#  and all the outputs of our model like model o/p,graph, metrics in a folder(artifact) 
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        print(self.artifact_dir)
class DataIngestionConfig:
    #We have to pass object of TrainingPipeLineConfig to every component in training pipeline
    # so that o/p folder for each component will be created in the object of the class TrainingPipelineConfig(self.artifact_dir)
    # i.e., path:arifact/time stamp/data_ingestion
    # Data ingestion o/p we have to generate here  
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name="aps"
        self.collection_name="sensor"
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
        #To store the dataframe that we created by loading data from Mongo DB,we have to create a path
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
        #In Data Ingestion part,we have to devide our data set into train,test,evaluation parts
        self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
        self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
        self.test_size=0.2
    def to_dict(self,)->dict:
    # To convert all the data into dictionary format
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)       

# "..." is for pass
class DataValidationConfig:
    #Here we are passing object of class:TrainingPipelineConfig-> training_pipeline_config as parameter/constructor to
    ##class:DataValidationConfig and we are using property of class:TrainingPipelineConfig ->training_pipeline_config.artifact_dir
    ###here in this class.
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
        self.report_file_path=os.path.join(self.data_validation_dir,"report.yaml")
        self.missing_threshold:float = 0.2
        self .base_file_path = os.path.join("aps_failure_training_set1.csv")
class DataTransformationConfig:
       #Here we are passing object of class:TrainingPipelineConfig-> training_pipeline_config as parameter/constructor to
    ##class:TransformationConfig and we are using property of class:TrainingPipelineConfig ->training_pipeline_config.artifact_dir
    ###here in this class.
    #This allows DataTransformationConfig to use the artifact_dir attribute of TrainingPipelineConfig to 
    ##construct file paths that are specific to the current training pipeline run
     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir,, "data_transformation")
        self.transform_object_path = os.path.join(self.data_transformation_dir,"transformer",TRANSFORMER_OBJECT_FILE_NAME)
        self.transformed_train_path =os.path.join(self.data_transformation_dir,"transformed",TRAIN_FILE_NAME)
        self.transformed_test_path =os.path.join(self.data_transformation_dir,"transformed",TEST_FILE_NAME)
        self.target_encoder_path    =os.path.join(self.data_transformation_dir,"target_encoder",TARGET_ENCODER_OBJECT_FILE_NAME)
class ModelTrainerConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir=os.path.join(training_pipeline_config.artifact_dir,"model_trainer")
        self.model_path = os.path.join(self.model_trainer_dir,"model",MODEL_FILE_NAME)
        self.expected_score = 0.7
        self.overfitting_threshold = 0.1

class ModelEvaluationConfig:...
class ModelPusherConfig:...






