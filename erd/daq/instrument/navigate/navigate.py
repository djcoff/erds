#from ..instrument import Instrument
from erd.daq.instrument.instrument import Instrument

class Navigate(Instrument):
    
    def __init__(self):
        super().__init__()
        self.name = 'Generic Navigation'
        self.type = 'Navigation'

    def start(self):
        print('Starting...')