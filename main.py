from sensor.logger import logging
from sensor.exception import SensorException
import sys,os
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity
from sensor.components import data_ingestion
#from sensor.entity.config_entity import DataIngestionConfig
if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = data_ingestion.DataIngestion(data_ingestion_config=data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())

          #get_collection_as_dataframe(database_name='aps',collection_name='sensor')
          #logging.info('get_collection_as_dataframe function in sensor.utils.py called from main.py and  execution completed successfully')
     except Exception as e:
          print(e)
          #raise SensorException(e,sys)
          










