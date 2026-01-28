from tkinter import * #importing everything from tkinter
import sqlite3

#widgets - GUI elements
#windows - container

conn = sqlite3.connect("database.db")  # creating db
cursor = conn.cursor()
#===================================
cursor.execute("""CREATE TABLE IF NOT EXISTS gpus (id INTEGER PRIMARY KEY, gpuname TEXT, vram TEXT, MHz TEXT, vmhz TEXT)""")

gpus = [
    ("RTX 3060", "12GB", "1867 MHz chip", "15000 MHz VRAM"),
    ("RTX 3070", "8GB", "1815 MHz chip", "14000 MHz VRAM"),
    ("RTX 3080", "10GB", "1710 MHz chip", "19000 MHz VRAM"),
    ("RTX 4060", "8GB", "2535 MHz chip", "17000 MHz VRAM"),
    ("RTX 4070", "12GB", "2550 MHz chip", "21000 MHz VRAM"),
    ("RX 7600", "8GB", "2755 MHz chip", "18000 MHz VRAM"),
    ("RX 9070 XT", "16GB", "3030 MHz chip", "20000 MHz VRAM"),
    ("Arc B570", "10GB", "2660 MHz chip", "19000 MHz VRAM"),
]

cursor.executemany(
    "INSERT INTO gpus (gpuname, vram, MHz, vmhz) VALUES (?, ?, ?, ?)",
    gpus
)
conn.commit()

#===================================
def search(): #searchinf function
    query = entry.get()

    listbox.delete(0, END)

    cursor.execute(
        "SELECT gpuname, vram, MHz, vmhz FROM gpus WHERE gpuname LIKE ?",
        ("%" + query + "%",)
    )

    rows = cursor.fetchall()

    for name, vram, mhz, vmhz in rows:
        listbox.insert(END, name)
        listbox.insert(END, f"  VRAM: {vram}")
        listbox.insert(END, f"  {mhz}")
        listbox.insert(END, f"  {vmhz}")
        listbox.insert(END, "-" * 30)
#===================================

window = Tk() #creating a window

#===================================
entry = Entry() #declaring a textbox
entry.config(font=("Courier New",20)) #changing font and text size
entry.insert(0,"write here!") #creating basic text
entry.pack() #placing a textbox
window.geometry("500x500") #creating a size of a window
window.title("App") #creating a name of Application

btn = Button(window, text="Search", command=search)
btn.pack(pady=5)

listbox = Listbox(
    window,
    width=60,
    height=15,
    font=("Courier New", 12)
)
listbox.pack(pady=10)
window.mainloop() #event listener and windowloop

