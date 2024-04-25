import tkinter as tk
from tkinter import simpledialog


def open_popup():
    # Separate items by their status
    completed_items = [
        listbox.get(idx)
        for idx in range(listbox.size())
        if "completed" in listbox.get(idx)
    ]
    incomplete_items = [
        listbox.get(idx)
        for idx in range(listbox.size())
        if "not completed" in listbox.get(idx)
    ]

    # Create the pop-up window
    popup = tk.Toplevel()
    popup.title("Items by Status")

    # Create a canvas and attach vertical and horizontal scrollbars to it
    canvas = tk.Canvas(popup)
    v_scrollbar = tk.Scrollbar(popup, orient="vertical", command=canvas.yview)
    h_scrollbar = tk.Scrollbar(popup, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Grid the canvas and scrollbars
    canvas.grid(row=0, column=0, sticky="nsew")
    v_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    # Create a frame inside the canvas for the items
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Display completed items with wrapped lines
    tk.Label(frame, text="Completed Items:", wraplength=200).pack()
    for item in completed_items:
        tk.Label(frame, text=item, wraplength=200).pack()

    # Display a separator
    tk.Label(frame, text="---", wraplength=200).pack()

    # Display incomplete items with wrapped lines
    tk.Label(frame, text="Incomplete Items:", wraplength=200).pack()
    for item in incomplete_items:
        tk.Label(frame, text=item, wraplength=200).pack()

    # Update the scrollregion of the canvas to encompass the frame
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


root = tk.Tk()
root.title("List Box with Items")

# Create a list box
listbox = tk.Listbox(root)
listbox.grid(row=0, column=0, padx=10, pady=10)

# Add some items to the list box
items = [
    "Task 1 - completed",
    "Task 2 - not completed",
    "Task 3 - completed",
    "Task 4 - not completed",
    "Task 5 - completed",
]
for item in items:
    listbox.insert(tk.END, item)

# Create a button to open the pop-up
button = tk.Button(root, text="Show Items by Status", command=open_popup)
button.grid(row=1, column=0, pady=10)

root.mainloop()
