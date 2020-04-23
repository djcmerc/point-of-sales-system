import tkinter as tk
import tkinter.font as font

def createButton(master, text, font, w, h, x, bd=5):
    button = tk.Button(master, text=text, font=font, bd=bd)
    button.place(relwidth=w,relheight=h,relx=x)

    return button

def createFrame(master, bg=None, highlightbackground=None, highlightthickness=None, x=0, y=0, w=0, h=0):
    frame = tk.Frame(master, bg=bg, highlightbackground=highlightbackground, highlightthickness=highlightthickness)
    frame.place(relx=x, rely=y, relwidth=w, relheight=h)

    return frame

class MainGUI:
    def __init__(self, master):
        self.master = master
        self.buttonFrame = ButtonFrame(master)
        self.menuFrame = MenuFrame(master)
        self.tabFrame = TabFrame(master)
        self.orderFrame = OrderFrame(master)
        self.orderButtonsFrame = OrderButtonsFrame(self.orderFrame.frame)
        self.totalFrame = TotalFrame(master)
        self.memberFrame = MemberFrame(master)

class ButtonFrame():
    def __init__(self, master):
        self.frame = createFrame(master=master, bg='blue', highlightbackground='black', highlightthickness=8, y=0.35, w=0.75, h=0.65)

class MenuFrame:
    def __init__(self, master):
        self.frame = createFrame(master, bg='red', highlightbackground='black', highlightthickness=8, w=0.25, h=0.25)

class TabFrame:
    def __init__(self, master):
        self.frame = createFrame(master, bg='green', highlightbackground='black', highlightthickness=8,y=0.25, h=0.1, w=0.75)

class OrderFrame:
    def __init__(self, master):
        self.frame = createFrame(master, highlightbackground='black', highlightthickness=8,x=0.75, w=0.25, h=0.85)

        self.orderListbox = tk.Listbox(self.frame)
        self.orderListbox.place(relwidth=1, relheight=0.9)

class OrderButtonsFrame():
    def __init__(self, master):
        self.guiFont = font.Font(family='Helvetica', size=36)

        self.frame = createFrame(master, bg='pink',y=0.9, w=1, h=0.1)

        self.upButton = createButton(self.frame, "UP", self.guiFont, (1/3), 1, 0)

        self.deleteButton = createButton(self.frame, "X", self.guiFont, (1/3), 1, (1/3))

        self.downButton = createButton(self.frame, "DOWN", self.guiFont, (1/3), 1, (2/3))

class MemberFrame:
    def __init__(self, master):
        self.frame = createFrame(master, bg='yellow', highlightbackground='black', highlightthickness=8,x=0.25, w=0.5, h=0.25)

class TotalFrame:
    def __init__(self, master):
        self.guiFont = font.Font(family='Helvetica', size=36)
        self.frame = createFrame(master, bg='pink', highlightbackground='black', highlightthickness=8, x=0.75, y=0.85, w=0.25, h=0.15)

        self.totalButton = createButton(self.frame, "Total: ", self.guiFont, 1, 1, 0)