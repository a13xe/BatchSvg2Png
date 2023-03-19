MultipleSvg2Png
=======================================================================

The code uses the os library to iterate through all files in the specified folder.
For each file that ends with .svg, it reads the SVG file using `svg2rlg` from `svglib` and renders it to a PNG image using `renderPM` from `reportlab`. 
The resulting PNG image is saved to the "output" folder folder with the same filename as the SVG file.
