from PIL import Image

image = Image.open("font.png")

i = 0
for y in range(0, image.height, 12):
    for x in range(0, image.width, 10):
        tile = image.crop((x, y, x + 10, y + 12))
        tile.save(f"font/font-{i}.png")
        i += 1
