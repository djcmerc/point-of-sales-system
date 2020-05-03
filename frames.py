import tkinter as tk
import tkinter.font as font

# Global functions used to create different elements of the UI
def createButton(master, text, font, w, h, x, y=0, fx = None, id = None, bd=5):
    button = tk.Button(master, text=text, font=font, command=lambda:fx(id), bd=bd)
    button.place(relwidth=w,relheight=h,relx=x,rely=y)

    return button

def createButtonList(master, menu, font, command, bd=5):
    buttons = []
    itemNames = []
    for name in menu:
        itemNames.append(name)
    for i in range(0, 6):
        buttons.append(createButton(master, itemNames[i], font, (1/6), (1/4), (i * 1/6), fx=command, id=i))

    return buttons

def createFrame(master, bg=None, highlightbackground=None, highlightthickness=None, x=0, y=0, w=0, h=0):
    frame = tk.Frame(master, bg=bg, highlightbackground=highlightbackground, highlightthickness=highlightthickness)
    frame.place(relx=x, rely=y, relwidth=w, relheight=h)

    return frame

def createLabel(master, text, font, w, h, y):
    label = tk.Label(master, text=text, font=font)
    label.place(relwidth=w, relheight=h, rely=y)

    return label

class ButtonFrame():
    def __init__(self, master, menu, listbox, addToOrder, updateTotal, getTotal):
        
        def buttonClick(id):
            addToOrder(list(menu.keys())[id], listbox)
            updateTotal(getTotal)

        self.guiFont = font.Font(family='Helvetica', size=18)
        self.frame = createFrame(master=master, bg='blue', highlightbackground='black', highlightthickness=8, y=0.35, w=0.75, h=0.65)

        self.buttons = createButtonList(master=self.frame, font=self.guiFont, menu=menu, command=buttonClick)

# MainGUI class which encompasses all other elements in the GUI
class MainGUI:
    def __init__(self, master):
        self.master = master
        self.orderHandler = OrderHandler()
        self.menuFrame = MenuFrame(master)
        self.tabFrame = TabFrame(master)
        self.totalFrame = TotalFrame(master)
        self.memberFrame = MemberFrame(master)
        self.orderFrame = OrderFrame(master)
        self.buttonFrame = ButtonFrame(master, self.orderHandler.menu, self.orderFrame.orderListbox, self.orderHandler.addToOrder, self.totalFrame.updateTotal, 
            self.orderHandler.getTotal)

class MemberFrame:
    def __init__(self, master):
        self.buttonFont = font.Font(family='Helvetica', size=18)
        self.labelFont = font.Font(family='Helvetica', size=12)
        self.frame = createFrame(master, bg='yellow', highlightbackground='black', highlightthickness=8,x=0.25, w=0.5, h=0.25)

        self.convertButton = createButton(self.frame, text="Convert Points", font=self.buttonFont, w=0.5, h=0.2, x=0, y=0.8)
        self.infoButton = createButton(self.frame, text="Additional Information", font=self.buttonFont, w=0.5, h=0.2, x=0.5, y=0.8)

        self.nameLabel = createLabel(self.frame, text="Member Name: ", font=self.labelFont, w=1, h=0.2, y=0)
        self.tierLabel = createLabel(self.frame, text="Membership Tier: ", font=self.labelFont, w=1, h=0.2, y=0.2)
        self.ptsLabel = createLabel(self.frame, text="Points: ", font=self.labelFont, w=1, h=0.2, y=0.4)
        self.ptsNextLabel = createLabel(self.frame, text="Points to next reward: ", font=self.labelFont, w=1, h=0.2, y=0.6)

class MenuFrame:
    def __init__(self, master):
        self.frame = createFrame(master, bg='red', highlightbackground='black', highlightthickness=8, w=0.25, h=0.25)

        self.loginLabel = createLabel(self.frame, text="User: ", font=font.Font(family='Helvetica', size=12), w=1, h=0.2, y=0)

        self.menuButton = createButton(self.frame, text="Menu", font=font.Font(family='Helvetica', size=16), w=0.5, h=0.2, x=0.25, y=0.55)

class OrderFrame:
    def __init__(self, master):
        self.frame = createFrame(master, highlightbackground='black', highlightthickness=8,x=0.75, w=0.25, h=0.85)
        self.orderFont = font.Font(family='Helvetica', size=18)
        self.buttonFont = font.Font(family='Helvetica', size=36)

        self.orderListbox = tk.Listbox(self.frame, font=self.orderFont)
        self.orderListbox.place(relwidth=1, relheight=0.9)

        self.upButton = createButton(self.frame, "UP", self.buttonFont, (1/3), 0.1, 0, 0.9)

        self.deleteButton = createButton(self.frame, "DEL", self.buttonFont, (1/3), 0.1, (1/3), 0.9)

        self.downButton = createButton(self.frame, "DOWN", self.buttonFont, (1/3), 0.1, (2/3), 0.9)

class OrderHandler:
    def __init__(self):
        self.menu = {"Combo #1": 14.59, "Combo #2": 20.79, "Combo #3": 13.09, "Combo #4": 15.69, "Combo #5": 15.69, "Combo #6": 14.59}
        self.order = {}
        self.total = 0

    def addToOrder(self, item, listbox):
        if item in self.order: 
            self.order[item] += 1
            listbox.delete(0, "end")
            for item in self.order:
                listbox.insert("end", "{0} ({1}) - ${2:.2f}".format(item, self.order[item], self.order[item] * self.menu[item]))
        else: 
            self.order[item] = 1
            listbox.insert("end", "{0} ({1}) - ${2:.2f}".format(item, self.order[item], self.order[item] * self.menu[item]))
            

        self.total += self.menu[item]
        print(self.order, self.total)

    def getTotal(self):
        return self.total

class TabFrame:
    def __init__(self, master):
        self.tabNames = ["Main", "Candy/Ice Cream", "Hot Food"]
        self.guiFont = font.Font(family='Helvetica', size=18)
        self.frame = createFrame(master, bg='#99ffff', highlightbackground='black', highlightthickness=8,y=0.25, h=0.1, w=0.75)

        self.mainTab = createButton(self.frame, self.tabNames[0], self.guiFont, w=(1/3), h=1, x=0)
        self.candyTab = createButton(self.frame, self.tabNames[1], self.guiFont, w=(1/3), h=1, x=(1/3))
        self.hotFoodTab = createButton(self.frame, self.tabNames[2], self.guiFont, w=(1/3), h=1, x=(2/3))

class TotalFrame:
    def __init__(self, master):
        self.guiFont = font.Font(family='Helvetica', size=36)
        self.frame = createFrame(master, bg='pink', highlightbackground='black', highlightthickness=8, x=0.75, y=0.85, w=0.25, h=0.15)

        self.totalButton = createButton(self.frame, "Total: $0.00", self.guiFont, 1, 1, 0)

    def updateTotal(self, getTotal):
        self.totalButton.config(text="Total: ${0:.2f}".format(getTotal()))
