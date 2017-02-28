'''
daq.py: 
    define the abstract DAQ class that will be inherited by all
    members of the DAQ class in the erd suite. 
'''

import abc
import asyncio

class DAQ(metaclass=abc.ABCMeta):
#class Instrument(abc.ABCMeta):
    #Eventually this will be a metadata class
    
    def __init__(self):
        self.name = 'DAQ'
        self.type = 'Generic'
        self.mfg = None
        self.model = None
        print("Name: ", self.name)
        
        #info = InstrumentInfo()
        #interface = Interface()
        self.loop = asyncio.get_event_loop()
        
    @abc.abstractmethod
    def configure(self):
        pass
    
    @staticmethod
    @abc.abstractmethod
    def factory_create():
        pass

       
    
# Need to include event loop at this level