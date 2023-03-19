import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

inputFolderPath = 'input/'
outputFolderPath = 'output/'

for filename in os.listdir(inputFolderPath):
    if filename.endswith('.svg'):
        svg_file = os.path.join(inputFolderPath, filename)
        drawing = svg2rlg(svg_file)
        png_file = os.path.join(outputFolderPath, filename[:-4] + '.png')
        renderPM.drawToFile(drawing, png_file, fmt='PNG')