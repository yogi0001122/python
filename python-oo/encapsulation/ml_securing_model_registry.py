class ModelRegistry:
    def __init__(self):
        self.__models = {} #Private dict to store models

    def register_model(self, model_name, accuracy):
        if accuracy > 80:
            self.__models[model_name] = accuracy
            print(f"Model '{model_name}' registered successfully..")
        else:
            print ("Model accuracy too low for registration")
    
    def get_regsitered_models(self):
        return self.__models
    
registry = ModelRegistry()
registry.register_model("RandomForest", 85)
registry.register_model("KNN", 75)
print(registry.get_regsitered_models())