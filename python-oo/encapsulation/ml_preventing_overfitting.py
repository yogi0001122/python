class MLModel:
    def __init__(self):
        self.__learning_rate = 0.01 # Private variable
    
    def set_learning_rate(self, new_lr):
        if 0.0001 <= new_lr <= 0.1: # Restrict learning rate range
            self.__learning_rate = new_lr
            print (f"Learning rate updated to {new_lr}")
        else:
            print ("Invalida learning rate. Must be b/w 0.0001 and 0.1")

    def get_learning_rate(self):
        return self.__learning_rate
    
model = MLModel()
model.set_learning_rate(0.05)
model.set_learning_rate(1.0)
print(model.get_learning_rate())