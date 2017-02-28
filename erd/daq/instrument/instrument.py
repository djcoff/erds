'''
instrument.py: 
    define the abstract instrument class that will be inherited by all
    instruments in the erd suite. 
'''
from erd.daq.daq import DAQ
import abc

import asyncio

class Instrument(DAQ):
#class Instrument(abc.ABCMeta):
    #Eventually this will be a metadata class
    
    def __init__(self):
        self.name = 'Instrument'
        self.type = 'Generic'
        self.mfg = None
        self.model = None
        print("Name: ", self.name)
        
        #info = InstrumentInfo()
        #interface = Interface()
    
    @abc.abstractmethod
    def start(self):
        pass
    
    def stop(self):
        pass

    def configure(self):
        pass
    
    @staticmethod
    @abc.abstractmethod
    def factory_create():
        pass
           
    

class DummyInstrument(Instrument):

    def __init__(self):
        self.name = 'DummyInstrument'
        self.type = 'Test'
        self.mfg = "DummyMfg"
        self.model = "DummyModel"
        print("Name: ", self.name)
        
        #info = InstrumentInfo()
        #interface = Interface()
    
    def start(self):
        task = asyncio.ensure_future(run_client(message,loop))
            
    def stop(self):
        pass

    def configure(self):
        pass
    
    @staticmethod
    def factory_create():
        return DummyInstrument()
        
    def read():
        print("DummyInstrument.read()")
        
    async def read_loop():
        await self.read()
    
# Need to include event loop at this level