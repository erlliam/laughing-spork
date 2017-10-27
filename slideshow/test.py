from tkinter import Tk, Label, Button

class MainGui:
	def __init__(self, master):
		self.current = 0
		self.master = master
		master.title("Python slideshow")

		self.label = Label(master, text="Test")
		self.label.pack()

		self.back_button = Button(master, text="<", command=self.back)
		self.back_button.pack()

		self.forward_button = Button(master, text=">", command=self.forward)
		self.forward_button.pack()

	def back(self):
		self.current = self.current - 1
		print(self.current)

	def forward(self):
		self.current = self.current + 1
		print(self.current)


root = Tk()
main_window = MainGui(root)
root.mainloop()
