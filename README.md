# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```
To download the dataset:
----
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
----
This change has been made in Neuro LAB to check conflict of entering data both in vscode and g
GIT COMMANDS
If you are starting a project and you want to use git in your project
-----
git init
-----
Note: This is going to initialize git in your source code


OR

You can clone existing github repo
----
git clone <github_url>
Note:Clone/ Download github repo in your system

Add your change made in file to get staggong area
---
git add file_name
---
Note:you can given file_name to add specific file or use "." to add everything in current working directory(here Workspace)  to staging area

Create Commits
---
git commit -m "message"
---

---
git push origin main
---
Note:Origin contains URL to your git hub repo
main->your branch name

To pull your changes from github repo
---
git pull origin main
---

To push your changes forcefully 
---
git push origin main -f
---
---
install_requires in setup.py file
---
install_requires is a section within the setup.py file in which you need to input a list of the minimum dependencies needed for a project to run correctly on the target operating system (such as ubuntu). When pip runs setup.py, it will install all of the dependencies listed in install_requires.
For example, if your project includes matplotlib, you’ll need to list it, as well as its dependency of NumPy in install_requires as shown below:
---
install_requires=['<matplotlib>','<numpy>']
---
====
significance of '-e.' in requirements.txt
====
if you install libraries using pip install -r requirements.txt,then '-e.' trigger to install setup.py file(If you want your source code to be used as Library).'e' represent editable installation means we can edit our source code and '.' represent install setup .py file in current working directory.If you want your source code is to be installed as Library,setup.py file must be installed.gWithout runninng setup file our source code as library with 0.0.1 version will not be released.without '-e.',setup file will not be triggered

---
if you use 'install_requires' ,then '-e.' is not required. so we need to remove it from requirements.txt
===
---
To install libraries required for source code
---
abc@f32c6df925e5:~/workspace$ pip freeze > requirements.txt
abc@f32c6df925e5:~/workspace$ pip install -r requirements.txt
===
After running the above command,sensor.egg-info will be created under sensor folder
Due to the presence of -.e in the requirements.txt file,setup.py is triggered to install our source code available in the sensor folder along with __init__.py file.findpackages() in the setup.py file try to find out the folder having __init__.py file and consider the folder as package/Library and the  the source code file in that folder as module
----------------------------------------------------------------------------------------------------------------------------
===== Model Training pipeline=====
In Jupyter Note book---After EDA,Preprocessing & Feature Engineering and comparing accuracy of various models picking up best model,We will go for "Model training Pipeline"
Pipeline means sequence of components executed in specific order.Each component requires some input(configuration in iNeuron) and generates some output(artifact)
An artifact is a machine learning term that is used to describe the output created by the training process in training pipeline . Output could be a fully trained model, a model checkpoint, or a file or a graph created during the training process.

Model Training pipe Line:
Dumping data or continuous streaming data into mongoDB is data engineer job
Data Ingestion->Data Validation ->Data Transformation->Model Trainer ->Model Evaluation->Model Pusher
Our training pipe line should be such away that even if there is a data drift or increase of data volume(streaming) ,we should be able to use the same code to train the model 
considering new production data set

1)Data Ingestion:
Bringing Data from Data Source(here We pulled/fetched the data from MongoDB)
Splitting data set into 3 files(Training,Validation,testing ) or 2 files(Traing and Testing) parts

2)Data Validation:
We have to check is there any data drift.
Data drift:It is defined as a variation in the production data from the data that was used to test and validate the model before deploying it.for ex:if a col of training/test data is normally distributed,the same col of product dataset also should be normally distributed.Then we have to retrain our model considering both old and new(production) dataset
Checking the data is valid or not i.e., correct or not.It's not EDA/Feature Engineering
Checking datatypes of dataset,no of columns,column data is numerical or not,how many records are having missing values
Here we will have base dataseti.e., dataframe on which we will apply EDA & Model Training

3)data Transformation:
Scaling(Standard Scaling/MinMax Scalar)
Converting Categorical data into Numerical data
4)Model Trainer:
Picking up the best model and parameter tuning using Grid search CV etc
5)Model Evaluation:
Testing model
If u r creating new model,compare it's accuracy with the existing model's accuracy which is already in production.
If newly trained model gives better accuracy,the model in production will be replaced with it
5)Model Pusher:
If newly trained model gives better accuracy,the model in production will be replaced with it.Model pusher will push the newly trained model into production
===========================================================
====ML/Deeplearning training pipeline====
https://www.tensorflow.org/tfx
============================================================
A TFX pipeline is a sequence of components that implement an ML pipeline which is specifically designed for scalable, high-performance machine learning tasks. Components are built using TFX libraries which can also be used individually.

We created 6 components under sensor based on data pipeline

==========================================================
Folders under Sensor:
Entity:To define the structure of i/p and o/p of each component in the training pipeline
Utils:Some helper functions may be required to load ur model,to save ur model,to save the artifacts in S3 bucket.These helper functions will be defined in Utils folder.

Entity:Defining i/p & O/p in entity folder
We should know the what is the i/p(configuration) required for particular component& what o/p(artifact) it will generate.
We have to create 7 confguration & 6 artifacts in entity folder for all the 6 components in traing pipeline
pipeline:
the 6 components will be arranged in sequence in training_pipeline.py
=========================================

========Logging==========================
Logging is a Python module in the standard library that provides the facility to work with the framework for releasing log messages from the Python programs. Logging is used to tracking events that occur when the software runs.
Logging is beneficial to store the logging records. Suppose there is no logging record, and the program is interrupted during its execution, we will be unable to find the actual cause of the problem.
Logging Levels-
Notset(0)
Debug (10): These are used to give Detailed information, typically of interest only when diagnosing problems.
Info (20): These are used to confirm that things are working as expected
Warning (30): These are used an indication that something unexpected happened, or is indicative of some problem in the near future
Error (40): This tells that due to a more serious problem, the software has not been able to perform some function
Critical(50) : This tells serious error, indicating that the program itself may be unable to continue running
===============================================================================================================

=================logger.py================
logger.py is created under sensor folder
logs directory path and logging level are defined in this file
===============================================================================================================
==================exception.py=============
exception.py is created under sensor folder to create customized exceptions
It will give the details ----from which file,line no   the exception occured.It also gives the error message
================================================================================================================
========We tested the logger.py & exception.py code with the following code being written in main.py========
from sensor.logger import logging
from sensor.exception import SensorException
import sys,os

def test_logger_and_exception():
     try:
          logging.info("Starting the test_logger_and_exception")
          result =3/0
          print(result)
          logging.info("Stopping the test_logger_and_excedption")
     except Exception as e:
          logging.debug("Stopping the test_logger_and_excedption")
          raise SensorException(e, sys)
if __name__=="__main__":
     try:
          test_logger_and_exception()
     except Exception as e:
          print(e)
----The log file created under the folder logs
==========================================================================================================================================
============config.py under sendor folder==============
Here mongodb local host url has been given to connect python to mongodb
Here we pass externally  URL/Secret Keys that are required for our code using 'Environmentvariable'
Exact variable name "MONGO_DB_URL" should be there in .env file
we created instance of class "EnvironmentVariable" as env_var
The MongoDB URL is assigned to variable 'mongo_client'This can be imported  in any other modules by using 
from sensor.config import mongo_client
=============================================================================================
==============.env======================================
Here we mention the exact mongoDB url/Secret Key/Accesskey that will be used in by 'environment variable' in config.py
 the URL will be changed in  development environment , staging environment , production environment.
 so we can change the URL here accordingly without disturbing the source code.
We should not expose mongoDB url to others in githum.So we keep it in .gitignore
 ===============================================================================================
==============================utils.py====================
The data from mongodb will be exported to Data Frame usin the function 'get_collection_as_dataframe()'
We have to pass database_name & Collection_name to this Function and it returns DataFrame
Unnecessary column '_id' has been removed
==========================================================================================================

===============config_entity.py====================
    Traingingpipelineconfig in config_entity is to store each file we generate
and all the outputs of our model like model o/p,graph, metrics in a folder(artifact) 
    We have to pass object of TrainingPipeLineConfig to every component in training pipeline
so that o/p folder for each component will be created in the object of the class TrainingPipelineConfig(self.artifact_dir) i.e., path:arifact/time stamp/data_ingestion
    Data ingestion o/p we have to generate here  
-----------------------------------------------------------------------------------------------------
===========================Entity folder under Sensor=================================
config_entity.py:Any input to the data pipeline components will be defined in the config_entity.py
Here, Under dataingestion dir, we define the feature store file path,train dataset file path,
 test dataset file path and artifact dir path.
Feature store is having data(df) on which we can start applying ML pipeline 
artifact_entity.py:Any output from the data pipe line components will be defined in the artifact_entity.py
here we are giving reference to the output data which we can use it in other components,if we are interested
========================data_ingestion.py=======================
Bringing Data from Data Source(here We pulled/fetched the data from MongoDB)
Splitting data set into 3 files(Training,Validation,testing ) or 2 files(Traing and Testing) parts
========================data validation=======================
Here we need base dataset(aps_failure_training_set1.csv) on which EDA & FE have done by my team
Using this dataset I will validate train & test dataset
We will check no.of columns,column names and distribution
In this Dataset,everything is numerical.So we can check for numerical datatype
1)NULL HYPOTHESIS
Now we will check whether train.csv ,test.csv and base dataset(aps_failure_training.set1.csv) having same distribution or not 
using scipy.stats(null hypothesis)
if pvalue is > 0.05,then the two distributions rae identical
if pvalue < 0.05 ,the base distrivution and test/train dataset distribution are not identical.So we have to retrain our model.
Retraining model means,we have to use new/updated data(After EDA and FE) to train our existing model to update model
 or create new model
 2)ANAMOLY DETECTION in my Dataset
 DATA DRIFT:
  i)High Null Value
  ii)Missing columns
  iii)Outlier
  iV)Categorical:
  Gender --> MALE,FEMALE,OTHER
MODEL DRIFT/TARGET DRIFT:
 In classification problem:the target may be binary classification now.In future the categories may be 3.
 In regression problem:Earlier the price of land per sq yard is 10000.suddenly a 6 lane road coming to that area so the price will be increased to 1 lakh/sq yard.This is Target drift in Regression problemTo predict this data we have to retrain the model
CONCEPT DRIFT:
if the relationship between i/p features and target feature changes