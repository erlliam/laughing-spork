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

        self.back_button = Button(root, text="<--", command=self.back)
        self.back_button.grid(row=1)

        self.forward_button = Button(root, text="-->", command=self.forward)
        self.forward_button.grid(row=1)
        
        self.select_directory = Button(root, text="Select directory", command=self.directory)
        self.select_directory.grid(row=1) 

        self.image = Label(root)
        self.image.config()
        self.image.grid(row=0)

    def back(self):
        if self.index - 1 >= 0:
            self.index = self.index - 1
            self.change_picture("{}{}".format(folder, files[self.index]))
    def forward(self):
        if self.index + 1 <= len(files) - 1:
            self.index = self.index + 1
            self.change_picture("{}{}".format(folder, files[self.index]))

    def directory(self):
        pass

    def change_picture(self, picture):
        picture = Image.open(picture)
        picture.thumbnail(size)
        picture = ImageTk.PhotoImage(picture)
        self.image.config(image=picture, height=640, width=480)
        self.image.image = picture


root = Tk()
#root.resizable(width=False, height=False)
window = MainGui(root)
root.mainloop()
