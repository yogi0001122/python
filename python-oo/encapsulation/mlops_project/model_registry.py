class ModelRegistry:
    def __init__(self):
        self.__models = {}  # Store models securely

    def register_model(self, model_name, accuracy):
        if accuracy > 80:  # Register only high-performing models
            self.__models[model_name] = accuracy
            print(f"Model '{model_name}' registered successfully.")
        else:
            print("Model accuracy too low for registration.")

    def get_registered_models(self):
        return self.__models  # Securely expose registered models

registry = ModelRegistry()
registry.register_model("RandomForest", 85)  # ✅ Model registered
registry.register_model("KNN", 75)  # ❌ Model rejected
