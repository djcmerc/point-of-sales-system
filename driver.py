import tkinter as tk
import tkinter.font as font

HEIGHT = 750
WIDTH = 1500

root = tk.Tk()
root.state('zoomed')
guiFont = font.Font(family='Helvetica', size=36)
#canvas = tk.Canvas(root, bg='black')
#canvas.pack(fill='both', expand=True)

def initialize_frames():
    menuFrame = tk.Frame(root, bg='red', highlightbackground='black', highlightthickness=8)
    menuFrame.place(relwidth=0.25, relheight=0.25)

    memberFrame = tk.Frame(root, bg='yellow', highlightbackground='black', highlightthickness=8)
    memberFrame.place(relx=0.25, relwidth=0.5, relheight=0.25)

    tabFrame = tk.Frame(root, bg='green', highlightbackground='black', highlightthickness=8)
    tabFrame.place(rely=0.25, relheight=0.1, relwidth=0.75)

    orderFrame = tk.Frame(root, highlightbackground='black', highlightthickness=8)
    orderFrame.place(relx=0.75, relwidth=0.25, relheight=0.85)
    orderListbox = tk.Listbox(orderFrame)
    orderListbox.place(relwidth=1, relheight=0.9)

    orderButtonsFrame = tk.Frame(orderFrame, bg='pink')
    orderButtonsFrame.place(rely=0.9, relwidth=1, relheight=0.1)
    upButton = tk.Button(orderButtonsFrame, text="UP", font=guiFont, bd=5)
    upButton.place(relwidth=(1/3), relheight=1)
    deleteButton = tk.Button(orderButtonsFrame, text="X", font=guiFont, bd=5)
    deleteButton.place(relwidth=(1/3), relheight=1, relx=(1/3))
    downButton = tk.Button(orderButtonsFrame, text="DOWN", font=guiFont, bd=5)
    downButton.place(relwidth=(1/3), relheight=1, relx=(2/3))

    buttonFrame = tk.Frame(root, bg='blue', highlightbackground='black', highlightthickness=8)
    buttonFrame.place(rely=0.35, relwidth=0.75, relheight=0.65)

    totalFrame = tk.Frame(root, bg='pink', highlightbackground='black', highlightthickness=8)
    totalFrame.place(relx=0.75, rely=0.85, relwidth=0.25, relheight=0.15)

    totalButton = tk.Button(totalFrame, text="Total: ", font=guiFont)
    totalButton.place(relwidth=1, relheight=1)

initialize_frames()




root.mainloop()
