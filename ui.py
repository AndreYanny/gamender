import tkinter as tk
import tkinter.font as tkFont
import users as u


class Sign_In:

    username = None
    password = None

    def __init__(self, root, username=None, password=None):
        root.title("Gamender")
        width = 419
        height = 417
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        signinButton = tk.Button(root)
        signinButton["anchor"] = "center"
        signinButton["bg"] = "#efefef"
        signinButton["cursor"] = "arrow"
        ft = tkFont.Font(family='Times', size=10)
        signinButton["font"] = ft
        signinButton["fg"] = "#000000"
        signinButton["justify"] = "center"
        signinButton["text"] = "Sign-In"
        signinButton["relief"] = "raised"
        signinButton.place(x=160, y=320, width=79, height=30)
        signinButton["command"] = self.signinButton_command

        usernameLabel = tk.Label(root)
        usernameLabel["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=10)
        usernameLabel["font"] = ft
        usernameLabel["fg"] = "#333333"
        usernameLabel["justify"] = "center"
        usernameLabel["text"] = "Username"
        usernameLabel.place(x=20, y=190, width=106, height=30)

        passLabel = tk.Label(root)
        passLabel["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=10)
        passLabel["font"] = ft
        passLabel["fg"] = "#333333"
        passLabel["justify"] = "center"
        passLabel["text"] = "Password"
        passLabel.place(x=40, y=250, width=70, height=25)

        username = tk.StringVar()
        nameEntry = tk.Entry(root, textvariable=username)
        nameEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        nameEntry["font"] = ft
        nameEntry["fg"] = "#333333"
        nameEntry["justify"] = "center"
        nameEntry["text"] = ""
        nameEntry.place(x=140, y=190, width=215, height=30)
        self.username = username

        password = tk.StringVar()
        passEntry = tk.Entry(root, textvariable=password)
        passEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        passEntry["font"] = ft
        passEntry["fg"] = "#333333"
        passEntry["justify"] = "center"
        passEntry["text"] = ""
        passEntry.place(x=140, y=250, width=215, height=30)
        self.password = password

        titleLabel = tk.Label(root)
        titleLabel["anchor"] = "center"
        titleLabel["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=58)
        titleLabel["font"] = ft
        titleLabel["fg"] = "#fad400"
        titleLabel["justify"] = "center"
        titleLabel["text"] = "Gamender"
        titleLabel.place(x=0, y=0, width=417, height=118)

    def signinButton_command(self):
        # u.login(self.username, self.password)
        print(self.username)
        