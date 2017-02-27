import sys
#import erd
#from erd.daq import *
#from erd.daq.instrument.cpc.tsicpc import TSI3010
from erd.daq.interface.interface import TCPPort
from erd.daq.instrument.cpc.tsicpc import TSI3010

import asyncio

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
    
 if __name__ == "__main__":

    async def run_client(message, loop):
        await tcp_echo_client(message, loop) 

    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(run_client(message,loop))

    try:
        #loop.run_forever()
        #loop.run_until_complete(tcp_echo_client(message, loop))
        loop.run_until_complete(asyncio.wait([task,]))
    except KeyboardInterrupt:
         #pass
         task.cancel()
         loop.run_forever()
    #     task.exception()
    #    loop.stop()
    finally:
        #loop.run_until_complete(loop.shutdown_asyncgens())
        print('stopping loop...')
        loop.stop()
