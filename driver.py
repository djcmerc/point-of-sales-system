import tkinter as tk
import tkinter.font as font
from frames import MainGUI

#HEIGHT = 750
#WIDTH = 1500

root = tk.Tk()
root.state('zoomed')
mainGUI = MainGUI(root)
#guiFont = font.Font(family='Helvetica', size=36)
#canvas = tk.Canvas(root, bg='black')
#canvas.pack(fill='both', expand=True)

root.mainloop()
