import pandas as pd

class DataPipeline:
    def __init__(self, data_source):
        self.__data_source = data_source  # Private variable
        self.__data = None  # Store dataset securely

    def load_data(self):
        print(f"Loading data from {self.__data_source}...")
        self.__data = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6]})  # Simulated data

    def get_sample_data(self):
        return self.__data.head(2)  # Only expose sample data

pipeline = DataPipeline("s3://dataset.csv")
pipeline.load_data()
print(pipeline.get_sample_data())  # Output: First 2 rows of the dataset
