# from .navigate import Navigate
# import sys
# sys.path.append('/home/derek/python/erds/erd')

# for line in sys.path: print(line)

from erd.daq.instrument.navigate.navigate import Navigate

class MagCompass(Navigate):
    
    def __init__(self):
        super().__init__()
        self.type = 'Compass'
        
    def start(self):
        pass
    
    def handle(self,msg):
        pass
    
    def parse(self,msg):
        pass

# def test_path():
    
#     print('****')
#     for line in sys.path: print(line)
    
# if __name__ == "__main__":
    
#     import sys
#     sys.path.append('/home/derek/python/erds/erd/daq')
    
#     for line in sys.path: print(line)
    
#     import asyncio
#     #from ...interface.interface import TCPPort
#     #from daq.interface.interface import TCPPort
    
#     test_path()

#     import instrument
#     #from daq.instrument.cpc.tsicpc import TSI3010
    
#     #async def run_client(message, loop):
#     #    await tcp_echo_client(message, loop) 

#     # loop = asyncio.get_event_loop()
#     # task = asyncio.ensure_future(run_client(message,loop))

#     # try:
#     #     #loop.run_forever()
#     #     #loop.run_until_complete(tcp_echo_client(message, loop))
#     #     loop.run_until_complete(asyncio.wait([task,]))
#     # except KeyboardInterrupt:
#     #      #pass
#     #      task.cancel()
#     #      loop.run_forever()
#     # #     task.exception()
#     # #    loop.stop()
#     # finally:
#     #     #loop.run_until_complete(loop.shutdown_asyncgens())
#     #     print('stopping loop...')
#     #     loop.stop()
