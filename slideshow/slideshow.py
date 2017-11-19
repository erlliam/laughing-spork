from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image

size = (640, 480)

folder = ""


class MainGui:
    def __init__(self, root):
        self.root = root
        root.title("Slideshow")

        self.back_button = Button(root, text="<--", command=self.back)

        self.forward_button = Button(root, text="-->", command=self.forward)
        
        self.select_directory = Button(root, text="Select directory", command=self.directory)

        self.image = Label(root)


        self.back_button.pack(side=LEFT)
        self.select_directory.pack(side=LEFT)
        self.forward_button.pack(side=LEFT)
        self.image.pack(side=LEFT)
    def back(self):
        if self.index - 1 >= 0:
            self.index = self.index - 1
            self.change_picture("{}/{}".format(self.folder, self.files[self.index]))
    def forward(self):
        if self.index + 1 <= len(self.files) - 1:
            self.index = self.index + 1
            self.change_picture("{}/{}".format(self.folder, self.files[self.index]))

    def directory(self):
        self.folder = filedialog.askdirectory()
        self.files = os.listdir(self.folder)
        self.index = -1
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
