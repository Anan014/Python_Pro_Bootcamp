from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_input.delete(0,'end')
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    password = password_input.get()
    email = email_user_input.get()
    if len(website) > 0 and len(password) > 0 and len(email) > 0:
        is_ok = messagebox.askokcancel(title=website_input.get(),
                               message=f"These are the details enterd:"
                                       f"\nEmail: {email}"
                                       f"\nPassword: {password}"
                                       f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.writelines(f"{website} | {email} | {password}\n")
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=38)
website_input.grid(row=1, column=1, columnspan=2)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

email_user_input = Entry(width=38)
email_user_input.grid(row=2, column=1, columnspan=2)
email_user_input.insert(0, "Anan18@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()