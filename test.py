import tkinter as tk

HEIGHT = 750
WIDTH = 1500

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

"""
searchFrame = tk.Frame(canvas, bg='red')
searchFrame.grid(row=0, column=0)

button = tk.Button(searchFrame, text="test")
button.place(width=10, height=10)

loginFrame = tk.Frame(canvas, bg='green')
loginFrame.grid(row=0, column=1)

manualFrame = tk.Frame(canvas, bg='yellow')
manualFrame.grid(row=0, column=2)

memberFrame = tk.Frame(canvas, bg='black')
memberFrame.grid(row=0, column=3, rowspan=2)
"""

buttonFrame = tk.Frame(root, bg='blue')
buttonFrame.place(rely=0.25, relwidth=0.7, relheight=0.75)

root.mainloop()
