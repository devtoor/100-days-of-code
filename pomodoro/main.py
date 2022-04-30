from __future__ import annotations

from tkinter import Button
from tkinter import Canvas
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
lap = 0
timer = ""


def reset_timer():
    global lap
    if timer:
        window.after_cancel(timer)
    head_label.config(text="Timer", fg=RED)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    lap = 0


def start_timer():
    global lap
    lap += 1
    if lap == 8:
        head_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif lap % 2 == 0:
        head_label.config(text="Break", fg=RED)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        head_label.config(text="Work", fg=YELLOW)
        count_down(WORK_MIN * 60)


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if lap % 2 == 0:
            check_label.config(text=f"{check_label.cget('text') + '✔'}")


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

head_label = Label(text="Timer", fg=RED, bg=GREEN, font=(FONT_NAME, 50, "normal"))
head_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold"),
)
canvas.grid(column=1, row=1)

start_button = Button(
    text="Start",
    highlightthickness=0,
    bd=0,
    pady=0,
    padx=0,
    command=start_timer,
)
start_button.grid(column=0, row=2)

reset_button = Button(
    text="Reset",
    highlightthickness=0,
    bd=0,
    pady=0,
    padx=0,
    command=reset_timer,
)
reset_button.grid(column=2, row=2)

check_label = Label(fg=RED, bg=GREEN)
check_label.grid(column=1, row=3)

window.mainloop()
