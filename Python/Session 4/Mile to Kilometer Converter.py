import tkinter

def convert_mile(event):
	miles = int(mile.get())
	kilometer.delete(0, tkinter.END)
	kilometer.insert(0, str(miles * 1.6))

def convert_kilometer(event):
	kilometers = int(kilometer.get())
	mile.delete(0, tkinter.END)
	mile.insert(0, str(kilometers / 1.6))

window = tkinter.Tk()

instrunctions = tkinter.Label(text="Enter a number and press Enter to convert it to the other.")

miles_label = tkinter.Label(text="Mile:")

mile = tkinter.Entry(width=100)
mile.bind("<Return>", convert_mile)

kilometer_label = tkinter.Label(text="Kilometer:")

kilometer = tkinter.Entry(width=100)
kilometer.bind("<Return>", convert_kilometer)

instrunctions.grid(row=0, column=0)
miles_label.grid(row=1, column=0)
mile.grid(row=1, column=1)
kilometer_label.grid(row=2, column=0)
kilometer.grid(row=2, column=1)

window.mainloop()
