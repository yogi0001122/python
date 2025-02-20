from config import Config
from data_pipeline import DataPipeline
from model import MLModel
from model_registry import ModelRegistry
from deployment import Deployment

# Load Configurations
config = Config()
print("Using API Key:", config.get_api_key())  # Secure API usage

# Load Data
pipeline = DataPipeline("s3://dataset.csv")
pipeline.load_data()
sample_data = pipeline.get_sample_data()

# Train Model
X, y = [[1, 4], [2, 5], [3, 6]], [0, 1, 0]  # Simulated Data
model = MLModel()
model.train(X, y)

# Register Model
registry = ModelRegistry()
registry.register_model("RandomForest", 85)

# Deploy Model
deployment = Deployment()
deployment.deploy_model("RandomForest")

print("Pipeline Execution Complete 🚀")
