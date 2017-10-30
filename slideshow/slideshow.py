from tkinter import *
import os
from PIL import ImageTk, Image

size = (640, 480)

folder = "images/"
files = os.listdir(folder)

class MainGui:
    def __init__(self, root):
        self.index = -1
        self.root = root
        root.title("Slideshow")

        self.image = Label(root)
        self.image.pack()

        self.back_button = Button(root, text="<--", command=self.back)
        self.back_button.pack(side=LEFT)

        self.forward_button = Button(root, text="-->", command=self.forward)
        self.forward_button.pack(side=RIGHT)

    def back(self):
        if self.index - 1 >= 0:
            self.index = self.index - 1
            self.change_picture("{}{}".format(folder, files[self.index]))
    def forward(self):
        if self.index + 1 <= len(files) - 1:
            self.index = self.index + 1
            self.change_picture("{}{}".format(folder, files[self.index]))

    def change_picture(self, picture):
        picture = Image.open(picture)
        picture.thumbnail(size)
        picture = ImageTk.PhotoImage(picture)
        self.image.config(image=picture)
        self.image.image = picture


root = Tk()

window = MainGui(root)
root.mainloop()
