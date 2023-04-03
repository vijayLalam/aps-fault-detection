import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os,sys
import yaml
import dill

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
        #print(df.shape)
        #print(df.sample(5))
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

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:

        for column in df.columns:
            if column not in exclude_columns:
                df[column]=df[column].astype('float')
        return df
    except Exception as e:
        raise e

def save_object(file_path: str, obj: object) -> None:
    #We will pass file path and object to this function
    try:
        logging.info("Entered the save_object method of utils")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        #dill library is used to save object into a file as binary format(serialization)It is an alternate to pickle(pkl)
        #loading binary format into object is known as de serialization
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise SensorException(e, sys) from e

def load_object(file_path: str, ) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise SensorException(e, sys) from e

#Python is an object-oriented programming language. 
# Everything is in Python treated as an object,
#  including variable, function, list, tuple, dictionary, set, etc.
#  Every object belongs to its class.

