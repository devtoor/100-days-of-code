from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)
    random_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    random_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    random_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password_list = random_letters + random_symbols + random_numbers
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    if len(website_entry.get()) > 0 and len(username_entry.get()) > 0 and len(password_entry.get()) > 0:
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        masked_password = ""
        for _ in password:
            masked_password += "*"
        if messagebox.askokcancel(title=website, message=f"Details: {website}\nUsername: {username}\n"
                                                         f"Password: {masked_password}\nSave?"):
            with open("password.csv", mode="a") as file:
                file.write(f"{website},{username},{password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

Label(text="Website:").grid(column=0, row=1, sticky="e")
Label(text="Email/Username:").grid(column=0, row=2, sticky="e")
Label(text="Password:").grid(column=0, row=3, sticky="e")

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "test@example.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
