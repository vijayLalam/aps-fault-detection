import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os,sys
import yaml

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        print(mongo_client[database_name][collection_name].find())
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        print(df)
        print(df.shape)
        print(df.sample(5))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)
def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
            #yaml is file with more readable format compared to json
            ##Here we are not using any database to save the validation report.
            ###Instead of DB we are using YAML file to check which validation passed/failed 
            ####We vcan use MONGO DB also instead of YAML
    except Exception as e:
        raise SensorException(error_message, error_detail)        