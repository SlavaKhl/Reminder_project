from email.policy import default
from tkinter import *
from tkinter import messagebox as mb
#import pygame
import datetime
import time

window = Tk()
window.title("Напоминание")
window.geometry("400x250")
window.iconbitmap(default="alarm_reminder.ico")

e = Entry(window, font=("Comic Sans MS", 20))
e.pack(pady=20)

btn = Button(window, font=("Comic Sans MS", 20), text="Установить напоминание")
btn.pack()

t_m = Label(window, font=("Comic Sands MS", 20))
t_m.pack(pady=20)

window.mainloop()

