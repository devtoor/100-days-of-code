from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
        website = website_entry.get().title()
        username = username_entry.get()
        password = password_entry.get()
        masked_password = ""
        new_item = {
            website: {
                "username": username,
                "password": password,
            }}
        for _ in password:
            masked_password += "*"
        if messagebox.askokcancel(title=website, message=f"Details: {website}\nUsername: {username}\n"
                                                         f"Password: {masked_password}\nSave?"):
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_item, file, indent=4)
            else:
                data.update(new_item)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror(message="Please make sure you haven't left any fields empty.")


# -------------------------- SEARCH PASSWORD ----------------------------- #

def search_password():
    website = website_entry.get().title()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            item = data[website]
    except FileNotFoundError:
        messagebox.showerror(message="Vault is empty")
    except KeyError:
        messagebox.showerror(message=f"{website} is not found.")
    else:
        messagebox.showinfo(message=f"{website}\nUsername: {item['username']}\nPassword: {item['password']}")
        pyperclip.copy(item["password"])


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

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "test@example.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=13, command=search_password)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
