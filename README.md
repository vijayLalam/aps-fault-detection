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
if you install libraries using pip install -r requirements.txt,then '-e.' trigger to install setup.py file(If you want your source code to be used as Library).'e' represent editable installation means we can edit our source code and '.' represent install setup .py file in current working directory.Without runninng setup file our source code as library with 0.0.0.1 version will not be released.without '-e.',setup file will not be triggered

---
if you use 'install_requires' ,then '-e.' is not required. so we need to remove it from requirements.txt
===
---
To install libraries required for source code
---
abc@f32c6df925e5:~/workspace$ pip freeze > requirements.txt
abc@f32c6df925e5:~/workspace$ pip install -r requirements.txt
===