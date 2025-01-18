
class ModelHandler:
    def __init__(self):
        self.__holding_model = ""
        
    @property
    def holding_model(self):
        return self.__holding_model
    
    @holding_model.setter
    def holding_model(self, path: str):
        self.__holding_model = path

    