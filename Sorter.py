
from StatMethods import AniArrayToNameString, AnimeFilter, SortDict, GetTopN, GenerateOptions
from GetAnimeFromJson import GenerateAnimeFromJson as GetAnime
from tkinter import *

# , border="#e3e3fc"


def UpdateSelection():
    """
    Checks filter Options and filters the Anime
    """
    # inclusivity of genre and tags
    if 0 in toggleboxes['dual'].curselection():
        SelectToggle['dual'] = True
    else:
        SelectToggle['dual'] = False

    for option in list(OptionSets.keys()):
        # inclusive of genre or tags
        if not (option == 'status' or option == 'year' or option == 'season'):
            if 0 in toggleboxes[option].curselection():
                SelectToggle[option] = True
            else:
                SelectToggle[option] = False

        # filter options
        SelectedOptions[option] = []
        for x in listboxes[option].curselection():
            SelectedOptions[option].append(listboxes[option].get(x).__str__())

    Results = AniArrayToNameString(AnimeFilter(
        Anime, SelectedOptions, SelectToggle))
    lb1.config(text=Results)


# Creates Tkinter window
root = Tk()
root.geometry("1280x960")
root.config(background="#101942")

# Gets Array of Anime
Anime = GetAnime()
Results = "ALL"

# Creates Filter list (OptionSets) and Filter Selected (Selected Options)
OptionSets = GenerateOptions(Anime)
SelectedOptions = {}
SelectToggle = {}
for option in list(OptionSets.keys()):
    SelectedOptions[option] = []
    if not (option == 'status' or option == 'year' or option == 'season'):
        SelectToggle[option] = False


# Creates sublist to allow for grid usage in the listboxes
subroot = Listbox(root)
subroot.pack(anchor=N)
subroot.config(background="#253372")

h1 = Label(subroot, text="Status", background="#805f5f",
           foreground="#FFFFFF").grid(row=2, column=0)
h2 = Label(subroot, text="Tags", background="#805f5f",
           foreground="#FFFFFF").grid(row=2, column=1)
h3 = Label(subroot, text="Genres", background="#805f5f",
           foreground="#FFFFFF").grid(row=2, column=2)
h4 = Label(subroot, text="Years", background="#805f5f",
           foreground="#FFFFFF").grid(row=2, column=3)
h5 = Label(subroot, text="Season", background="#805f5f",
           foreground="#FFFFFF").grid(row=2, column=4)


# , background="#12136b",foreground="#3ef9d1"
# , background="#1f3154",foreground="#ff6b6b"

# Creation of filter lists from option set
i = 0
listboxes = {}
toggleboxes = {}
scrollbars = {}
for option in list(OptionSets.keys()):
    #############################
    # Creates Inclusive buttons #
    #############################
    if not (option == 'status' or option == 'year' or option == 'season'):
        toggleboxes[option] = Listbox(
            subroot, width=0, height=0, background="#12136b", foreground="#3ef9d1", selectbackground="#00F0FF", selectforeground="#000000", exportselection=False, selectmode=SINGLE)
        toggleboxes[option].grid(row=1, column=i)
        toggleboxes[option].insert(END, "INCLUSIVE")
        toggleboxes[option].insert(END, "EXCLUSIVE")
        toggleboxes[option].select_set(0)

    #####################
    # Filter List Boxes #
    #####################
    listboxes[option] = Listbox(
        subroot, width=0, selectmode=MULTIPLE, selectbackground="#FFF000", selectforeground="#000000", exportselection=False, background="#12136b", foreground="#3ef9d1")
    # for j in range(0, 100):
    #     listboxes[option].insert(END, f"{j}")
    for element in list(OptionSets[option]):
        listboxes[option].insert(END, element)

    listboxes[option].grid(row=3, column=i)

    scrollbars[option] = Scrollbar(listboxes[option])

    listboxes[option].config(yscrollcommand=scrollbars[option].set)
    scrollbars[option].config(command=listboxes[option].yview)
    i = i+1


h6 = Label(subroot, text="TAG AND GENRE EXCLUSIVITY",
           wraplength=90, background="#1f3154", foreground="#6bd7ff").grid(row=1, column=6)

toggleboxes['dual'] = Listbox(
    subroot, width=0, height=0, selectbackground="#00F0FF", selectforeground="#000000", exportselection=False, selectmode=SINGLE, background="#12136b", foreground="#3ef9d1")
toggleboxes['dual'].grid(row=2, column=6)
toggleboxes['dual'].insert(END, "INCLUSIVE")
toggleboxes['dual'].insert(END, "EXCLUSIVE")
toggleboxes['dual'].select_set(0)

# SELECTS ALL STARTING LISTS FIRST
listboxes['status'].select_set(0, END)

# Adds Button to update list to use current filters
b = Button(root, text="UPDATE SELECTION",
           command=UpdateSelection, background="#1f3154", foreground="#6bd7ff")
b.pack(anchor=N)

# Text list of Anime
lb1 = Label(root, text=Results, wraplength=1280,
            background="#1f3154", foreground="#6bd7ff")
lb1.pack(anchor=N)

# Runs Update Selection once when program is ran
UpdateSelection()

# Tkinter loop start
root.mainloop()
