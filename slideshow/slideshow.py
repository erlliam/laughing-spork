from tkinter import *
import os
from PIL import ImageTk, Image

size = (640, 480)

folder = "images/"
test = os.listdir(folder)

class MainGui:
    def __init__(self, root):
        self.root = root
        root.title("Slideshow")

        self.image = Label(root)
        self.image.pack()

        self.back_button = Button(root, text="<--", command=self.back)
        self.back_button.pack(side=LEFT)

        self.forward_button = Button(root, text="-->", command=self.forward)
        self.forward_button.pack(side=RIGHT)

    def back(self):
        pass

    def forward(self):
        pass

    def change_picture(self, picture):
        picture = ImageTk.PhotoImage(Image.open(picture))
        self.image.config(image=picture)
        self.image.image = picture


root = Tk()

window = MainGui(root)
print(test[0])
print(len(test)-1)
root.mainloop()
