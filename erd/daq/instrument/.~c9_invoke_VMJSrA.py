'''
instrument.py: 
    define the abstract instrument class that will be inherited by all
    instruments in the erd suite. 
'''

import abc

class Instrument(metaclass=abc.ABC):
    name = None
    type = None
    
    pass
