from time import sleep
from tkinter import *
import pandas as pd
from collections import Counter
from itertools import chain
import os
import sqlite3
import users as u
import genres as ge
import games as g

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "gamender.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()
data_neighbours = pd.read_sql_query("SELECT * FROM collaboration", conn, index_col='game_id')
global radiobutton_nobody_saves_the_world


def updategenres(list, user):
    c.execute('DELETE FROM users_genres WHERE user_id = ?', (user,))
    conn.commit()
    for i in list:
        u.add_genre_byid(i + 1, user)


def addlikedgames(list, user):
    for i in list:
        u.add_game(user, g_id=i + 1)


def refresh(self):
    self.destroy()
    self.__init__()
    # self.pack(side=TOP, fill=BOTH)
    # self.config(relief=GROOVE, bd=2)


class homepage(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.genres = u.get_fav_genres(user_id)
        self.genre1 = ge.get_genre_name(self.genres[0][0])
        self.genre2 = ge.get_genre_name(self.genres[1][0])
        self.genre3 = ge.get_genre_name(self.genres[2][0])

        self.genre_id1 = ge.get_genre_id(self.genre1)
        self.genre_id2 = ge.get_genre_id(self.genre2)
        self.genre_id3 = ge.get_genre_id(self.genre3)

        self.top_game_id1 = ge.get_top_game(self.genre_id1)
        self.top_game_id2 = ge.get_top_game(self.genre_id2)
        self.top_game_id3 = ge.get_top_game(self.genre_id3)

        self.top_game1 = g.get_game_name(self.top_game_id1)
        self.top_game2 = g.get_game_name(self.top_game_id2)
        self.top_game3 = g.get_game_name(self.top_game_id3)
        self.collab_list = u.get_user_games(user_id)
        self.collab_games_id = get_top_game(self.collab_list)
        self.collab_games = []
        if self.collab_games_id != 0:
            for i in self.collab_games_id:
                self.collab_games.append(g.get_game_name(i))
            self.collab_games_conc = ', '.join(self.collab_games)
        else:
            self.collab_games_conc = 'please Review more games for a personalized recommendation'

        ##########HENA################
        Label(self, text="GAMENDER", font=32, pady=20).pack()
        Label(self, text=self.genre1 + ":", font='Calibre 10 bold').pack()
        Label(self, text=self.top_game1).pack()
        Label(self, text=self.genre2 + ":", font='Calibre 10 bold').pack()
        Label(self, text=self.top_game2).pack()
        Label(self, text=self.genre3 + ":", font='Calibre 10 bold').pack()
        Label(self, text=self.top_game3).pack()
        Label(self, text="Recommendations for you:", font='Calibre 10 bold').pack()
        Label(self, text=self.collab_games_conc).pack()
        Button(self, text="Review Game", command=review_game).pack()
        Button(self, text="Change Favourite Genres", command=change_fav_genres).pack()
        Label(self, text='').pack()
        ##########HENA################


def logoinscreendestroy():
    login_screen.destroy()


# Implementing event on register button
def register_user():
    username_info = username.get()
    password_info = password.get()
    global reg_user_id
    u.add_user(username_info, password_info)
    reg_user_id = u.get_user_id(username_info)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=11).pack()


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


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], maxpicks=2, side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.maxpicks = maxpicks
        self.numpicks = 0
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var,
                              command=checkmax(self, var))
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


def checkmax(bar, var):
    # called after the intvar is changed
    def _check():
        print(bar.numpicks, var.get())
        if var.get():  # checked
            if bar.numpicks < bar.maxpicks:
                bar.numpicks += 1
            else:
                var.set(0)
        else:  # unchecked
            bar.numpicks -= 1

    return _check


# Deleting popups
def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def remove_already_played(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)


def get_top_game(games_list):
    common = []
    listoflists = []
    if len(games_list) == 1:
        common.append(data_neighbours.iloc[games_list[0] - 1, 0])
        return common
    else:
        n = len(games_list)
        for j in range(0, n):
            listoflists.append(list(data_neighbours.iloc[games_list[j] - 1]))
        common = list(chain.from_iterable(listoflists))
        commonofmany = [k for k, v in Counter(common).items() if v > 1]
        if len(commonofmany) > 0:
            remove_already_played(commonofmany, games_list)
            return commonofmany
        else:
            remove_already_played(common, games_list)
            return list(dict.fromkeys(common))


def destroy_review_game():
    review_game_screen.destroy()


def destroy_fav_genres():
    change_f_g_screen.destroy()


def main_account_screen_destroy():
    main_screen.destroy()


###################################
################UI#################
###################################
# Designing Registration Window
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("600x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter your details below", pady=5).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username:")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password:")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    lng = Checkbar(register_screen, ['Action', 'Adventure', 'RPG', 'Simulation', 'Strategy', 'Sports & Racing'], 3)
    lng.pack(side=TOP, fill=BOTH)
    lng.config(relief=GROOVE, bd=2)

    def allstates():
        register_user()
        index_pos_list = [i for i in range(len(list(lng.state()))) if
                          list(lng.state())[i] == 1]
        print(index_pos_list)
        print(reg_user_id)
        updategenres(list=index_pos_list, user=reg_user_id)

    Label(register_screen, text='').pack()
    Button(register_screen, text="Register", width=10, height=1, command=allstates).pack()


# Designing Login Window
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter your details below to login", pady=5).pack()
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


# Designing popup for login success
def login_sucess():
    global login_success_screen
    logoinscreendestroy()
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("250x100")

    Label(login_success_screen, text="Welcome back!", pady=5).pack()
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


# Designing Home
def home():
    def refreshs():
        refresh(hm)
        hm.pack()

    # delete_login_success()
    global home_screen
    delete_login_success()
    main_account_screen_destroy()
    home_screen = Tk()
    mainContainer = Frame(home_screen)
    home_screen.title("Home")
    home_screen.geometry("500x350")
    hm = homepage(mainContainer)
    Button(home_screen, text="Refresh", command=refreshs).pack()
    hm.__init__()
    hm.pack()

    # hm.config(relief=GROOVE, bd=2)

    home_screen.mainloop()


# Designing Reviewing a Game Window
def review_game():
    global review_game_screen

    review_game_screen = Toplevel(home_screen)
    review_game_screen.title("Review Game")

    Label(review_game_screen, text='').grid(row=0, column=0)

    Label(review_game_screen, text="Positive", pady=5).grid(row=0, column=2)
    Label(review_game_screen, text="Negative", pady=5).grid(row=0, column=3)

    Label(review_game_screen, text="Dying Light 2").grid(row=1, column=1)
    global radiobutton_dying_light
    radiobutton_dying_light = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_dying_light, value=1).grid(row=1, column=2)
    Radiobutton(review_game_screen, variable=radiobutton_dying_light, value=0).grid(row=1, column=3)

    Label(review_game_screen, text="The Witcher 3 Wild Hunt").grid(row=2, column=1)
    global radiobutton_witcher
    radiobutton_witcher = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_witcher, value=1).grid(row=2, column=2)
    Radiobutton(review_game_screen, variable=radiobutton_witcher, value=0).grid(row=2, column=3)

    Label(review_game_screen, text="Cities Skylines").grid(row=3, column=1)
    global radiobutton_cities_skylines
    radiobutton_cities_skylines = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_cities_skylines, value=1).grid(row=3,
                                                                                        column=2)
    Radiobutton(review_game_screen, variable=radiobutton_cities_skylines, value=0).grid(row=3,
                                                                                        column=3)

    Label(review_game_screen, text="Crusader Kings 3").grid(row=4, column=1)
    global radiobutton_crusader_kings
    radiobutton_crusader_kings = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_crusader_kings, value=1).grid(row=4, column=2)
    Radiobutton(review_game_screen, variable=radiobutton_crusader_kings, value=0).grid(row=4, column=3)

    Label(review_game_screen, text="Civilization 6").grid(row=5, column=1)
    global radiobutton_civilization
    radiobutton_civilization = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_civilization, value=1).grid(row=5, column=2)
    Radiobutton(review_game_screen, variable=radiobutton_civilization, value=0).grid(row=5, column=3)

    Label(review_game_screen, text="Humankind").grid(row=6, column=1)
    global radiobutton_humankind
    radiobutton_humankind = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_humankind, value=1).grid(row=6, column=2)
    Radiobutton(review_game_screen, variable=radiobutton_humankind, value=0).grid(row=6, column=3)

    Label(review_game_screen, text="Forza Horizon 5").grid(row=7, column=1)
    global radiobutton_forza_horizon
    radiobutton_forza_horizon = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_forza_horizon, value=1).grid(row=7, column=2)
    Radiobutton(review_game_screen, variable=radiobutton_forza_horizon, value=0).grid(row=7, column=3)

    Label(review_game_screen, text="FIFA 22").grid(row=8, column=1)
    global radiobutton_fifa
    radiobutton_fifa = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_fifa, value=1).grid(row=8, column=2)
    Radiobutton(review_game_screen, variable=radiobutton_fifa, value=0).grid(row=8, column=3)

    Label(review_game_screen, text="Riders Republic").grid(row=9, column=1)
    global radiobutton_riders_republic
    radiobutton_riders_republic = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_riders_republic, value=1).grid(row=9,
                                                                                        column=2)
    Radiobutton(review_game_screen, variable=radiobutton_riders_republic, value=0).grid(row=9,
                                                                                        column=3)

    Label(review_game_screen, text='    ').grid(row=0, column=4)

    Label(review_game_screen, text="Positive", pady=5).grid(row=0, column=6)
    Label(review_game_screen, text="Negative", pady=5).grid(row=0, column=7)

    Label(review_game_screen, text="God of War").grid(row=1, column=5)
    global radiobutton_god_of_war
    radiobutton_god_of_war = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_god_of_war, value=1).grid(row=1, column=6)
    Radiobutton(review_game_screen, variable=radiobutton_god_of_war, value=0).grid(row=1, column=7)

    Label(review_game_screen, text="The Elder Scrolls Online").grid(row=2, column=5)
    global radiobutton_elder_scrolls_online
    radiobutton_elder_scrolls_online = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_elder_scrolls_online, value=1).grid(row=2,
                                                                                             column=6)
    Radiobutton(review_game_screen, variable=radiobutton_elder_scrolls_online, value=0).grid(row=2,
                                                                                             column=7)

    Label(review_game_screen, text="Disco Elysium").grid(row=3, column=5)
    global radiobutton_disco_elysium
    radiobutton_disco_elysium = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_disco_elysium, value=1).grid(row=3, column=6)
    Radiobutton(review_game_screen, variable=radiobutton_disco_elysium, value=0).grid(row=3, column=7)

    Label(review_game_screen, text="Life is Strange").grid(row=4, column=5)
    global radiobutton_life_is_strange
    radiobutton_life_is_strange = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_life_is_strange, value=1).grid(row=4,
                                                                                        column=6)
    Radiobutton(review_game_screen, variable=radiobutton_life_is_strange, value=0).grid(row=4,
                                                                                        column=7)

    Label(review_game_screen, text="It Takes Two").grid(row=5, column=5)
    global radiobutton_it_takes_two
    radiobutton_it_takes_two = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_it_takes_two, value=1).grid(row=5, column=6)
    Radiobutton(review_game_screen, variable=radiobutton_it_takes_two, value=0).grid(row=5, column=7)

    Label(review_game_screen, text="The Sims 4").grid(row=6, column=5)
    global radiobutton_sims
    radiobutton_sims = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_sims, value=1).grid(row=6, column=6)
    Radiobutton(review_game_screen, variable=radiobutton_sims, value=0).grid(row=6, column=7)

    Label(review_game_screen, text="Nobody Saves the World").grid(row=7, column=5)

    radiobutton_nobody_saves_the_world = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_nobody_saves_the_world, value=1).grid(row=7,
                                                                                               column=6)
    Radiobutton(review_game_screen, variable=radiobutton_nobody_saves_the_world, value=0).grid(row=7,
                                                                                               column=7)

    Label(review_game_screen, text="Planet Zoo").grid(row=8, column=5)
    global radiobutton_planet_zoo
    radiobutton_planet_zoo = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_planet_zoo, value=1).grid(row=8, column=6)
    Radiobutton(review_game_screen, variable=radiobutton_planet_zoo, value=0).grid(row=8, column=7)

    Label(review_game_screen, text="Metal Gear Rising").grid(row=9, column=5)
    global radiobutton_metal_gear_rising
    radiobutton_metal_gear_rising = IntVar()
    Radiobutton(review_game_screen, variable=radiobutton_metal_gear_rising, value=1).grid(row=9,
                                                                                          column=6)
    Radiobutton(review_game_screen, variable=radiobutton_metal_gear_rising, value=0).grid(row=9,
                                                                                          column=7)

    Label(review_game_screen, text='').grid(row=0, column=8)
    Label(review_game_screen, text='').grid(row=10, column=4)

    def updatedb():
        list_i_will_kill_you_for_making_me_do_this = [radiobutton_dying_light.get(), radiobutton_witcher.get(),
                                                      radiobutton_cities_skylines.get(),
                                                      radiobutton_crusader_kings.get(),
                                                      radiobutton_civilization.get(), radiobutton_humankind.get(),
                                                      radiobutton_forza_horizon.get(), radiobutton_fifa.get(),
                                                      radiobutton_riders_republic.get(), radiobutton_god_of_war.get(),
                                                      radiobutton_elder_scrolls_online.get(),
                                                      radiobutton_disco_elysium.get(),
                                                      radiobutton_life_is_strange.get(),
                                                      radiobutton_it_takes_two.get(), radiobutton_sims.get(),
                                                      radiobutton_nobody_saves_the_world.get(),
                                                      radiobutton_planet_zoo.get(), radiobutton_metal_gear_rising.get(),
                                                      ]
        index_pos_list = [i for i in range(len(list_i_will_kill_you_for_making_me_do_this)) if
                          list_i_will_kill_you_for_making_me_do_this[i] == 1]
        print(index_pos_list)
        addlikedgames(user=user_id, list=index_pos_list)
        destroy_review_game()

    Button(review_game_screen, text="Save", command=updatedb).grid(row=11, column=4)


# Designing Changing Favourite Genres Window
def change_fav_genres():
    global change_f_g_screen

    change_f_g_screen = Toplevel(home_screen)
    change_f_g_screen.title("Change Favourite Genres")

    lng = Checkbar(change_f_g_screen, ['Action', 'Adventure', 'RPG', 'Simulation', 'Strategy', 'Sports & Racing'], 3)

    lng.pack(side=TOP, fill=BOTH)

    lng.config(relief=GROOVE, bd=2)

    def allstates():
        index_pos_list = [i for i in range(len(list(lng.state()))) if
                          list(lng.state())[i] == 1]
        print(index_pos_list)
        updategenres(list=index_pos_list, user=user_id)
        destroy_fav_genres()

    Button(change_f_g_screen, text='submit', command=allstates).pack(side=RIGHT)
    change_f_g_screen.mainloop()


# Designing Main Window (First Window)
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
