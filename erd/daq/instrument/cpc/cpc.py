from erd.daq.instrument import Instrument


class CPC(Instrument):
    
    def __init__(self):
        super().__init__()
        self.name = 'Generic CPC'
        self.type = 'CPC'
        print ('Name: ',self.name)
        print ('Type: ',self.type)
        
    def start(self):
        print('Starting...')