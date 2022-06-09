import math
import random
from textwrap import wrap
import ResponseManuver as rm
import json
from StatMethods import AniArrayToNameString, AnimeFilter, SortDict, GetTopN, GenerateOptions
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime
from tkinter import *


def UpdateSelection():
    for option in list(OptionSets.keys()):
        SelectedOptions[option] = []
        for x in listboxes[option].curselection():
            SelectedOptions[option].append(listboxes[option].get(x).__str__())

    Results = AniArrayToNameString(AnimeFilter(Anime, SelectedOptions))
    lb1.config(text=Results)


root = Tk()
root.geometry("1080x720")

Anime = GetAnime()
Results = "ALL"

OptionSets = GenerateOptions(Anime)
SelectedOptions = {}
for option in list(OptionSets.keys()):
    SelectedOptions[option] = []


subroot = Listbox(root)
subroot.pack(anchor=W)


i = 0
listboxes = {}
scrollbars = {}
for option in list(OptionSets.keys()):
    listboxes[option] = Listbox(
        subroot, width=0, selectmode=MULTIPLE, selectbackground="#FFF000", selectforeground="#000000", exportselection=False)
    # for j in range(0, 100):
    #     listboxes[option].insert(END, f"{j}")
    for element in list(OptionSets[option]):
        listboxes[option].insert(END, element)

    listboxes[option].grid(row=0, column=i)

    scrollbars[option] = Scrollbar(listboxes[option])

    listboxes[option].config(yscrollcommand=scrollbars[option].set)
    scrollbars[option].config(command=listboxes[option].yview)
    i = i+1

listboxes['status'].select_set(0, END)


b = Button(root, text="UPDATE SELECTION",
           command=UpdateSelection)
b.pack(anchor=W)

lb1 = Label(root, text=Results, wraplength=720)
lb1.pack(anchor=W)

UpdateSelection()

root.mainloop()
