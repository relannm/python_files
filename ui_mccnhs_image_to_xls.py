import tkinter as tk
from tkinter import filedialog
import os
import time
import shutil
import cv2
from PIL import Image, ImageTk


# CONFIG - WINDOW SIZE and CONSTANTS
WINDOW_WIDTH_MIN = WINDOW_WIDTH = 380
WINDOW_HEIGHT_MIN = WINDOW_HEIGHT = 500

# CONFIG - TEXTS
PROGRAM_TITLE = "Prototype Document HT-SD"
PROGRAM_DESC = "Reads text from images and write it to spreadsheet"
SRC_LABEL = "Location (directory) of images"
BTN_LABEL = "CONVERT"
SUB_WINDOW_TITLE = "Please Select Directory of Input Images"

# CONFIG - COLORS
MAIN_BG = "#2C394B"
BTN_COLOR = "#00e6e6"
BTN_HOVER = "#ff3377"
BTN_FONT = MAIN_FONT = WHITE = SECOND_BG = "#FFFFFF"
GREY = "#999999"
BLACK = "#000000"


# to search for directory
def search_src_dir():
    current_dir = os.getcwd()
    src_dir = filedialog.askdirectory(parent=window, initialdir=current_dir, title=SUB_WINDOW_TITLE)
    if len(src_dir) > 0:
        entry_src.delete(0, tk.END)
        entry_src.insert(0, src_dir)
        entry_src.configure(fg=BLACK)


# execute button
def button_enter(event):
   button.config(bg=BTN_HOVER)


def button_leave(event):
   button.config(bg=BTN_COLOR)


# directories button
def button_dir_enter(event):
   button.config(bg=BTN_HOVER)


def button_dir_leave(event):
   button.config(bg=BTN_COLOR)


# clear text box when click to prepare for character input
def clear_entry_src(x):
    if entry_src.get() == SRC_LABEL:
        entry_src.delete(0, tk.END)
        entry_src.configure(fg=BLACK)


# reset text box - when entry is blank
def reset_entry_src(x):
    if not entry_src.get():
        entry_src.insert(0, SRC_LABEL)
        entry_src.configure(fg=GREY)


# function for writing to spreadsheet (excel)


# function called after pressing (execute) button
def execute_task():
    src_dir = entry_src.get()

    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)

    output_text.insert(tk.END, "\nChecking directories... \n\n")
    time.sleep(2)

    output_text.yview(tk.END)
    output_text.config(state=tk.DISABLED)

########## WINDOW ##########
# initialize window
window = tk.Tk()
window.title(PROGRAM_TITLE)
window.minsize(WINDOW_WIDTH_MIN, WINDOW_HEIGHT_MIN)
window.configure(bg=MAIN_BG)

# position of window after opening
##### get screen width and height
screen_width = window.winfo_screenwidth()     # width of the screen
screen_height = window.winfo_screenheight()   # height of the screen
##### calculate x and y coordinates for the Tk root window
win_pos_x = int((screen_width/2) - (WINDOW_WIDTH/2))
win_pos_y = int((screen_height/2) - (WINDOW_HEIGHT/2))
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{win_pos_x}+{win_pos_y}")

# dummy padding
label_topmargin = tk.Label(window, bg=MAIN_BG)
label_topmargin.pack(padx=20, pady=5)

# logo
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("mccnhs.PNG"))

# Create a Label Widget to display the text or Image
label_image = tk.Label(window, image=img)
label_image.pack(padx=20, pady=0)

# create a title bar
title_bar = tk.Frame(window, bg=MAIN_BG, relief=tk.FLAT, bd=2)

# description
label_program = tk.Label(window, text=PROGRAM_TITLE, bg=MAIN_BG, fg=MAIN_FONT, font=("Arial", 18, "bold"))
label_program.pack(padx=20, pady=20)
label_program = tk.Label(window, text=PROGRAM_DESC, bg=MAIN_BG, fg=MAIN_FONT, font=("Arial", 11))
label_program.pack(padx=20, pady=0)

# directories
dirframe = tk.Frame(window, bg=MAIN_BG, bd=0)
dirframe.columnconfigure(0, weight=1)
##### source
entry_src = tk.Entry(dirframe, width=70, bd=5, fg=GREY, relief=tk.FLAT, font=("Arial", 9))
entry_src.insert(0, SRC_LABEL)
entry_src.grid(row=0, column=0, sticky=tk.W+tk.E, pady=10)

button_src = tk.Button(dirframe, text="...", bg=WHITE, width=2, bd=3, relief=tk.FLAT, font=("Arial", 8),
                       activebackground=WHITE, activeforeground=WHITE, command=search_src_dir)
button_src.grid(row=0, column=1, sticky=tk.W+tk.E, pady=5)

entry_src.bind("<FocusIn>", clear_entry_src)
entry_src.bind("<FocusOut>", reset_entry_src)

dirframe.pack(padx=20, pady=20, fill="both", expand=True)

# execute button
button = tk.Button(window, text=BTN_LABEL, bd=0, bg=BTN_COLOR, fg=BTN_FONT, width=50, height=1, relief=tk.FLAT,
                   font=("Arial", 12), activebackground=BTN_HOVER, activeforeground=BTN_FONT, command=execute_task)
button.pack(padx=20, pady=0)
button.bind('<Enter>', button_enter)
button.bind('<Leave>', button_leave)

# output
output_text = tk.Text(window, bg="#334756", fg=BTN_FONT, width=100, height=150, relief=tk.FLAT, font=('Arial', 8))
output_text.pack(padx=20, pady=20)
output_text.config(state=tk.DISABLED)

# show window
window.lift()   #to start window it top level
window.mainloop()
