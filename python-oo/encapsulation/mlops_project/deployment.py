class Deployment:
    def __init__(self):
        self.__deployed_models = []  # Securely track deployed models

    def deploy_model(self, model_name):
        print(f"Deploying {model_name} to Kubernetes cluster...")
        self.__deployed_models.append(model_name)

    def get_deployed_models(self):
        return self.__deployed_models  # Securely expose deployed models

deploy = Deployment()
deploy.deploy_model("RandomForest")
print(deploy.get_deployed_models())  # Output: ['RandomForest']
