# The code uses the os library to iterate through all files in the specified folder. 
# For each file that ends with .svg, it reads the SVG file using svg2rlg from svglib and renders it to a PNG image using renderPM from reportlab. 
# The resulting PNG image is saved to the "output" folder folder with the same filename as the SVG file.


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
