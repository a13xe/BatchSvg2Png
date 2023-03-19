import os
import cairosvg

inputFolder = 'input'
outputFolder = 'output'

# The output PNG files should have a size of 1024x1024 pixels with a scale factor of 1. 
# You can adjust these parameters as needed.
outputImgWidth = 1024
outputImgHeight = 1024

# Create the output folder if it doesn't exist
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# Get a list of all SVG files in the input folder
svg_files = [f for f in os.listdir(inputFolder) if f.endswith('.svg')]

# Loop through the SVG files and convert each one to a PNG file with a transparent background
for svg_file in svg_files:
    svg_path = os.path.join(inputFolder, svg_file)
    png_path = os.path.join(outputFolder, os.path.splitext(svg_file)[0] + '.png')
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=outputImgWidth, output_height=outputImgHeight, scale=1)