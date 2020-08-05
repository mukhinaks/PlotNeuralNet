from core.layers import *
from collections import OrderedDict
from core.style import Arrow

available_layers = {
    'Conv2D': ConvLayer,
    'MaxPool': PoolLayer,
    'AvgPool': PoolLayer,
    'SoftMax': SoftmaxLayer,
    'Linear': FCLayer,
}

class Model:
    def __init__(self):
        super().__init__()
        self.layers = OrderedDict()
        self.connections = []

    def addLayer(self, layertype, name, width, height, depth, autoPosition = True):
        try:
            layer = available_layers[layertype]()
        except:
            layer = BaseLayer()

        layer.width = width
        layer.height = height
        layer.depth = depth
        layer.name = name
        layer.xlabel=""
        layer.ylabel = ""
        layer.zlabel=""

        if autoPosition:
            if len(self.layers) > 0:
                key = next(reversed(self.layers))
                layer.position_of_previous_layer = '(' + key + '-east)'
                if layertype == 'MaxPool' or layertype == 'AvgPool':
                    layer.offset_from_previous_layer = (0,0,0)
                else:
                    layer.offset_from_previous_layer = (1,0,0)
        
        self.layers[name] = layer

    def addCaptionToLayer(self, layer_name, caption):
        return

    def addConnection(self, first, second):
        if first in self.layers:
            if second in self.layers:
                self.connections.append( (first, second) )
            else:
                AssertionError(second + 'layer is not defined!')
        else:
            AssertionError(first + 'layer is not defined!')

    def to_tex(self):
        tex_code = []
        for x in self.layers.values():    
            tex_code.append(x.tex_code()) 

        for x,y in self.connections:
            tex_code.append(r"""
                    \draw [connection]  ("""+x+"""-east)    -- node {\midarrow} ("""+y+"""-west);
                    """)
        return tex_code

