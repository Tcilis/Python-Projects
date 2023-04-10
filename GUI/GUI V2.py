import tkinter as tk

class MyGUI:
    
    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=("Courier", 18))
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root, height=5, font=("Courier", 16))
        self.textbox.pack(padx=10, pady=10)

        self.checkstate = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text=("Show message box"), font=("Courier", 16) , variable = self.checkstate)
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root , text=("Show Message") , font = ("Courier", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10 )

        self.root.mainloop()
    
    def show_message(self):
        print("Hello World")

MyGUI()