import random
import string
from tkinter import *

def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for i in range(length))

    result_label.config(text=password)

root = Tk()
root.title("Password Generator")
root.geometry("400x300")

Label(root, text="Password Length").pack(pady=10)

length_entry = Entry(root)
length_entry.pack()

Button(
    root,
    text="Generate Password",
    command=generate_password
).pack(pady=20)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()