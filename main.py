import sqlite3
import os
import users as u
import games as g
import tkinter as tk
from ui import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "gamender.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

u.login('Andre', 'Andy1097')

if __name__ == "__main__":
    root = tk.Tk()
    app = Sign_In(root)
    root.mainloop()
