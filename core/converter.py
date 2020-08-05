import torch
from core.model import *

def from_pytorch(model):
    arch = Model()
    model.apply(init_layer)

    for layer in model.layers:
        arch.addConv("", layer.num_classes, layer.width, layer.height)
    return ""

def init_layer(m):
    if type(m) == torch.nn.Conv2D:
        return ConvLayer()
