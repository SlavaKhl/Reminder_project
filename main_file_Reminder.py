from email.policy import default
from tkinter import *
from tkinter import messagebox as mb
import pygame
import datetime
import time


def set_reminder():
    global remind_time_second, is_rem
    rem_time = e.get()
    if rem_time:
        t_m.config(text="")
        hour, minute = rem_time.split(":")
        full_now_time = datetime.datetime.now()
        remind_time_second = full_now_time.replace(hour=int(hour), minute=int(minute), second=0).timestamp()
        t_m.config(text=f"Напоминание установлено на {hour}:{minute}")
        t_m.config(fg="green", font=("Comic Sans MS", 16))
        is_rem = True
        check_now_time()
        e.delete(0, END)
    else:
        t_m.config(text="Поле не заполнено", font=("Comic Sans MS", 16))
        t_m.config(fg="red")


def check_now_time():
    global remind_time_second, is_rem
    if not is_rem:
        t_m.config(text="Напоминание отменено")
        return
    now_time_sec = time.time()
    if now_time_sec >= remind_time_second:
        play_music()
        remind_time_second = None
        return
    window.after(1000, check_now_time)

def play_music():
    global is_music
    pygame.mixer.init()
    pygame.mixer.music.load("5836_pod-zvonok.ru__.mp3")
    pygame.mixer.music.play()
    t_m.config(text="Напоминание сработало")
    is_music = True


def stop_music():
    global is_music
    if is_music:
        pygame.mixer.music.stop()
        is_music = False
        t_m.config(text="Напоминание завершено")


def cancel_reminder():
    global is_rem
    if is_rem:
        is_rem = False


is_rem =False
is_music = False
remind_time_second = None

window = Tk()
window.title("Напоминание")
window.geometry("470x300")
window.iconbitmap(default="alarm_reminder.ico")

l_e = Label(window, text="Укажите время для напоминания:", font=("Comic Sans MS", 16))
l_e.pack()

e = Entry(window, font=("Comic Sans MS", 20))
e.pack()

f = Frame(window)
f.pack(pady=10)

btn = Button(f, font=("Comic Sans MS", 14), text="Установить напоминание", command=set_reminder)
btn.pack(side=LEFT)
btn = Button(f, font=("Comic Sans MS", 14), text="Остановить музыку", command=stop_music)
btn.pack(side=LEFT)

btn = Button(window, font=("Comic Sans MS", 14), text="Отменить напоминание", command=cancel_reminder)
btn.pack()

t_m = Label(window, font=("Comic Sands MS", 20))
t_m.pack()

window.mainloop()

