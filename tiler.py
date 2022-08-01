# write a python program to divide a image file equally into row by column tiles
# take command-line arguments: file path, row, column using argparse
# save each tile in a separate image file

# example: python split_image.py images/beach.jpg 2 2
# output: images/beach_split_0.jpg, images/beach_split_1.jpg, images/beach_split_2.jpg, images/beach_split_3.jpg

# example: python split_image.py images/beach.jpg 3 4
# output: images/beach_split_0.jpg, images/beach_split_1.jpg, images/beach_split_2.jpg, images/beach_split_3.jpg, images/beach_split_4.jpg, images/beach_split_5.jpg, images/beach_split_6.jpg, images/beach_split_7.jpg, images/beach_split_8.jpg, images/beach_split_9.jpg, images/beach_split_10.jpg, images/beach_split_11.jpg

# Use the numpy library
# import numpy as np
# Use the argparse library
import argparse

# Use matplotlib for display
import matplotlib.pyplot as plt

# Use the skimage library to load the image
from skimage import io

# Create an argparse object
parser = argparse.ArgumentParser(description="Split the image")
# Add the arguments
parser.add_argument("--image", help="Path to the image", required=True)
parser.add_argument("--rows", help="No. of rows", required=True)
parser.add_argument("--columns", help="No. of columns", required=True)
# Parse the arguments
args = parser.parse_args()

# Read the image
img = io.imread(args.image)
# Get the dimensions of the image
height, width, channels = img.shape
# Convert it to grayscale if it has multiple channels
if channels == 3:
    img = io.imread(args.image, as_gray=True)

# Save the tile
def save_tile(tile, tile_no):
    # Define a name for each tile
    img_title = (
        "images/"
        + args.image.split("/")[1].split(".")[0]
        + "_split_"
        + str(tile_no)
        + ".jpg"
    )
    # Save the tile
    io.imsave(img_title, tile)


# Divide it into tiles
tile_height = height // int(args.rows)
tile_width = width // int(args.columns)
# Initialize the tile number
tile_no = 0
# Iterate over the image
for i in range(0, height, tile_height):
    for j in range(0, width, tile_width):
        # Crop the image
        tile = img[i : i + tile_height, j : j + tile_width]
        # Save the tile
        save_tile(tile, tile_no)
        # Increment the tile number
        tile_no += 1

# Save the original image
img_title = "images/" + args.image.split("/")[1]
# Save the tile
io.imsave(img_title, img)

# Display the tile
plt.imshow(img, cmap="gray", interpolation="bicubic")
# Don't autoscale the axes
plt.axis("off")
# Show the plot
plt.show()
