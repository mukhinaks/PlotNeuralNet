from warnings import warn
import matplotlib

class Arrow:
    def __init__(self, name, color = 'edgecolor', line_width = 0.5):
        self.name = name
        self.color = color
        self.line_width = line_width

    def to_tex(self):
        tex_code = "\\newcommand{\\" + self.name + \
                "}{\\tikz \\draw[-Stealth,line width=" + str(self.line_width) + \
                "mm,draw=" + self.color + "] (-0.3,0) -- ++(0.3,0);}"
        return tex_code
        #\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]

class ColorScheme:
    def __init__(self):
        super().__init__()
        self.colors = {
            "ConvColor":  "{RGB}{255, 204, 102}",
            "ConvReluColor": "{RGB}{254, 173, 77}",
            "PoolColor": "{RGB}{196, 0, 0}",
            "UnpoolColor": "{RGB}{22, 72, 157}",
            "FCColor": "{RGB}{156, 96, 207}",
            "FCReluColor": "{RGB}{166, 68, 166}",
            "SoftmaxColor": "{RGB}{106, 0, 106}",
            "edgecolor": "{RGB}{60, 60, 60}",
            "Default": "{RGB}{255, 87, 51}",
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
            colors += "\definecolor{" + name + "}" + color + "\n"
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


