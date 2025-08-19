import os
import tkinter as tk
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Potato Doom")
main.config(bg="#E4E2E2")
main.geometry("1920x1080")
def chooseMap():
    frame = tk.Frame(master=main)
    frame.config(bg="#EDECEC")
    frame.place(x=158, y=52, width=617, height=160)

    label = tk.Label(master=frame, text="Choose Map")
    label.config(bg="#E4E2E2", fg="#000")
    label.place(x=51, y=29, width=512, height=88)

    button = tk.Button(master=main, text="map1")
    button.config(bg="#E4E2E2", fg="#000")
    button.place(x=96, y=300, width=480, height=480)

    button1 = tk.Button(master=main, text="map2")
    button1.config(bg="#E4E2E2", fg="#000")
    button1.place(x=672, y=300, width=480, height=480)

    button2 = tk.Button(master=main, text="map3")
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
    
    button3 = tk.Button(master=main, text="Connect To Host 2")
    button3.config(bg="#E4E2E2", fg="#000")
    button3.place(x=588, y=444, width=300, height=300)

    button2 = tk.Button(master=main, text="Connect To Host 3")
    button2.config(bg="#E4E2E2", fg="#000")
    button2.place(x=1032, y=444, width=300, height=300) 

    button1 = tk.Button(master=main, text="Connect To Host 4")
    button1.config(bg="#E4E2E2", fg="#000")
    button1.place(x=1476, y=444, width=300, height=300)
Main_menu()
main.mainloop()
