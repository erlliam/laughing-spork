from tkinter import *

class MainGui:
    def __init__(self, root):
        self.root = root
        root.title("Lagswitch")

        self.start_b = Button(root, text="Start", command=self.start)
        self.stop_b = Button(root, text="Stop", command=self.stop)
        self.timer_t = Label(root, text="Time: 15")

        self.start_b.grid()
        self.stop_b.grid(row=0, column=1)
        self.timer_t.grid(row=1, columnspan=2)


    def start(self):
        pass

    def stop(self):
        pass

root = Tk()
window = MainGui(root)
root.mainloop()
