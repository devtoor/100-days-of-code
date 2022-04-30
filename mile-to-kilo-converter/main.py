from __future__ import annotations

from tkinter import Button
from tkinter import END
from tkinter import Entry
from tkinter import Label
from tkinter import Tk


def miles_to_km():
    km = round(float(miles_input.get()) * 1.609, 3)
    kilometer_result_label.config(text=km)
    miles_input.delete(0, END)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
