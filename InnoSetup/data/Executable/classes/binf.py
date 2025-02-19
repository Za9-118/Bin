import winshell
import pythoncom
import os
import tkinter as tk
from pygame import mixer
from pygame.mixer import Sound

mixer.init()
def openrec():
    os.system("start shell:RecycleBinFolder")
    Sound("png/binquest.mp3").play()

def ico_hunger(root,file):
    if root==None:
        hunger = len(list(winshell.recycle_bin()))
        if hunger:
            set_iconr(1,file)
        else:
            set_iconr(0,file)
    else:
        hunger = len(list(winshell.recycle_bin()))
        if hunger:
            set_ico(1,root,file)
        else:
            set_ico(0,root,file)

def clean(main):
    #root.destroy()
    main()
    winshell.recycle_bin().empty(0)
    main()
    Sound("png/binclean.mp3").play()

def set_iconr(hungry,file):
    pythoncom.CoInitialize()
    dire=os.path.abspath(os.path.dirname(file))

    if hungry:
        ico="png/full.ico"
    else:
        ico="png/bin.ico"
    
    link_filepath = os.path.join(winshell.desktop(), "Bin.lnk")
    with winshell.shortcut(link_filepath) as link:
        #link.path = __file__
        link.description = "Progressbar Bin"
        
        link.path = f"{dire}/../Bin.exe"

        link.working_directory = dire+"/.."
        link.icon_location = (os.path.join(dire, ico.replace("/", "\\")), 0)
    pythoncom.CoUninitialize()

def set_ico(hungry,root,file):
    pythoncom.CoInitialize()
    dire=os.path.abspath(os.path.dirname(file))

    if hungry:
        root.iconphoto(0, tk.PhotoImage(file="png/full.png"))
        ico="../png/full.ico"
    else:
        root.iconphoto(0, tk.PhotoImage(file="png/bin.png"))
        ico="../png/bin.ico"
    print(ico)
    
    link_filepath = os.path.join(winshell.desktop(), "Bin.lnk")
    with winshell.shortcut(link_filepath) as link:
        #link.path = __file__
        link.description = "Progressbar XB Bin"
        
        link.path = f"{dire}/../Bin.exe"

        link.working_directory = dire+"/.."
        link.icon_location = (os.path.join(dire, ico.replace("/", "\\")), 0)
    pythoncom.CoUninitialize()
