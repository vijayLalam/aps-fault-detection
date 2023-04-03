from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from typing import Optional
from sensor.logger import logging
import os,sys
from xgboost import XGBClassifier
from sensor import utils
from sklearn.metrics import f1_score


class ModelTrainer:
    def __init__(self,model_trainer_config:config_entity.ModelTrainerConfig,data_transformation_artifact:artifact_entity.DataTransformationArtifact):
        try:
        def train_model(self,x,y):
            xgb_clf=XGBClassifier()
            xgb_clf.fit(x,y)
            return xgb_clf

            
        except Exception as e:
            raise e

        def train_model(self,x,y):
            xgb_clf=XGBClassifier()
            xgb_clf.fit(x,y)
            return xgb_clf
    def initiate_model_trainer()->artifact_entity.ModelTrainerArtifact:
        try:
            train_arr=utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_path)
            test_arr=utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_path)
            
            x_train,y_train = train_arr[:,:,-1],train_arr[:,-1]
            x_test,y_test = test_arr[:,:,-1],train_arr[:,-1]
        
            model =train_model(x=x_train,y=y_train)
            logging.info(f"Calculating f1 train score")
            yhat_train=model.predict(x_train)
            f1_train_score = f1_score(y_true=y_train , y_pred = yhat_train)
            
            logging.info(f"Calculating f1 test score")
            yhat_test=model.predict(x_test)
            f1_test_score = f1_score(y_true=y_train , y_pred = yhat_test)
            logging.info(f"train score:{f1_train_score} and tests score {f1_test_score}")
            
            #check for overfitting or underfitting or expected score
            #overfitting getting accuracy with train data but not test data
            #underfitting means accuracy for both train and test data
            #Expected score means what score we are expecting  atleast from this model
            logging.info(f"Checking if our model is underfitting or not")
            if f1_test_score<self.model_trainer_config.expected_score:
                raise Exception(f"Model is not good as it is not able to give \
                expected accuracy: {self.model_trainer_config.expected_score}: model actual score: {f1_test_score}")
            logging.info(f"Checking if our model is overfitting or not")
            diff = abs(f1_train_score-f1_test_score)
            if diff > self.model_trainer_config.overfitting_threshhold:
                raise Exception(f"Train and test score diff:{diff} is more than overfitting threshold {self.model_trainer_config.overfitting_threshold}")

            #save the trained model
            logging.info(f"Saving mode object")
            utils.save_object(file_path = self.model_trainer_config.model_path,obj=model)

            #prepare artifact
            logging.info(f"Prepare the artifact")
            model_trainer_artifact=artifact_entity.ModelTrainerArtifact(model_path=self.model_trainer_config.model_path,
            f1_train_score=f1_train_score,f1_test_score=f1_test_score)
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            return model_trainer_artifact



        except Exception as e:
            raise e
   



