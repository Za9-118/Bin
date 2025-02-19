import tkinter as tk
import winshell
import sys
import os, json
import threading as thr
from classes.binf import *
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer
from pygame.mixer import Sound

mixer.init()

def crash():
    nomore

def get_arg():
    ico_hunger(root,__file__)
    if len(sys.argv) > 1:
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        sys.argv.append("nothing!./")
        deleted=0
        endit=0
        for file in sys.argv[1:]:
            try:
                if "bin" in file.lower():
                    os.system("python bindialog.py")
                    endit=1
                else:
                    winshell.delete_file(file)
                    deleted+=1
                    root.withdraw()
                    sfx=Sound("png/bineat.mp3")
                    th=thr.Thread(target=sfx.play)
                    th.start()
            except:
                print("not file")
                if endit:
                    crash()

root = tk.Tk()
get_arg()
root.title("Bin")
running=1
try:
	data=json.loads(open("data.json").read())
except:
	data={
		"Happiness": 50,
		"Mood": ["Awake","Shy"],
		"Skin": "XB",
		"IsDream": 0,
		"ver": "1.1"
	}
root.geometry("280x320")
root.resizable(0, 0)
ico_hunger(root,__file__)

hunger = len(list(winshell.recycle_bin()))
def update_hunger():
    # update hunger
    global hunger
    hunger_old = hunger
    while running:
        hunger_old = hunger
        hunger = len(list(winshell.recycle_bin()))
        if hunger_old != hunger:
            render_hunger()
            ico_hunger(root,__file__)

def render_hunger():
    if hunger < 2:
        ttk.Label(root, text="  Hungry  ").place(x=140, y=140, anchor="center")
    elif hunger > 1 and hunger < 5:
        ttk.Label(root, text="Well-fed").place(x=140, y=140, anchor="center")
    elif hunger > 4 and hunger < 20:
        ttk.Label(root, text="Over-fed").place(x=140, y=140, anchor="center")
    elif hunger > 19:
        ttk.Label(root, text="  Obese  ").place(x=140, y=140, anchor="center")

    if hunger:
        ttk.Button(root, text="Clean", command=lambda:clean(main)).place(x=140, y=170, anchor="center")
    else:
        ttk.Button(root, text="Clean", state="disabled").place(x=140, y=170, anchor="center")

def caress():
    global data
    data["Happiness"] += 5
    main()
    Sound("png/binhappy.mp3").play()

def razz():
    global ata
    data["Happiness"] -= 5
    main()
    Sound("png/binquest.mp3").play()

def main():
    ttk.Separator(root, orient='horizontal').place(x=50, y=190, width=180, height=2)
    ttk.Separator(root, orient='horizontal').place(x=50, y=125, width=180, height=2)
    
    imgo     = Image.open("png/sad.png").resize((20,20))
    img      = ImageTk.PhotoImage(imgo)
    root.img = img
    sadimg   = ttk.Label(root, image=img).place(x=80,y=35)

    imgo     = Image.open("png/neutral.png").resize((20,20))
    img      = ImageTk.PhotoImage(imgo)
    root.imgj= img
    okimg    = ttk.Label(root, image=img).place(x=140,y=50, anchor="center")

    imgo     = Image.open("png/happy.png").resize((20,20))
    img      = ImageTk.PhotoImage(imgo)
    root.imgb= img
    happyimg = ttk.Label(root, image=img).place(x=175,y=35)

    happybar = ttk.Progressbar(value=data["Happiness"]).place(x=140, y=75, anchor="center")
    if data["Happiness"] > 50:
        ttk.Label(root, text=f"(+{data["Happiness"]-50})", foreground="green").place(x=140, y=100, anchor="center")
        ttk.Label(root, text="Happy").place(x=140, y=25, anchor="center")
    elif data["Happiness"] == 50:
        ttk.Label(root, text=f"   (0)   ").place(x=140, y=100, anchor="center")
        ttk.Label(root, text="Neutral").place(x=140, y=25, anchor="center")
    else:
        ttk.Label(root, text=f"(-{abs(data["Happiness"]-50)})", foreground="red").place(x=140, y=100, anchor="center")
        ttk.Label(root, text="   Sad   ").place(x=140, y=25, anchor="center")

    render_hunger()

    ttk.Button(root, text="Caress", command=caress).place(x=140, y=215, anchor="center")
    ttk.Button(root, text="Razz", command=razz).place(x=140, y=250, anchor="center")
    ttk.Button(root, text="Open..", command=openrec).place(x=140, y=285, anchor="center")

main()
t=thr.Thread(target=update_hunger)
t.start()
root.mainloop()
running=0

with open("data.json", "w") as f:
    f.writelines(json.dumps(data))