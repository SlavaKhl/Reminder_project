from email.policy import default
from tkinter import *
from tkinter import messagebox as mb
import pygame
import datetime
import time


def set_reminder():
    global remind_time_second
    rem_time = e.get()
    if rem_time:
        t_m.config(text="")
        hour, minute = rem_time.split(":")
        full_now_time = datetime.datetime.now()
        remind_time_second = full_now_time.replace(hour=int(hour), minute=int(minute)).timestamp()
        t_m.config(text=f"Напоминание установлено на {hour}:{minute}")
        t_m.config(fg="green")
        check_now_time()
    else:
        t_m.config(text="Поле не заполнено", font=("Comic Sans MS", 16))
        t_m.config(fg="red")


def check_now_time():
    global remind_time_second
    now_time_sec = time.time()
    if now_time_sec >= remind_time_second:
        play_music()
        remind_time_second = None
        return
    window.after(1000, check_now_time)

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("5836_pod-zvonok.ru__.mp3")
    pygame.mixer.music.play("")

remind_time_second = None

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

