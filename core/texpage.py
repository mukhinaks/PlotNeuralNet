from core.style import *
from core.model import Model
import os

class TexPage:
    def __init__(self, texfilespath = '.'):
        super().__init__()
        self.colors = ColorScheme()
        self.arrow = Arrow('midarrow')
        self.model = Model()
        self.path = os.path.join( texfilespath, 'tex-elements/' ).replace('\\', '/') 

    def to_tex(self):
        page = []

        page.append(r"""
            \documentclass[border=8pt, multi, tikz]{standalone} 
            \usepackage{import}
            \subimport{"""+ self.path + r"""}{init}
            \usetikzlibrary{positioning}
            \usetikzlibrary{3d} %for including external image 
            """)

        page.append(self.colors.to_tex())
        page.append(self.arrow.to_tex())
        page.append(r"""
            \begin{document}
            \begin{tikzpicture}
            \tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=edgecolor,opacity=0.7]
            \tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
            """)

        page.extend(self.model.to_tex())

        page.append(r"""
            \end{tikzpicture}
            \end{document}
            """)

        return page

    def generate(self, pathname="file.tex", ):
        with open(pathname, "w") as f: 
            for c in self.to_tex():
               # print(c)
                f.write( c )