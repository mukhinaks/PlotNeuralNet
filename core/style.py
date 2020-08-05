from warnings import warn
import matplotlib

class Arrow:
    def __init__(self, name, color = 'edgecolor', line_width = 0.5):
        self.name = name
        self.color = color
        self.line_width = line_width

    def to_tex(self):
        tex_code = "\\newcommand{\\" + self.name + \
                "}{\\tikz \draw[-Stealth,line width=" + str(self.line_width) + \
                "mm,draw=\\" + self.color + "] (-0.3,0) -- ++(0.3,0);}"
        return tex_code

class ColorScheme:
    def __init__(self):
        super().__init__()
        self.colors = {
            "ConvColor":  (0, "{rgb:yellow,5;red,2.5;white,5}"),
            "ConvReluColor": (0, "{rgb:yellow,5;red,5;white,5}"),
            "PoolColor": (0, "{rgb:red,1;black,0.3}"),
            "UnpoolColor": (0, "{rgb:blue,2;green,1;black,0.3}"),
            "FcColor": (0, "{rgb:blue,5;red,2.5;white,5}"),
            "FcReluColor": (0, "{rgb:blue,5;red,5;white,4}"),
            "SoftmaxColor": (0, "{rgb:magenta,5;black,7}"),  
            "edgecolor": (0, "{rgb:blue,4;red,1;green,3;black,3}"),
            "Default": (1, "{RGB}{255, 87, 51}"),
        }

    def add_color(self, color_name, color):
        if color_name in self.colors:
            warn('Already existing colour will be changed. Old value: ' + self.colors[color_name], RuntimeWarning)
            self.colors[color_name] = self.__color_to_tex__(color)
        else:
            self.colors[color_name] = self.__color_to_tex__(color)

    def to_tex(self):
        colors = ""
        for name, color in self.colors.items():
            if color[0] == 0:
                colors += "\def\\" + name + color[1] + "\n"
            else:
                colors += "\definecolor{" + name + "}" + color[1] + "\n"
        return colors

    def get_color(self, color_name = None):
        if color_name in self.colors:
            return self.colors[color_name]
        else:
            return self.colors['Default']

    def __color_to_tex__(self, color):
        rgb_color = matplotlib.colors.to_rgb(color)
        tex_color = '{RGB}' + '{' + ','.join( rgb_color) + '}'
        return tex_color


class CaptionStyle:
    def __init__(self):
        super().__init__()
        self.fontsize = 16
        self.position = 'center'
        self.style = 'bold'

    def to_tex(self, caption_text):
        return caption_text


