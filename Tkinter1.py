# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:14:59 2023

@author: fmezai
"""

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hola a todos en el mundo!").grid(column=0, row=0)
ttk.Button(frm, text="Ingresar", command=root.destroy).grid(column=3, row=0)

ttk.Label(frm, text="Fer").grid(column=0, row=70)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=70)


root.mainloop()

