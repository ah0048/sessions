import tkinter as tk

# # Create main window
# root = tk.Tk()

# # Window title
# root.title("My first Tkinter app")

# # Set size
# root.geometry("500x600")

# # Run the event loop
# root.mainloop()


root = tk.Tk()
root.title("Labels Example")
root.geometry("500x600")






# label widget

# label = tk.Label(root, text="Hello World!", font=("Arial", 15))
# label.pack()

# button widget

# def say_hello():
#     print("Hello World!")


# button = tk.Button(root, text="Click me", command=say_hello)
# button.pack()


# entry widget

# entry = tk.Entry(root)
# entry.pack(pady=5)

# def show_entry():
#     print(entry.get())

# button = tk.Button(root, text="click me", command=show_entry)
# button.pack(pady=5)


# # text widget
# text = tk.Text(root, height=5, width=30)
# text.pack(pady=5)

# def show_text():
#     print(text.get("1.0", tk.END))

# button = tk.Button(root, text="show text", command=show_text)
# button.pack(pady=5)


# # checkbox widget
# var = tk.IntVar()

# checkbox = tk.Checkbutton(root, text="check button", variable=var)
# checkbox.pack(pady=5)

# def check_status():
#     print("Checked?" , var.get())

# btn = tk.Button(root, text="Check", command=check_status)
# btn.pack(pady=5)


# --------- layout managers -------------
# pack

# label1 = tk.Label(root, text="Top")
# label1.pack(side="top")

# label2 = tk.Label(root, text="Bottom")
# label2.pack(side="bottom")



# # grid

# username_label = tk.Label(root, text="Username")
# username_label.grid(row=0, column=0)

# username_entry = tk.Entry(root)
# username_entry.grid(row=0, column=1)

# password_label = tk.Label(root, text="Pasword")
# password_label.grid(row=1, column=0)

# password_entry = tk.Entry(root, show="*")
# password_entry.grid(row=1, column=1)


# # place

# def login():
#     print(f"Username: {username_entry.get()}")
#     print(f"Password: {password_entry.get()}")

# button = tk.Button(root, text="Login", command=login)
# button.place(x=100, y=200)

# def on_key(event):
#     print(f"You pressed: {event.char}")

# root.bind("<Key>", on_key)



# mini login form

# root.title("Login Form")
# root.geometry("500x600")

# username_label = tk.Label(root, text="Username")
# username_label.grid(row=1, column=1)

# username_entry = tk.Entry(root)
# username_entry.grid(row=1, column=2)

password_label = tk.Label(root, text="Password")
password_label.grid(row=2, column=1)

# password_entry = tk.Entry(root, show="*")
# password_entry.grid(row=2, column=2)


# def login():
#     username = username_entry.get()
#     password = password_entry.get()
#     if username == "admin" and password == "123456":
#         print("Login Successful !!")
#     else:
#         print("Wrong username or passowrd")

# button = tk.Button(root, text="Login", command=login)
# button.grid(row=3, column=2)



# file manager

from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="choose a file")
    print(f"you selected file: {file_path}")


button = tk.Button(root, text="Open File", command=open_file)
button.pack()


root.mainloop()
