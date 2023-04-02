import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Learning GUI in PYTHON!")

label = tk.Label(root, text="Hello there!", font=("Courier", 24))
label.pack(padx=20, pady=30)

textbox = tk.Text(root, height=(3), font=("Courier", 15))
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight= 1)
buttonframe.columnconfigure(1, weight= 1)
buttonframe.columnconfigure(2, weight= 1)

btn1 = tk.Button(buttonframe, text=("1"), font=("Courier", 20))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text=("2"), font=("Courier", 20))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text=("3"), font=("Courier", 20))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text=("4"), font=("Courier", 20))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text=("5"), font=("Courier", 20))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text=("6"), font=("Courier", 20))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

freerambutton = tk.Checkbutton(root, text=("I Agree to download free ram"), font=("Courier", 15))
freerambutton.place(y=450)

root.mainloop()