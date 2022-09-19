from tkinter import *
from functools import partial
# from turtle import Turtle, Screen
#
# screen = Screen()
# screen.bgcolor("#FFE3E1")

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Quiz Login Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="Your Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
#
# #Set the Menu initially
# menu = StringVar()
# menu.set("Select Any Topic you want quiz on")
#
# #Create a dropdown Menu
# drop = OptionMenu(tkWindow, menu, "Science", "Astronomy", "Culture", "History", "Geography")
# drop.pack()

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Go!", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()
