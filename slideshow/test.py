from tkinter import Tk, Label, Button
from PIL import ImageTk, Image
import os

folder = "images"
files = os.listdir(folder)
    

class MainGui:
    def __init__(self, master, picture):
        self.current = 0
        self.master = master
        master.title("Python slideshow")
        
        self.label = Label(master, text="Test")
        self.label.pack()
        
        self.back_button = Button(master, text="<", command=self.back)
        self.back_button.pack()
        
        self.forward_button = Button(master, text=">", command=self.forward)
        self.forward_button.pack()
        
        self.image = Label(master, image="")
        self.image.pack(side="bottom", fill="both", expand="yes")
    def back(self):
        if self.current - 1 != -1:
            self.current = self.current - 1
            self.picture("{}/{}".format(folder, files[self.current]))
            
    def forward(self):
        self.picture("{}/{}".format(folder, files[self.current]))
        print(self.picture.image)
        
    def picture(self, picture):
        picture = ImageTk.PhotoImage(Image.open(picture))
        self.image.config(image=picture)


root = Tk()
test = ImageTk.PhotoImage(Image.open("images/logo.png"))
main_window = MainGui(root, test)
root.mainloop()
