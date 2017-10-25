from PIL import Image
import os

picture = Image.open("/home/mint/Pictures/test/1.jpeg")
picture.thumbnail((1280, 720))
picture.show()
