from abc import ABCMeta, abstractmethod
import asyncio
from erd.daq.daq import DAQ

"""
Interface
Abstract base class for HW Interface between Instrument class and "hardware". 
Interface requires:
   - event loop (asyncio) 
   - configuration (dictionary with hw specific values)
"""

class Interface(DAQ):
    
    def __init__(self):
        super().__init__()
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
        super().__init__()
        
    def open(self):
        pass
    
    def close(self):
        pass
    
    def configure(self):
        pass
    