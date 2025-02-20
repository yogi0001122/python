class Config:
    def __init__(self):
        self.__api_key = "SECRET-123456"  # Private variable

    def get_api_key(self):
        return "******"  # Masked key for security

    def set_api_key(self, new_key):
        if len(new_key) > 10:  # Basic validation
            self.__api_key = new_key
        else:
            print("Invalid API Key!")

config = Config()
print(config.get_api_key())  # Output: ******
config.set_api_key("NEW_SECRET")  # API key updated securely
