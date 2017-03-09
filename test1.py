import sys
#import erd
#from erd.daq import *
#from erd.daq.instrument.cpc.tsicpc import TSI3010
#from erd.daq.interface.interface import TCPPort
#from erd.daq.instrument.cpc.tsicpc import TSI3010

#from erd.daq.instrument.instfactory import InstrumentFactory
from erd.daq import instrument
from erd.daq.instrument.instrument import Instrument
import pkgutil
import sys
import importlib

 
import inspect

# for name, data in inspect.getmembers(instrument.instrument,inspect.isclass):
#     print('{} : {!r}'.format(name, data))
#     # if name.startswith('__'):
#     #     continue
#     # print('{} : {!r}'.format(name, data))
    
# # for name, data in inspect.getmembers(instrument.instrument,inspect.ismodule):
# #     print('{} : {!r}'.format(name, data))
    
    
# def inheritors(cls):
#     subclasses = set()
#     work = [cls]
#     while work:
#         parent = work.pop()
#         for child in parent.__subclasses__():
#             if child not in subclasses:
#                 subclasses.add(child)
#                 work.append(child)
#     return subclasses
    
#print(inheritors(Instrument))

# def find_subclasses(module, clazz):
#     return [
#         cls
#             for name, cls in inspect.getmembers(module)
#                 if inspect.isclass(cls) and issubclass(cls, clazz)
#     ]

# print(find_subclasses(instrument,Instrument))

# def all_subclasses(cls):
#     return cls.__subclasses__() + [g for s in cls.__subclasses__()
#                                   for g in all_subclasses(s)]

# print(all_subclasses(vars()['Instrument']))

def get_subclasses(module_name,cls):
    subcls = []
    mod = importlib.import_module(module_name)
    for name, data in inspect.getmembers(mod,inspect.isclass):
        #print('{} : {!r}'.format(name, data))
        if (issubclass(data,cls) and not inspect.isabstract(data)):
            print('{} : {!r}'.format(name, data))
            subcls.append(data)
            #print(data)
            
    return subcls
            
def explore_package(module_name, cls, subs): 
    #subs = []
    mod = importlib.import_module(module_name)
    #loader = pkgutil.get_loader(mod.)
    #print(dir(loader))
    #print(loader.name)
    #print(find_subclasses(mod,cls))
    #print(issubclass(cls,cls))
    #get_subclasses(module_name,cls)
    
#    for sub_module in pkgutil.walk_packages([loader.name]):
    for sub_module in pkgutil.iter_modules(mod.__path__):
        #print(sub_module)
        importer, sub_module_name, ispkg = sub_module
        print ('sub_module: '+sub_module_name+' ('+str(ispkg)+')')

        #sub_module.is_package
        #importlib.import_module(qname)
        qname = module_name + "." + sub_module_name
        #print(qname)
        if ispkg:
            explore_package(qname,cls,subs)
        else:
            #submod = importlib.import_module(qname)
            for subcls  in get_subclasses(qname,cls):
                if subcls not in subs:
                    subs.append(subcls)
            #print('Look for subclass in: ' + qname)
            #print(inspect.getmodulename(qname))
            #pass


    return subs

sub_list = []    
sub_list = explore_package('erd.daq.instrument',Instrument, sub_list)
print(sub_list)
for cls in sub_list:
    print('Instrument subclass: ' + cls.__name__)
#mod_ = importlib.import_module(inst_config['module'])

#get_subclasses('erd.daq.instrument.instrument',Instrument)