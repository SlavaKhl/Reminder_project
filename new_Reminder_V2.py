from tkinter import *
from tkinter import ttk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None
music = False  # Переменная для отслеживания проигрывания музыки
reminder_text = None

#def set():
#    global t
#    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)")
#    if rem:
#        try:
#            hour = int(rem.split(":")[0])
#            minute = int(rem.split(":")[1])
#            now = datetime.datetime.now()
#            dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
#            t = dt.timestamp()
#            label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}")
#        except ValueError:
#            mb.showerror("Ошибка", "Неверный формат времени")

#Задание 1.
#Добавьте визуальное напоминание в виде всплывающего окна с текстом напоминания, которое будет отображаться
#в момент срабатывания таймера.Это позволит пользователю не только слышать напоминание, но и видеть
#текстовое сообщение, что может быть особенно полезно, если звук выключен или временно не доступен.
#
#Сохраните текст напоминания в глобальную переменную при его установке.
#При срабатывании напоминания отобразите всплывающее окно с текстом напоминания.

def set():
    global t, reminder_text
    rem_time = sd.askstring("Время напоминания", "Введите время напоминания в формате ЧЧ:ММ (в 24-часовом формате):")
    if rem_time:
        try:
            hour = int(rem_time.split(":")[0])
            minute = int(rem_time.split(":")[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0)
            t = dt.timestamp()
            reminder_text = sd.askstring("Текст напоминания", "Введите текст напоминания:")
            label.config(text=f"Напоминание на {hour:02}:{minute:02} с текстом: {reminder_text}")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            rem_text()
            t = None
    window.after(10000, check)

def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()


def rem_text():
    global reminder_text
    window = Tk()
    window.title("Текст напоминания")
    window.geometry("250x200")
    label = ttk.Label(window, text=f"{reminder_text}")
    label.pack(anchor=CENTER, expand=1)


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")

window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=5)

check()

window.mainloop()
