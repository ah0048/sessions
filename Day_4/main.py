import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Tkinter Advanced")
root.geometry("500x400")

dims = []
# importing an image
# image = Image.open("Day_4/python.png")
# image.resize((200, 200))
# photo = ImageTk.PhotoImage(image)

# img_label = tk.Label(text="this is an image", image=photo)
# img_label.pack()


# -------------------- option menu -------------------

# options = ["--please select an option--", "option 1", "option 2", "option 3"]
# selected = tk.StringVar()
# selected.set(options[0])

# menu = tk.OptionMenu(root, selected, *options)
# menu.pack()

# def show_option():
#     print(f"Selected: {selected.get()}")


# btn = tk.Button(root, text="show selected option", command=show_option)
# btn.pack()


# --------------- combo box ------------------

# options = ["--please select an option--", "option 1", "option 2", "option 3"]

# menu = ttk.Combobox(root, values=options)
# menu.current(0)
# menu.pack()

# def show_option():
#     print(f"Selected: {menu.get()}")


# btn = tk.Button(root, text="show selected option", command=show_option)
# btn.pack()


# canvas is a container of containers (frames)
# frame is a container of widgets

# --------------- scrolled text area -----------------
# scroller_text = scrolledtext.ScrolledText(root, width=40, height=5)
# scroller_text.pack()


# -------------- scroller canvas ------------------

# canvas = tk.Canvas(root, width=300, height=200)
# scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

# frame = tk.Frame(canvas)

# for i in range(20):
#     label = tk.Label(frame, text=f"this is item {i}")
#     label.pack()

# frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# canvas.create_window((0, 0), window=frame, anchor="nw")
# canvas.configure(yscrollcommand=scroll_y.set)

# canvas.pack(side="right")
# scroll_y.pack(side="left", fill="y")


# ------------ top level window ----------------

# def open_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("child window")
#     new_window.geometry("500x400")
#     root.withdraw()

# btn = tk.Button(text="open new window", command=open_window)
# btn.pack()


# ------------ notebook ---------------

# notebook = ttk.Notebook(root)

# tab1 = tk.Frame(notebook)
# tab2 = tk.Frame(notebook)

# notebook.add(tab1, text="BOM")
# notebook.add(tab2, text="Reports")

# notebook.pack(expand=True, fill="both")

# label1 = tk.Label(tab1, text="this is BOM tab")
# label1.pack()

# label2 = tk.Label(tab2, text="this is Reports tab")
# label2.pack()



# -------------- Message Boxes -----------------

# def show_messagebox():
#     messagebox.showinfo("INFO", "some info here !!")


# btn = tk.Button(root, text="show message box", command=show_messagebox)
# btn.pack()


def open_file():
    file_path = filedialog.askopenfilename()

    if file_path is None:
        messagebox.showerror("Error", "File Doesn't exist")
        return
    
    if selected.get() == "Text":
        with open(file_path, "r") as f:
            content = f.read()
        scroller_text.delete("1.0", tk.END)
        scroller_text.insert(tk.END, content)
    
    if selected.get() == "Image":
        image = Image.open(file_path)
        image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        label.configure(image=photo)
        label.image = photo


options = ["Text", "Image"]

selected = tk.StringVar()
selected.set(options[0])

menu = ttk.Combobox(root, textvariable=selected, values=options)
menu.pack()

btn = tk.Button(root, text="open file", command=open_file)
btn.pack()

scroller_text = scrolledtext.ScrolledText(root, width=40, height=10)
scroller_text.pack()

label = tk.Label(root)
label.pack()

root.mainloop()

