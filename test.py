import sys
sys.path.append('..')

from core.texpage import *
import subprocess

# Define tex page
page = TexPage()

# Add layers to model
page.model.addLayer('Conv2D','c1', 2, 64, 64)
page.model.addLayer('MaxPool', 'pool1', 2, 32, 32)
page.model.addLayer('Conv2D', 'c2', 2, 32, 32)
page.model.addLayer('MaxPool', 'pool2', 1, 28, 28)
page.model.addLayer('SoftMax', 'soft', 1, 28, 28)
page.model.addConnection('pool1', 'c2')
page.model.addConnection('pool2', 'soft')

# Create tex file
namefile = str(sys.argv[0]).split('.')[0]
page.generate(namefile + '.tex' )

# Run tex to get pdf
return_value = subprocess.call(['pdflatex', namefile + '.tex'], shell=False)

# net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
# net.apply(init_weights)

