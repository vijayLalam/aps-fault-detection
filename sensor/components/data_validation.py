from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from typing import Optional
from sensor.logger import logging
from scipy.stats import ks_2samp
import os,sys
from sensor import utils
import numpy as np
class DataValidation:
    def __init__(self,
                    data_validation_config:config_entity.DataValidationConfig,
                    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data validation {'<<'*20}")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            self.validation_error=dict()
        except Exception as e:
            raise SensorException(e, sys)

    
    
    def drop_missing_values_columns(self,df:pd.Dataframe,report_key_name:str)->Option[pd.DataFrame]:
        """
        This fn will check every col.if any col containing more than
        30% missing values,it will drop that col.
        
        df:Accepts a pandas dataframe
        threshold:percentage criterion to drop a column
        ======================================================
        returns Pandas DataFrame if atleast single column is availableafter missing columns drop else None
        """
        try:
            
            threshold = self.data_validation_config.missing_threshold
            null_report=df.isna().sum()/df.shape[0]
            #selecting column names which contains null values
            logging.info(f"selecting column name which contains null above to {threshold}")
            drop_column_names = null_report[null_report>.3].index
            logging.info(f"columns to drop:{drop_column_names}")
            self.validation_error[report_key_name]=drop_column_names
            df.drop(list(drop_column_names),axis=1,inplace=True)
            
            #return None,if no column left
            if len(df.columns)==0:
                return None
            return df
        except Exception as e:
            raise SensorException(error_message, error_detail)

    def is_required_columns_exists(self,base_df:pd.DataFrame,current_df:pd.DataFrame,report_key_name:str)->bool:
        try:
            base_columns = base_df.columns
            current_columns = current_df.columns
            missing_columns = []
            for base_column in base_columns:
                if base_column not in current_columns:
                    logging.info(f"Column:[{base} is not available]")                   
                    missing_columns.append(base_column)
            if len(missing_columns) > 0:
                self.validation_error[report_key_name]=missing_columns
                return False
            return True
            
        except Exception as e:
            raise exception(e,sys)

    def data_drift(self,base_df:pd.DataFrame,current_df:pd.DataFrame,,report_key_name):
        try:
            drift_report = dict()
            base_columns = base_df.columns
            current_columns = current_df.columns
            for base_column in base_columns:
                base_data,current_data = base_df[base_column],current_df[base_column]
                #Null hypothesis is that both column data drawn from same distribution
                same_distribution = ks_2samp(base_data,current_data)
                
                if same_distribution.pvalue > 0.05:
                    #We are accepting null hypothesis
                    drift_report[base_column]={
                        "pvalues":same_distribution.pvalue,
                        "same_distribution": True

                    }
                    
                else:
                    drift_report[base_column]={
                        "pvalues":same_distribution.pvalue,
                        "same_distribution":False
                    pass
                    #different distribution
            self.validation_error[report_key_name]=drift_report
        except Exception as e:
            raise SensorException(e,sys)

    

    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        try:
            logging.info(f"reading base data Frame")
            base_df = pd.read_csv(self.data_validation_config.base_file_path)
            base_df.replace({"na":np.NaN},inplace=True)
            logging.info(f"Replace na value in base df")
            #base_df has na as null
            logging.info(f"Drop null values from base df")
            base_df = self.drop_missing_values_columns(df=base_df,report_key_name="missing_values_within_base_dataset")
            
            logging.info(f"Reading train Data Frame")
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            logging.info(f"Reading test Data Frame")
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            
            logging.info("Drop null values columns from train df")
            train_df = self.drop_missing_values_columns(df=train_df,report_key_name="missing_values_within_train_dataset")
                        logging.info("Drop null values columns from test df")
            test_df = self.drop_missing_values_columns(df=test_df,report_key_name="missing_values_within_test_dataset")
            
            logging.info(f"Is all required columns present in train df")
            train_df_columns_status = self.is_required_columns_exists(base_df=base_df, current_df=train_df,report_key_name="missing_columns_within_train_dataset)
            logging.info(f"Is all required columns present in test df")
            test_df_columns_status = self.is_required_columns_exists(base_df=base_df, current_df=test_df,report_key_name="missing_columns_within_test_dataset")
            
            if train_df_columns_status:
                logging.info(f"As all columns available in train df hence detecting data drift")
                self.data_drift(base_df=base_df, current_df=train_df,current_df=train_df,report_key_name="data_drift_within_train_dataset")
            if test_df_columns_status:
                logging.info(f"As all columns available in train df hence detecting data drift")
                self.data_drift(base_df=base_df, current_df=test_df,report_key_name="data_drift_within_test_dataset")

            #write the report
            utils.write_yaml_file(file_path=self.data_validation_config.report_file_path, data=self.validation_error)
            data_validation_artifact = artifact_entity.DataValidationArtifact(report_file_path=self.data_validation_config.report_file_path)
            return data_validation_artifact
        except Exception as e:
            raise SensorException(e, sys)
