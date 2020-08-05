from core.style import ColorScheme

class BaseLayer:
    def __init__(self):
        super().__init__()
        self.name = ""
        self.width = 10
        self.height= 10
        self.depth = 10
        self.caption=""
        self.xlabel=""
        self.ylabel = ""
        self.zlabel=""
        self.fill="Default"
        self.opacity=0.6
        self.offset_from_previous_layer = (0,0,0)
        self.position_of_previous_layer = (0,0,0)

    def tex_code(self):
        tex_code = "\\pic[shift={" + str(self.offset_from_previous_layer) + \
            "}] at " +  \
            str(self.position_of_previous_layer) + """ 
            {Box={
                name=""" + self.name +""",
                caption="""+ self.caption +""",
                xlabel={{"""+ self.xlabel +""", }},
                ylabel="""+ self.ylabel +""",
                zlabel="""+ self.zlabel +""",
                fill="""+ self.fill +""",
                opacity="""+ str(self.opacity) +""",
                height="""+ str(self.height) +""",
                width="""+ str(self.width) +""",
                depth="""+ str(self.depth) +"""
                }
            };
        """
        return tex_code

class ConvLayer(BaseLayer):
    def __init__(self):
        super().__init__()
        self.fill = "ConvColor"

class FCLayer(BaseLayer):
    def __init__(self):
        super().__init__()
        self.fill = "FCColor"

class SoftmaxLayer(BaseLayer):
    def __init__(self):
        super().__init__()
        self.fill = "SoftmaxColor"

class PoolLayer(BaseLayer):
    def __init__(self):
        super().__init__()
        self.fill = "PoolColor"