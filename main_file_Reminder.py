from email.policy import default
from tkinter import *
from tkinter import messagebox as mb
#import pygame
import datetime
import time

def set_reminder():
    rem_time = e.get()
    if rem_time:
        t_m.config(text="")
        hour, minute = rem_time.split(":")
        full_now_time = datetime.datetime.now()
        remind_time = full_now_time.replace(hour=int(hour), minute=int(minute))
        t_m.config(text=f"Напоминание установлено на {hour}:{minute}")
        t_m.config(fg="green")
    else:
        t_m.config(text="Поле не заполнено", font=("Comic Sans MS", 16))
        t_m.config(fg="red")

window = Tk()
window.title("Напоминание")
window.geometry("400x250")
window.iconbitmap(default="alarm_reminder.ico")

l_e = Label(window, text="Укажите время для напоминания:", font=("Comic Sans MS", 16))
l_e.pack()

e = Entry(window, font=("Comic Sans MS", 20))
e.pack()

btn = Button(window, font=("Comic Sans MS", 20), text="Установить напоминание", command=set_reminder)
btn.pack(pady=20)

t_m = Label(window, font=("Comic Sands MS", 20))
t_m.pack()

window.mainloop()

