from dataclasses import dataclass
#whatever files generated in each component,
# the paths will be available in artifact so that we can re use it in other components

@dataclass
#Here we are defining the output of dataingestion component
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str
# "..." is replacement for pass
@dataclass
class DataValidationArtifact:
    #the variable report_file_path  will be having location for the file report.yaml
    # It going to store string type data
    report_file_path:str
@dataclass
class DataTransformationArtifact:
    #The following variables store the object path/train/test paths
    transform_object_path:str
    transformed_train_path:str
    transformed_test_path:str
    target_encoder_path:str       


@dataclass
class ModelTrainerArtifact:
    model_path:str
    f1_train_score:float
    f1_test_score:float

class ModelEvaluationArtifact:...
class ModelPusherArtifact:...