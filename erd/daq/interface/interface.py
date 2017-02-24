from abc import ABCMeta, abstractmethod
import asyncio
"""
Interface
Abstract base class for HW Interface between Instrument class and "hardware". 
Interface requires:
   - event loop (asyncio) 
   - configuration (dictionary with hw specific values)
"""

class Interface(metaclass=ABCMeta):
    
    def __init__(self):
        self.name = None
        self.type = None
        self.loop = None
        
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
    
    
class SerialPort(Interface):
    
    def __init__(self):
        super().__init__(self)
        
    def open(self):
        pass
    
    def close(self):
        pass
    
    def configure(self):
        pass
    
    
class TCPPort(Interface):
    
    def __init__(self):
        super().__init__(self)
        
    def open(self):
        pass
    
    def close(self):
        pass
    
    def configure(self):
        pass
    