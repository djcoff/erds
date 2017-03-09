
import abc
import pkgutil
import inspect
import importlib

from erd.daq.instrument.instrument import Instrument
from erd.daq.interface.interface import Interface

#class DAQConfig(metaclass=abc.ABCMeta):
class DAQConfig():
    
    INSTRUMENT = {'module':'erd.daq.instrument','class':Instrument}
    INTERFACE = {'path':'erd.daq.interface','class':Interface}
    
    
    def __init__(self):
        
        # dictionary to hold config
        self.config = {}
        
    @staticmethod
    def get_list(hw):
        
        hwlist = DAQConfig._build_hw_list(hw['module'],hw['class'])

        return hwlist

    @staticmethod
    def _build_hw_list(mod_name,cls):
        
        hwlist = []
        
        DAQConfig._find_subclasses(mod_name,cls,hwlist)

        return hwlist
    @staticmethod    
    def _find_subclasses(mod_name,cls,hwlist):
        mod = importlib.import_module(mod_name)
        for sub_module in pkgutil.iter_modules(mod.__path__):
            importer, sub_mod_name, ispkg = sub_module
            qname = mod_name + "." + sub_mod_name
            if ispkg:
                DAQConfig._find_subclasses(qname,cls,hwlist)
            else:
                for subcls  in DAQConfig._get_subclasses(qname,cls):
                    if subcls not in hwlist:
                        hwlist.append(subcls)
           
        return hwlist
        
    @staticmethod    
    def _get_subclasses(mod_name,cls):
        subcls = []
        mod = importlib.import_module(mod_name)
        for name, data in inspect.getmembers(mod,inspect.isclass):
            if (issubclass(data,cls) and not inspect.isabstract(data)):
                #print('{} : {!r}'.format(name, data))
                subcls.append(data)
                #print(data)
        return subcls
        
# def get_subclasses(module_name,cls):
#     subcls = []
#     mod = importlib.import_module(module_name)
#     for name, data in inspect.getmembers(mod,inspect.isclass):
#         #print('{} : {!r}'.format(name, data))
#         if (issubclass(data,cls) and not inspect.isabstract(data)):
#             print('{} : {!r}'.format(name, data))
#             subcls.append(data)
#             #print(data)
            
#     return subcls
            
# def explore_package(module_name, cls, subs): 
#     #subs = []
#     mod = importlib.import_module(module_name)
#     #loader = pkgutil.get_loader(mod.)
#     #print(dir(loader))
#     #print(loader.name)
#     #print(find_subclasses(mod,cls))
#     #print(issubclass(cls,cls))
#     #get_subclasses(module_name,cls)
    
# #    for sub_module in pkgutil.walk_packages([loader.name]):
#     for sub_module in pkgutil.iter_modules(mod.__path__):
#         #print(sub_module)
#         importer, sub_module_name, ispkg = sub_module
#         print ('sub_module: '+sub_module_name+' ('+str(ispkg)+')')

#         #sub_module.is_package
#         #importlib.import_module(qname)
#         qname = module_name + "." + sub_module_name
#         #print(qname)
#         if ispkg:
#             explore_package(qname,cls,subs)
#         else:
#             #submod = importlib.import_module(qname)
#             for subcls  in get_subclasses(qname,cls):
#                 if subcls not in subs:
#                     subs.append(subcls)
#             #print('Look for subclass in: ' + qname)
#             #print(inspect.getmodulename(qname))
#             #pass


#     return subs

# sub_list = []    
# sub_list = explore_package('erd.daq.instrument',Instrument, sub_list)
# print(sub_list)
# for cls in sub_list:
#     print('Instrument subclass: ' + cls.__name__)
