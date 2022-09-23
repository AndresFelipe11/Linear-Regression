import tkinter as tk

class GUI:

    def __init__(self):
        self.root = tk.Tk()
    
    def start(self):
        self.root.title("Linear Regression")
        self.root.geometry("750x450")
        self.root.configure(bg="white")

        self.root.mainloop()