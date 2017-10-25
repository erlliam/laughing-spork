from PIL import Image
import os, sys, time

size = (640, 480)
folder = os.path.abspath("images")

for image in os.listdir(folder):
	p = Image.open("{}/{}".format(folder, image))
	p.thumbnail(size)
	p.show()
	time.sleep(2)

