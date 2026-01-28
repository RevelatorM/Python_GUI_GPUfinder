from tkinter import * #importing everything from tkinter
import sqlite3

#widgets - GUI elements
#windows - container

conn = sqlite3.connect("database.db")  # creating db
cursor = conn.cursor()
#===================================
cursor.execute("""CREATE TABLE IF NOT EXISTS gpus (id INTEGER PRIMARY KEY, gpuname TEXT, vram TEXT, MHz TEXT, vmhz TEXT)""")
sql = "INSERT INTO gpus (gpuname, vram, MHz, vmhz) VALUES (?, ?, ?, ?)"


#===================================
#def submit():

#===================================

window = Tk() #creating a window

#===================================
#submit = Button(window, text = "submit",command = submit) #creating a button
entry = Entry() #declaring a textbox
entry.config(font=("Courier New",20)) #changing font and text size
entry.insert(0,"write here!") #creating basic text
entry.pack() #placing a textbox
window.geometry("500x500") #creating a size of a window
window.title("App") #creating a name of Application
window.mainloop() #event listener and windowloop

