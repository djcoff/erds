import sys
#import erd
#from erd.daq import *
#from erd.daq.instrument.cpc.tsicpc import TSI3010
#from erd.daq.interface.interface import TCPPort
#from erd.daq.instrument.cpc.tsicpc import TSI3010

from erd.daq.instrument.instfactory import InstrumentFactory
from erd.daq.instrument.instrument import Instrument

import asyncio
import inspect


#for line in sys.path: print(line)

#cpc_direct = TSI3010()
#tcp_port = TCPPort()

## Test compass with event loop
#     import asyncio
#     #from ...interface.interface import TCPPort
#     #from daq.interface.interface import TCPPort
    
#     test_path()

#     import instrument
#     #from daq.instrument.cpc.tsicpc import TSI3010


# def get_subclasses(class):
    
#     return class.__subclasses__()

# def get_instrument_list():
#     instruments = ()
    
#     cls = Instrument()
    
#     cls_list = get_subclasses(cls)
    
    

# def build_class_config():

def dummy_build_inst_config():
    dummy_inst = {
        "name":"dummy_inst",
        "module":"erd.daq.instrument.instrument",
        "class":"DummyInstrument"
        
    }
    
    dummy_iface = {
        "name":"dummy_iface",
        "module":"erd.daq.interface.interface",
        "class":"DummyPort",
        "iface_cfg": {"host":"moxa16phys1.pmel.noaa.gov","port":4002}
    }

    tcp_iface = {
        "name":"tcpport_iface",
        "module":"erd.daq.interface.interface",
        "class":"TCPPort",
        "iface_cfg": {"host":"192.168.86.106","port":4001}
    }
    
    inst_plist_map = {
        "default":dummy_iface
        #"default":tcp_iface
    }
    
    dummy = {
        "instrument":dummy_inst,
        "interface_map":inst_plist_map
    }
    

    return dummy

task_list = []
names = ['one','two','three']

class TestTask:
    index = 0

    def __init__(self):
        self.name = names[TestTask.index]   
        self.counter = 0
        TestTask.index += 1
        
    def run(self):
        print('Running:' + self.name)
        if (self.counter > 10):
            self.counter = 0
        else:
            self.counter += 1
        
        
async def run_task(cls):

    #await tcp_echo_client(message, loop) 
    while True:
        cls.run()
        if (cls.counter > 10):
            new_task()
        await asyncio.sleep(.25)

def new_task():
    
    if TestTask.index < 3:
        task_cls = TestTask()
        task = asyncio.ensure_future(run_task(task_cls))
        task_list.append(task)
    
async def heartbeat():
    while True:
        print("beat")
        await asyncio.sleep(10)
    

if __name__ == "__main__":


    #InstrumentFactory.build_factories()

    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(heartbeat())
    
    config = dummy_build_inst_config()
    dummy = InstrumentFactory.create(config)
    dummy.start()
    
    print(dummy)
    
    # classNameGen()
    
    #print(InstrumentFactory.__name__)
    
    #print(dummy.__class__.__name__)
    #print(dummy.__doc__)
    #print(dummy.__file__)
    #print(dummy.__name__)
    #print(dummy.__qualname__)
    #print(dummy.__module__)

    # async def run_client(message, loop):
    #     await tcp_echo_client(message, loop) 
    #new_task()
    #print(task_list)
    # task = asyncio.ensure_future(run_client(message,loop))

    # iface_config = {
    
    task_list = asyncio.Task.all_tasks()
    try:
        #loop.run_forever()
        #loop.run_until_complete(tcp_echo_client(message, loop))
        #loop.run_until_complete(asyncio.wait([task,]))
        loop.run_until_complete(asyncio.wait(task_list))
    except KeyboardInterrupt:
        dummy.stop()
         #pass
        for task in task_list:
            task.cancel()
        loop.run_forever()
    #    task.exception()
    #    loop.stop()
    finally:
        #loop.run_until_complete(loop.shutdown_asyncgens())
        print('stopping loop...')
        loop.stop()
