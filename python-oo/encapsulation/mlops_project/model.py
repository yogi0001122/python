from sklearn.linear_model import LogisticRegression

class MLModel:
    def __init__(self, model_type="LogisticRegression"):
        self.__learning_rate = 0.01  # Private variable
        self.__model = None  # Store trained model

    def set_learning_rate(self, new_lr):
        if 0.0001 <= new_lr <= 0.1:  # Restrict learning rate range
            self.__learning_rate = new_lr
            print(f"Updated learning rate to {new_lr}")
        else:
            print("Invalid learning rate!")

    def train(self, X, y):
        print("Training model...")
        self.__model = LogisticRegression()
        self.__model.fit(X, y)

    def get_model(self):
        return self.__model  # Securely expose trained model

model = MLModel()
model.set_learning_rate(0.05)  # Output: Updated learning rate to 0.05
