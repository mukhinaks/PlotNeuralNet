class Legend:
    class LegendElement:
        def __init_subclass__(cls, name, color):
            self.name = name
            self.color = color
            return super().__init_subclass__()

    def __init__(self):
        self.elements = set()
        super().__init__()

    def add_element(self, layer_name, colors):
        elem = LegendElement(layer_name)
        self.elements.add(elem)
