'''
instrument.py: 
    define the abstract instrument class that will be inherited by all
    instruments in the erd suite. 
'''
from erd.daq.daq import DAQ
import abc

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
    
# Need to include event loop at this level