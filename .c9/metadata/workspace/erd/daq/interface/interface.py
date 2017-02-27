{"changed":true,"filter":false,"title":"interface.py","tooltip":"/erd/daq/interface/interface.py","value":"from abc import ABCMeta, abstractmethod\nimport asyncio\nfrom erd.daq.daq import DAQ\n\n\"\"\"\nInterface\nAbstract base class for HW Interface between Instrument class and \"hardware\". \nInterface requires:\n   - event loop (asyncio) \n   - configuration (dictionary with hw specific values)\n\"\"\"\n\nclass Interface(DAQ):\n    \n    def __init__(self):\n        super().__init__()\n        self.name = None\n        self.type = None\n        self.loop = None\n        \n        #self.info = InterfaceInfo\n        #self.config = InterfaceConfig\n    \n    @abstractmethod    \n    def open(self):\n        pass\n    \n    @abstractmethod\n    def close(self):\n        pass\n    \n    @abstractmethod\n    def configure(self): #second arg will be config info\n        pass\n    \n    \nclass SerialPort(Interface):\n    \n    def __init__(self):\n        super().__init__(self)\n        \n    def open(self):\n        pass\n    \n    def close(self):\n        pass\n    \n    def configure(self):\n        pass\n    \n    \nclass TCPPort(Interface):\n    \n    def __init__(self):\n        super().__init__()\n        self.reader = None\n        self.writer = None\n        \n    def open(self):\n        #pass\n        self.reader, self.writer = asyncio.open_connection('192.168.86.106', 4002,loop=self.loop)\n    \n    def close(self):\n        pass\n    \n    def configure(self):\n        pass\n    ","undoManager":{"mark":9,"position":100,"stack":[[{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["n"],"id":84}],[{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["i"],"id":85}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["i"],"id":86}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["t"],"id":87}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["t"],"id":88}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["i"],"id":89}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["t"],"id":90}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["_"],"id":91}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["_"],"id":92}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":26},"action":"insert","lines":["()"],"id":93}],[{"start":{"row":57,"column":12},"end":{"row":58,"column":0},"action":"insert","lines":["",""],"id":94},{"start":{"row":58,"column":0},"end":{"row":58,"column":8},"action":"insert","lines":["        "]},{"start":{"row":58,"column":4},"end":{"row":58,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":58,"column":4},"end":{"row":58,"column":8},"action":"insert","lines":["    "],"id":95}],[{"start":{"row":58,"column":8},"end":{"row":58,"column":88},"action":"insert","lines":["reader, writer = await asyncio.open_connection('192.168.86.106', 4002,loop=loop)"],"id":96}],[{"start":{"row":54,"column":26},"end":{"row":55,"column":0},"action":"insert","lines":["",""],"id":97},{"start":{"row":55,"column":0},"end":{"row":55,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":55,"column":8},"end":{"row":55,"column":9},"action":"insert","lines":["s"],"id":98}],[{"start":{"row":55,"column":9},"end":{"row":55,"column":10},"action":"insert","lines":["e"],"id":99}],[{"start":{"row":55,"column":10},"end":{"row":55,"column":11},"action":"insert","lines":["l"],"id":100}],[{"start":{"row":55,"column":11},"end":{"row":55,"column":12},"action":"insert","lines":["f"],"id":101}],[{"start":{"row":55,"column":12},"end":{"row":55,"column":13},"action":"insert","lines":["."],"id":102}],[{"start":{"row":55,"column":13},"end":{"row":55,"column":14},"action":"insert","lines":["r"],"id":103}],[{"start":{"row":55,"column":14},"end":{"row":55,"column":15},"action":"insert","lines":["e"],"id":104}],[{"start":{"row":55,"column":15},"end":{"row":55,"column":16},"action":"insert","lines":["a"],"id":105}],[{"start":{"row":55,"column":16},"end":{"row":55,"column":17},"action":"insert","lines":["d"],"id":106}],[{"start":{"row":55,"column":17},"end":{"row":55,"column":18},"action":"insert","lines":["e"],"id":107}],[{"start":{"row":55,"column":18},"end":{"row":55,"column":19},"action":"insert","lines":["r"],"id":108}],[{"start":{"row":55,"column":19},"end":{"row":55,"column":20},"action":"insert","lines":[" "],"id":109}],[{"start":{"row":55,"column":20},"end":{"row":55,"column":21},"action":"insert","lines":["="],"id":110}],[{"start":{"row":55,"column":21},"end":{"row":55,"column":22},"action":"insert","lines":[" "],"id":111}],[{"start":{"row":55,"column":22},"end":{"row":55,"column":23},"action":"insert","lines":["o"],"id":112}],[{"start":{"row":55,"column":22},"end":{"row":55,"column":23},"action":"remove","lines":["o"],"id":113}],[{"start":{"row":55,"column":22},"end":{"row":55,"column":23},"action":"insert","lines":["N"],"id":114}],[{"start":{"row":55,"column":23},"end":{"row":55,"column":24},"action":"insert","lines":["o"],"id":115}],[{"start":{"row":55,"column":24},"end":{"row":55,"column":25},"action":"insert","lines":["n"],"id":116}],[{"start":{"row":55,"column":25},"end":{"row":55,"column":26},"action":"insert","lines":["e"],"id":117}],[{"start":{"row":55,"column":26},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":118},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":56,"column":8},"end":{"row":56,"column":9},"action":"insert","lines":["s"],"id":119}],[{"start":{"row":56,"column":9},"end":{"row":56,"column":10},"action":"insert","lines":["e"],"id":120}],[{"start":{"row":56,"column":10},"end":{"row":56,"column":11},"action":"insert","lines":["l"],"id":121}],[{"start":{"row":56,"column":10},"end":{"row":56,"column":11},"action":"remove","lines":["l"],"id":122}],[{"start":{"row":56,"column":9},"end":{"row":56,"column":10},"action":"remove","lines":["e"],"id":123}],[{"start":{"row":56,"column":9},"end":{"row":56,"column":10},"action":"insert","lines":["l"],"id":124}],[{"start":{"row":56,"column":10},"end":{"row":56,"column":11},"action":"insert","lines":["e"],"id":125}],[{"start":{"row":56,"column":10},"end":{"row":56,"column":11},"action":"remove","lines":["e"],"id":126}],[{"start":{"row":56,"column":9},"end":{"row":56,"column":10},"action":"remove","lines":["l"],"id":127}],[{"start":{"row":56,"column":9},"end":{"row":56,"column":10},"action":"insert","lines":["e"],"id":128}],[{"start":{"row":56,"column":10},"end":{"row":56,"column":11},"action":"insert","lines":["l"],"id":129}],[{"start":{"row":56,"column":11},"end":{"row":56,"column":12},"action":"insert","lines":["f"],"id":130}],[{"start":{"row":56,"column":11},"end":{"row":56,"column":12},"action":"remove","lines":["f"],"id":131}],[{"start":{"row":56,"column":11},"end":{"row":56,"column":12},"action":"insert","lines":["."],"id":132}],[{"start":{"row":56,"column":11},"end":{"row":56,"column":12},"action":"remove","lines":["."],"id":133}],[{"start":{"row":56,"column":11},"end":{"row":56,"column":12},"action":"insert","lines":["f"],"id":134}],[{"start":{"row":56,"column":12},"end":{"row":56,"column":13},"action":"insert","lines":["."],"id":135}],[{"start":{"row":56,"column":13},"end":{"row":56,"column":14},"action":"insert","lines":["r"],"id":136}],[{"start":{"row":56,"column":13},"end":{"row":56,"column":14},"action":"remove","lines":["r"],"id":137}],[{"start":{"row":56,"column":13},"end":{"row":56,"column":14},"action":"insert","lines":["w"],"id":138}],[{"start":{"row":56,"column":14},"end":{"row":56,"column":15},"action":"insert","lines":["r"],"id":139}],[{"start":{"row":56,"column":15},"end":{"row":56,"column":16},"action":"insert","lines":["i"],"id":140}],[{"start":{"row":56,"column":16},"end":{"row":56,"column":17},"action":"insert","lines":["t"],"id":141}],[{"start":{"row":56,"column":17},"end":{"row":56,"column":18},"action":"insert","lines":["e"],"id":142}],[{"start":{"row":56,"column":18},"end":{"row":56,"column":19},"action":"insert","lines":["r"],"id":143}],[{"start":{"row":56,"column":19},"end":{"row":56,"column":20},"action":"insert","lines":[" "],"id":144}],[{"start":{"row":56,"column":20},"end":{"row":56,"column":21},"action":"insert","lines":["="],"id":145}],[{"start":{"row":56,"column":21},"end":{"row":56,"column":22},"action":"insert","lines":[" "],"id":146}],[{"start":{"row":56,"column":22},"end":{"row":56,"column":23},"action":"insert","lines":["N"],"id":147}],[{"start":{"row":56,"column":23},"end":{"row":56,"column":24},"action":"insert","lines":["o"],"id":148}],[{"start":{"row":56,"column":24},"end":{"row":56,"column":25},"action":"insert","lines":["n"],"id":149}],[{"start":{"row":56,"column":25},"end":{"row":56,"column":26},"action":"insert","lines":["e"],"id":150}],[{"start":{"row":60,"column":30},"end":{"row":60,"column":31},"action":"remove","lines":[" "],"id":151}],[{"start":{"row":60,"column":29},"end":{"row":60,"column":30},"action":"remove","lines":["t"],"id":152}],[{"start":{"row":60,"column":28},"end":{"row":60,"column":29},"action":"remove","lines":["i"],"id":153}],[{"start":{"row":60,"column":27},"end":{"row":60,"column":28},"action":"remove","lines":["a"],"id":154}],[{"start":{"row":60,"column":26},"end":{"row":60,"column":27},"action":"remove","lines":["w"],"id":155}],[{"start":{"row":60,"column":25},"end":{"row":60,"column":26},"action":"remove","lines":["a"],"id":156}],[{"start":{"row":60,"column":77},"end":{"row":60,"column":78},"action":"insert","lines":["s"],"id":157}],[{"start":{"row":60,"column":78},"end":{"row":60,"column":79},"action":"insert","lines":["e"],"id":158}],[{"start":{"row":60,"column":79},"end":{"row":60,"column":80},"action":"insert","lines":["l"],"id":159}],[{"start":{"row":60,"column":80},"end":{"row":60,"column":81},"action":"insert","lines":["f"],"id":160}],[{"start":{"row":60,"column":81},"end":{"row":60,"column":82},"action":"insert","lines":["."],"id":161}],[{"start":{"row":59,"column":8},"end":{"row":59,"column":9},"action":"insert","lines":["#"],"id":162}],[{"start":{"row":60,"column":8},"end":{"row":60,"column":9},"action":"insert","lines":["s"],"id":163}],[{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"insert","lines":["l"],"id":164}],[{"start":{"row":60,"column":10},"end":{"row":60,"column":11},"action":"insert","lines":["e"],"id":165}],[{"start":{"row":60,"column":11},"end":{"row":60,"column":12},"action":"insert","lines":["."],"id":166}],[{"start":{"row":60,"column":11},"end":{"row":60,"column":12},"action":"remove","lines":["."],"id":167}],[{"start":{"row":60,"column":10},"end":{"row":60,"column":11},"action":"remove","lines":["e"],"id":168}],[{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"remove","lines":["l"],"id":169}],[{"start":{"row":60,"column":9},"end":{"row":60,"column":10},"action":"insert","lines":["e"],"id":170}],[{"start":{"row":60,"column":10},"end":{"row":60,"column":11},"action":"insert","lines":["l"],"id":171}],[{"start":{"row":60,"column":11},"end":{"row":60,"column":12},"action":"insert","lines":["f"],"id":172}],[{"start":{"row":60,"column":12},"end":{"row":60,"column":13},"action":"insert","lines":["."],"id":173}],[{"start":{"row":60,"column":21},"end":{"row":60,"column":22},"action":"insert","lines":["s"],"id":174}],[{"start":{"row":60,"column":22},"end":{"row":60,"column":23},"action":"insert","lines":["l"],"id":175}],[{"start":{"row":60,"column":23},"end":{"row":60,"column":24},"action":"insert","lines":["e"],"id":176}],[{"start":{"row":60,"column":24},"end":{"row":60,"column":25},"action":"insert","lines":["f"],"id":177}],[{"start":{"row":60,"column":24},"end":{"row":60,"column":25},"action":"remove","lines":["f"],"id":178}],[{"start":{"row":60,"column":23},"end":{"row":60,"column":24},"action":"remove","lines":["e"],"id":179}],[{"start":{"row":60,"column":22},"end":{"row":60,"column":23},"action":"remove","lines":["l"],"id":180}],[{"start":{"row":60,"column":22},"end":{"row":60,"column":23},"action":"insert","lines":["e"],"id":181}],[{"start":{"row":60,"column":23},"end":{"row":60,"column":24},"action":"insert","lines":["l"],"id":182}],[{"start":{"row":60,"column":24},"end":{"row":60,"column":25},"action":"insert","lines":["f"],"id":183}],[{"start":{"row":60,"column":25},"end":{"row":60,"column":26},"action":"insert","lines":["."],"id":184}]]},"ace":{"folds":[],"scrolltop":525,"scrollleft":0,"selection":{"start":{"row":60,"column":26},"end":{"row":60,"column":26},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1488140107252}