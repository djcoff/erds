'''
instrument.py: 
    define the abstract instrument class that will be inherited by all
    instruments in the erd suite. 
'''
from erd.daq.daq import DAQ
from erd.daq.interface.ifacefactory import InterfaceFactory
import abc

import asyncio

class Instrument(DAQ):
#class Instrument(abc.ABCMeta):
    #Eventually this will be a metadata class
    
    
    
    base_config = {}
    
    def __init__(self,config):
        super().__init__()
        self.name = 'Instrument'
        self.type = 'Generic'
        self.mfg = None
        self.model = None
        print("Name: ", self.name)
        
        self.parameter_list = {}
        
        self.config = config
        self.iface_map = {}
        self.configure()
        #info = InstrumentInfo()
        #interface = Interface()
    
    def open(self):
        pass
    
    @abc.abstractmethod
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def configure(self):
        imap = self.config['interface_map']
        for key in imap.keys():
            print('key : ' + key)
            iface_cfg = imap[key]
            print(iface_cfg)
            iface = InterfaceFactory.create(iface_cfg)
            print(iface)
            self.iface_map[key] = iface

    # @abstractmethod
    def configure_param_list():
        pass
    
    # @staticmethod
    # @abc.abstractmethod
    # def factory_create():
    #     pass
           
    
    # @classmethod
    # def _get_base_config():
        
    
    # @classmethod
    # @abstractmethod
    # def get_config():
    #     pass
        
        
        
    

class DummyInstrument(Instrument):

    def __init__(self,config):
        super().__init__(config)
        self.name = 'DummyInstrument'
        self.type = 'Test'
        self.mfg = "DummyMfg"
        self.model = "DummyModel"
        print("Name: ", self.name)
        
        self.is_running = False
        
        #info = InstrumentInfo()
        #interface = Interface()

    def configure_param_list(self):
        
        # param_list should definte 'polled|unpolled' and what command needs 
        #            to be sent polled reads
        
        # define param
        param = {
            'input':'default',
            'output':'default',
            'interface':None,
            'name':'temperature_dp',
            'long_name':'Dewpoint Temperature',
            'units':'C'
        }
        self.parameter_list[param['name']] = param
        
        # param = {
        #     'input':'default'
        #     'output':'default'
        #     'interface':None
        #     'name':'temperature'
        #     'long_name':'Temperature'
        #     'units':'C'
        # }
        # self.parameter_list[param['name']] = param

        # param = {
        #     'input':'default'
        #     'output':'default'
        #     'interface':None
        #     'name':'pressure'
        #     'long_name':'Pressure'
        #     'units':'mbar'
        # }
        # self.parameter_list[param['name']] = param

    
    def open(self):
        pass
        #task = asyncio.ensure_future(run_client(message,loop))

    def start(self):
        
        # start interface(s)
        for key in self.iface_map.keys():
            #print('key: '+key)
            self.iface_map[key].start()
            task = asyncio.ensure_future(self.read_loop())
            self.task_list.append(task)
        
        self.is_running = True
        
    def stop(self):
        print("stopping DummyInstrument")
        tasks = asyncio.Task.all_tasks()
        for t in self.task_list:
            t.cancel()
            tasks.remove(t)
        self.is_running = False
        
        ### THIS ISN'T RIGHT BUT FOR NOW...
        # stop interfaces
        for key in self.iface_map.keys():
            print('key: '+key)
            self.iface_map[key].stop()

    # def configure(self):
    #     pass
    
    # @staticmethod
    # def factory_create():
    #     return DummyInstrument()
        
    def read(self):
        print("DummyInstrument.read()")
        
        for key in self.iface_map.keys():
            iface = self.iface_map[key]
            #print(iface)
            ts,buf = self.iface_map[key].read(buffer=key)
            #buf = ''
            print('buffer['+key+']: ' + ts.strftime('%Y-%m-%d %H:%M:%S') + ' -- ' + buf)

        
    async def read_loop(self):
        while self.is_running:
            self.read()
            await asyncio.sleep(1)
            
# Need to include event loop at this level