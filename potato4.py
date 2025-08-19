import os
from tkinter import *
from PIL import Image, ImageTk
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = Tk()
main.title("Potato Doom")
main.config(bg="#E4E2E2")
main.geometry("1920x1080")

connect = []

def clear_screen():
    for widget in main.winfo_children():
        widget.destroy()

def start():
    if connect[0] == 4:
        command = ['./host.sh', str(connect[1])]
    elif connect[0] == 2:
        command = ['./join.sh', str(connect[0]), str(connect[1])]
    elif connect[0] ==3:
        command = ['./join.sh', str(connect[0]), str(connect[1])]
    elif connect[0] == 1:
        command = ['./join.sh', str(connect[0]), str(connect[1])]
    subprocess.run(command)
def host1():
    clear_screen()
    connect.insert(0, 1)
    Main_menu()
def host2():
    clear_screen()
    connect.insert(0, 2)
    chooseMap()
def host3():
    clear_screen()
    connect.insert(0, 3)
    chooseMap()
def host4():
    clear_screen()
    connect.insert(0, 4)
    chooseMap()



def map1():
    connect.insert(1, 1)
    start()
def map2():
    connect.insert(1, 2)
    start()
def map3():
    connect.insert(1, 3)
    start()
def map4():
    connect.insert(1, 4)
    start()
def map5():
    connect.insert(1, 5)
    start()
def map6():
    connect.insert(1, 6)
    start()

map1img = PhotoImage(file=os.path.join(BASE_DIR, "maps", "map1.png"))
map2img = PhotoImage(file=os.path.join(BASE_DIR, "maps", "map2.png"))
map3img = PhotoImage(file=os.path.join(BASE_DIR, "maps", "map3.png"))
map4img = PhotoImage(file=os.path.join(BASE_DIR, "maps", "map4.png"))
map5img = PhotoImage(file=os.path.join(BASE_DIR, "maps", "map5.png"))
map6img = PhotoImage(file=os.path.join(BASE_DIR, "maps", "map6.png"))

def chooseMap():
    frame = Frame(master=main, bg="#EDECEC")
    frame.place(x=158, y=52, width=617, height=160)

    label = Label(master=frame, text="Choose Map", bg="#E4E2E2", fg="#000")
    label.place(x=51, y=29, width=512, height=88)

    Button(main, text="map1", command=map1, image=map1img).place(x=96, y=300, width=480, height=480)
    Button(main, text="map2", command=map2, image=map2img).place(x=672, y=300, width=480, height=480)
    Button(main, text="map3", command=map3, image=map3img).place(x=1248, y=300, width=480, height=480)
    Button(main, text="map4", command=map4, image=map4img).place(x=96, y=800, width=480, height=200)
    Button(main, text="map5", command=map5, image=map5img).place(x=672, y=800, width=480, height=200)
    Button(main, text="map6", command=map6, image=map6img).place(x=1248, y=800, width=480, height=200)

def Main_menu():
    frame = Frame(master=main, bg="#EDECEC")
    frame.place(x=104, y=99, width=613, height=218)

    label = Label(master=frame, text="Host 4", bg="#E4E2E2", fg="#000")
    label.place(x=91, y=56, width=422, height=125)

    Button(main, text="Host Game", command=host4).place(x=144, y=444, width=300, height=300)
    Button(main, text="Connect To Host 1", command=host1).place(x=588, y=444, width=300, height=300)
    Button(main, text="Connect To Host 2", command=host2).place(x=1032, y=444, width=300, height=300)
    Button(main, text="Connect To Host 3", command=host3).place(x=1476, y=444, width=300, height=300)

Main_menu()
main.mainloop()
