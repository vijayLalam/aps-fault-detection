from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
import pandas as pd
import numpy as numpy
from sklearn.model_selection import train_test_split

class DataIngestion:
    
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)
    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            #exporting collection data as pandas dataframe
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name,
                collection_name=self.data_ingestion_config.collection_name)
        logging.info("Save data in feature store")
        #replace na with Nan
        df.replace(to_replace="na",np.NAN,inplace=True)
        #save data in feature store
        #Create feature store folder if not vailable
        feature_store_dir=os.path.dirname(self.data_ingestion_config.feature_store_file_path)
        os.makedirs(feature_store_dir,exist_ok=True)
        logging.info("Save df to feature store folder")
        #Save df to feature store folder
        df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)

        
        except Exception as e:
            raise SensorException(error_message=e,error_detail=sys)

    