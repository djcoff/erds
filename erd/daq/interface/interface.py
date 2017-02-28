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
        self.__inputs = []
        self.__outputs = []
        
    
    @abstractmethod    
    def open(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def configure(self): #second arg will be config info
        pass
    
    @property
    def inputs(self):
        return self.input_list
        
    @inputs.setter    
    def inputs(self,input_list):
        self.input_list = input_list

        
    def add_input(iface_input):
        self.input_list.append(iface_input)
    
    def output_list():
        return self.output_list
        
    def output_list(output_list):
        self.output_list = output_list

    def add_output(iface_output):
        self.output_list.append(iface_output)
    
    
    
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
    