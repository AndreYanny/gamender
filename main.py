import sqlite3
import os
import users as u
import games as g
import handlers as h
import tkinter as tk
import pandas as pd
from ui import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "gamender.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()

if __name__ == "__main__":
    main_account_screen()
