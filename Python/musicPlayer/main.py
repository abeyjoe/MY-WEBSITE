import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

player = tkinter.Tk()
player.title("Music Player")
player.geometry("310x325")

var = tkinter.StringVar()
var.set("Slect the song to play")

os.chdir(askdirectory())
songlist = os.listdir()

playing = tkinter.Listbox(player.font="Helvetica", width=28,bg="black",fg="while",selectmode=tkinter.Si)

for item in songlist:
    playing.insert(0,item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tkinter.ACTIVE))
