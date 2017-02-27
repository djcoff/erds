'''
   Concrete instrument class for TSI 3010 CPC
'''

from erd.daq.instrument.cpc.cpc import CPC

#@Instrument.register
class TSI3010(CPC):
    
    def __init__(self):
        super().__init__()
        self.name = 'TSI 3010'
        self.mfg = 'TSI'
        self.model = '3010'
        print ('Name: ',self.name)
        print ('Type: ',self.type)
        
    def start(self):
        print('Starting...')
        