
class TrainingPipelineConfig:


#Trainging pipeline config is to store each file we generate
#  and all the outputs of our model like model o/p,graph, metrics in a folder(artifact) 
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name="aps"
        self.collection_name="sensor"
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir)
# "..." is for pass
class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...

