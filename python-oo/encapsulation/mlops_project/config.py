class Config:
    def __init__(self):
        self.__api_key = "SECRET_123456"
        self.__db_password = "DB_PASS_9876"

    def get_api_key(self):
        return "******"  # Hide actual API key

    def get_db_password(self):
        return "******"

config = Config()
print(config.get_api_key())  # Output: ******
