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
Data Ingestion->Data Validation ->Data Transformation->Model Trainer ->Model Evaluation->Model Pusher
1)Data Ingestion:
Bringing Data from Data Source
Splitting data set into 3 files(Training,Validation,testing ) or 2 files(Traing and Testing) parts
2)Data Validation:
Checking the data is valid or not i.e., correct or not.It's not EDA/Feature Engineering
Checking datatypes of dataset,no of columns,column data is numerical or not,how many records are having missing values
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

==========================================================
Folders under Sensor:
Entity:To define the structure of i/p and o/p of each component in the training pipeline
Utils:Some helper functions may be required to load ur model,to save ur model,to save the artifacts in S3 bucket.These helper functions will be defined in Utils folder.
step1:

Entity:Defining i/p & O/p in entity folder
We should know the what is the i/p(configuration) required for particular component& what o/p(artifact) it will generate.
We have to create 7 confguration & 6 artifacts in entity folder for all the 6 components in traing pipeline
=========================================
========Logging==========================
Logging is a Python module in the standard library that provides the facility to work with the framework for releasing log messages from the Python programs. Logging is used to tracking events that occur when the software runs.
Logging is beneficial to store the logging records. Suppose there is no logging record, and the program is interrupted during its execution, we will be unable to find the actual cause of the problem.