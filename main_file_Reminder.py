from tkinter import *
from tkinter import messagebox as mb
#import pygame
import datetime
import time

window = Tk()
window.title("Напоминание")
window.geometry("400x250")

e = Entry(window, font=("Arial", 20))
e.pack(pady=20)

btn = Button(window, font=("Arial", 20), text="Установить напоминание")
btn.pack()

window.mainloop()

