from tkinter import *
import os
import sqlite3
import users as u
import genres as ge
import games as g

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "gamender.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username:").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password:").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    global username1
    username1 = username_verify.get()
    global password1
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    user = (username1, password1)
    c.execute('SELECT * FROM user WHERE username = ? AND password = ?', user)
    if not c.fetchone():
        password_not_recognised()
    else:
        login_sucess()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Welcome back!").pack()
    Button(login_success_screen, text="Surprise me...", command=home).pack()
    global user_id
    user_id = u.get_user_id(username1)


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


def home():
    global home_screen

    genres = u.get_fav_genres(user_id)
    genre1 = ge.get_genre_name(genres[0][0])
    genre2 = ge.get_genre_name(genres[1][0])
    genre3 = ge.get_genre_name(genres[2][0])

    genre_id1 = ge.get_genre_id(genre1)
    genre_id2 = ge.get_genre_id(genre2)
    genre_id3 = ge.get_genre_id(genre3)

    top_game_id1 = ge.get_top_game(genre_id1)
    top_game_id2 = ge.get_top_game(genre_id2)
    top_game_id3 = ge.get_top_game(genre_id3)

    top_game1 = g.get_game_name(top_game_id1)
    top_game2 = g.get_game_name(top_game_id2)
    top_game3 = g.get_game_name(top_game_id3)

    home_screen = Toplevel(login_success_screen)
    home_screen.title("Home")
    home_screen.geometry("500x350")
    Label(home_screen, text="GAMENDER", font=32, pady=20).pack()
    Label(home_screen, text=genre1 + ":", font='Calibre 10 bold').pack()
    Label(home_screen, text=top_game1).pack()
    Label(home_screen, text=genre2 + ":", font='Calibre 10 bold').pack()
    Label(home_screen, text=top_game2).pack()
    Label(home_screen, text=genre3 + ":", font='Calibre 10 bold').pack()
    Label(home_screen, text=top_game3).pack()
    Button(home_screen, text="Review Game", command=review_game).pack()


def review_game():
    global review_game_screen

    review_game_screen = Toplevel(home_screen)
    review_game_screen.title("Review Game")


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Gamender")
    Label(text="GAMENDER", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()
