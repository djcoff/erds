
#from __future__ import generators
from erd.daq.instrument.instrument import *

import importlib
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
        inst_config = config['instrument']
        print("module: " + inst_config['module'])
        print("class: " + inst_config['class'])
        
        try:
            #print('Creating: ' + config['name'])
            #print('   ClassName: ' + config['class'])
            mod_ = importlib.import_module(inst_config['module'])
            cls_ = getattr(mod_,inst_config['class'])
            #inst_class = eval(config['class'])
            #return inst_class.factory_create()
            return cls_(config)
            
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
            