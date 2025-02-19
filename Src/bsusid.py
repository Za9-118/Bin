import winshell
import sys
import os
import threading as thr
from classes.binf import *

def crash():
    ahadhabafoqbfqbfhabodlqfojqbcpnzadoajhboqhfyuegwiyuiwesdrftgyhwetryfgkhw3sdfghrdfghdrtfyghj

hunger = len(list(winshell.recycle_bin()))
running = 1

def update_hunger():
    # update hunger
    global hunger
    hunger_old = hunger
    while running:
        hunger_old = hunger
        hunger = len(list(winshell.recycle_bin()))
        if hunger_old != hunger:
            ico_hunger(None,__file__)

update_hunger()
