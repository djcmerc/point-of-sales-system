import tkinter as tk

HEIGHT = 750
WIDTH = 1500

root = tk.Tk()
root.state('zoomed')
#canvas = tk.Canvas(root, bg='black')
#canvas.pack(fill='both', expand=True)

def initialize_frames():
    menuFrame = tk.Frame(root, bg='red')
    menuFrame.place(relwidth=0.25, relheight=0.25)

    memberFrame = tk.Frame(root, bg='yellow')
    memberFrame.place(relx=0.25, relwidth=0.5, relheight=0.25)

    tabFrame = tk.Frame(root, bg='green')
    tabFrame.place(rely=0.25, relheight=0.1, relwidth=0.75)

    orderFrame = tk.Frame(root, bg='black')
    orderFrame.place(relx=0.75, relwidth=0.25, relheight=0.85)

    buttonFrame = tk.Frame(root, bg='blue')
    buttonFrame.place(rely=0.35, relwidth=0.75, relheight=0.65)

    totalFrame = tk.Frame(root, bg='pink')
    totalFrame.place(relx=0.75, rely=0.85, relwidth=0.25, relheight=0.15)

initialize_frames()


root.mainloop()
