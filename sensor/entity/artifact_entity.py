from dataclasses import dataclass


@dataclass
#Here we are defining the output of dataingestion component
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str
# "..." is replacement for pass
class DataValidationArtifact:
    #the variable report_file_path  will be having location for the file report.yaml
    # It going to store string type data
    report_file_path:str



class DataTransformationArtifact:...
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...