from tkinter import Tk, Label, Button
import PIL
from PIL import *

class MainGui:
	def __init__(self, master, picture):
		self.current = 0
		self.picture = picture
		self.master = master
		master.title("Python slideshow")

		self.label = Label(master, text="Test")
		self.label.pack()

		self.back_button = Button(master, text="<", command=self.back)
		self.back_button.pack()

		self.forward_button = Button(master, text=">", command=self.forward)
		self.forward_button.pack()

		self.image = Label(master, image=self.picture)
		self.image.pack(side="bottom", fill="both", expand="yes")

	def back(self):
		self.current = self.current - 1
		print(self.current)

	def forward(self):
		self.current = self.current + 1
		print(self.current)

	def picture(self, picture):
		self.picture = picture


root = Tk()
test = ImageTk.PhotoImage(Image.open("images/logo.png"))
main_window = MainGui(root, test)
root.mainloop()
