import tkinter
from tkinter import ttk



# root = tkinter.Tk()

# root.title("Treeview example")

# root.geometry("600x500")

# -------------- treeview -----------------

# tree = ttk.Treeview(root, columns=("Name", "Quantity", "Material"), show="headings")

# tree.heading("Name", text="Part Name")
# tree.heading("Quantity", text="Quantity")
# tree.heading("Material", text="Material")


# tree.insert("", "end", values=("Bolt", 50, "Steel"))
# tree.insert("", "end", values=("Nut", 30, "Steel"))
# tree.insert("", "end", values=("Sheetmetal", 50, "Aluminuim"))

# tree.pack(fill="both", expand=True)



# ---------------- scrollable treeview ----------------------

# frame = tkinter.Frame(root)
# frame.pack(fill="both", expand=True)

# scroll_y = tkinter.Scrollbar(frame, orient="vertical")

# tree = ttk.Treeview(frame, columns=("Name", "Qty"), show="headings", yscrollcommand=scroll_y.set)

# scroll_y.config(command=tree.yview)

# tree.heading("Name", text="Part Name")
# tree.heading("Qty", text="Quantity")

# for i in range(100):
#     tree.insert("", "end", values=(f"part {i}", i*5))

# tree.pack(side="left", fill="both", expand=True)
# scroll_y.pack(side="right", fill="y")

import pandas as pd

# ----------- reading from excel ----------------

# df = pd.read_excel("Day_5/bom.xlsx", sheet_name="project")           # dataframe is a table
# print(df)
# print(df.columns)
# print(df.head())

# ----------- writing excel ---------------

# df.to_excel("test.xlsx", index=False)


# ------------- selecting columns and rows ------------------

# get column values
# print(df["Material"])
# print(df["Part Name"])

# get multiple columns values
# print(df[["Part Name", "Material", "Cost"]])

# print(df.iloc[3])

# get specific cell
# print(df.loc[1, "Part Name"])


# ----------------- filtering ----------------
# cheap_parts = df[df["Cost"] <= 1.5]
# print(cheap_parts)

# alum_parts = df[df["Material"] == "Aluminum"]
# print(alum_parts)

# ---------------- sorting ---------------

# sorted_df = df.sort_values(by="Cost")
# print(sorted_df)

# sorted_df = df.sort_values(by="Quantity")
# print(sorted_df)


# ----------------- grouping -----------------

# grouped_df = df.groupby("Material")["Quantity"].sum()
# print(grouped_df)

# ------------------ example for pandas & treeview -------------------
# root = tkinter.Tk()

# root.title("Treeview example")

# root.geometry("600x500")


# df = pd.read_excel("Day_5/bom.xlsx", sheet_name="project")

# tree = ttk.Treeview(root, columns=list(df.columns), show="headings")

# for col in df.columns:
#     tree.heading(col, text=col)
#     tree.column(col, width=100)

# for i, row in df.iterrows():
#     tree.insert("", "end", values=list(row))

# tree.pack(fill="both", expand=True)


# root.mainloop()
