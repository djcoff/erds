from abc import ABCMeta, abstractmethod

class Interface(metaclass=ABCMeta):
    
    def __init__(self):
        self.name = None
        self.type = None
        
        #self.info = InterfaceInfo
        #self.config = InterfaceConfig
    
    @abstractmethod    
    def open(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def configure(self): #second arg will be config info
        pass