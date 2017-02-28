
#from __future__ import generators
from erd.daq.instrument.instrument import *
import sys

class InstrumentFactory:
    
    factories = {}
    
    @staticmethod
    def build_factories():
        dummy = {"name":"dummy","class":"DummyInstrument"}
        print(dummy)
        InstrumentFactory.factories[dummy['name']] = dummy
        
        # loop through all subclasses to get config
        
    @staticmethod
    def create(config):
        
        try:
            print('Creating: ' + config['name'])
            print('   ClassName: ' + config['class'])
            inst_class = eval(config['class'])
            return inst_class.factory_create()
       
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        
        # print(InstrumentFactory.factories)
        # if name in InstrumentFactory.factories:
            
        #     inst_desc = InstrumentFactory.factories[name]
        #     inst_class = eval(inst_desc['class'])
        #     print(inst_class)
        #     return inst_class.factory_create()
        
        # else:
            
        #     print('Unknown instrument: %s' % name)
            