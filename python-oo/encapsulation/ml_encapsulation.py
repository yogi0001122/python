class DataPipeline:
    def __init__(self):
        self.__data = []   #private variable storing training data

    def load_data(self, data_source):
        print(f"loading data from {data_source}")
        self.__data = ["record1", "record2", "record3"]
    
    def get_data_sample(self):
        return self.__data[:2] # Retrun only a sample (not entire data)
    

pipeline = DataPipeline()
pipeline.load_data("s3://sample-datastore")
print(pipeline.get_data_sample())