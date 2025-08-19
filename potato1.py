import os
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Potato Doom")
main.config(bg="#E4E2E2")
main.geometry("1920x1080")

connect = []
def start():
    print(str(connect))

def host1():
    connect.insert(0,1)
def host2():
    connect.insert(0,2)
    chooseMap()
def host3():
    connect.insert(0,3)
    chooseMap()
def host4():
    connect.insert(0,4)
    chooseMap()
    
    
def map1():
    connect.insert(1,1)
    start()
def map2():
    connect.insert(1,2)
    start()
def map3():
    connect.insert(1,3)
    start()
def map4():
    connect.insert(1,4)
    start()
def map5():
    connect.insert(1,5)
    start()
def map6():
    connect.insert(1,6)
    start()

map1img = PhotoImage(file = r"\maps\map1.png")
map2img = PhotoImage(file = r"\maps\map2.png")
map3img = PhotoImage(file = r"\maps\map3.png")
map4img = PhotoImage(file = r"\maps\map4.png")
map5img = PhotoImage(file = r"\maps\map5.png")
map6img = PhotoImage(file = r"\maps\map6.png")

def chooseMap():
    frame = tk.Frame(master=main)
    frame.config(bg="#EDECEC")
    frame.place(x=158, y=52, width=617, height=160)

    label = tk.Label(master=frame, text="Choose Map")
    label.config(bg="#E4E2E2", fg="#000")
    label.place(x=51, y=29, width=512, height=88)

    button = tk.Button(master=main, text="map1", command=map1, image=map1img)
    button.config(bg="#E4E2E2", fg="#000")
    button.place(x=96, y=300, width=480, height=480)

    button1 = tk.Button(master=main, text="map2", command=map2, image=map2img)
    button1.config(bg="#E4E2E2", fg="#000")
    button1.place(x=672, y=300, width=480, height=480)

    button2 = tk.Button(master=main, text="map3", command=map3, image=map3img)
    button2.config(bg="#E4E2E2", fg="#000")
    button2.place(x=1248, y=300, width=480, height=480)


def Main_menu():
    frame = tk.Frame(master=main)
    frame.config(bg="#EDECEC")
    frame.place(x=104, y=99, width=613, height=218)

    label = tk.Label(master=frame, text="Host 1")
    label.config(bg="#E4E2E2", fg="#000")
    label.place(x=91, y=56, width=422, height=125)
    
    button = tk.Button(master=main, text="Host Game", command=chooseMap)
    button.config(bg="#E4E2E2", fg="#000")
    button.place(x=144, y=444, width=300, height=300)
    
    button3 = tk.Button(master=main, text="Connect To Host 2", command=host2)
    button3.config(bg="#E4E2E2", fg="#000")
    button3.place(x=588, y=444, width=300, height=300)

    button2 = tk.Button(master=main, text="Connect To Host 3", command=host3)
    button2.config(bg="#E4E2E2", fg="#000")
    button2.place(x=1032, y=444, width=300, height=300) 

    button1 = tk.Button(master=main, text="Connect To Host 4", command=host4)
    button1.config(bg="#E4E2E2", fg="#000")
    button1.place(x=1476, y=444, width=300, height=300)
Main_menu()
main.mainloop()
