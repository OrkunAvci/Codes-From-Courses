import tkinter

def print_input(event):
	print(entry.get())

def reset(event):
	str_input = entry.get()
	entry.delete(0, tkinter.END)
	entry.insert(0, f"Input taken was: {str_input}")

window = tkinter.Tk()
greeting = tkinter.Label(text="Hello, Tkinter", foreground="white", background="#34A2FE", width=100, height=25)   #   Or just fg= and bg=
greeting.pack()

entry = tkinter.Entry(fg="black", bg="white", width=50)
entry.bind("<Return>", print_input)
entry.pack()

button = tkinter.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow")
button.bind("<Button>", reset)
button.pack()

window.mainloop()
