#11.02.2025
#harjutus 8

import tkinter as tk 
from tkinter import filedialog
from pathlib import Path
from PIL import Image, ImageOps
import os

selected_files=[]


def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        dir_label.config(text=f"Valitud kaust: {directory}")
        kausta_sisu=os.listdir(directory)
        for fail in kausta_sisu:
            file_name, file_extension=os.path.splitext(fail)
            if file_extension == ".jpg":
                inputtxt.insert(tk.END, fail+"\n")
                selected_files.append(os.path.join(directory, fail))
        print(selected_files)
    else:
        dir_label.config(text="Kausta ei valitud.")


def save_images():
    pass


aken = tk.Tk()
aken.title("Pildi suuruse muutmine")
aken.geometry("450x400")

label = tk.Label(aken, text="Pilid suurus 200x200", font="Arial=16")

inputtxt=tk.Text(aken, height=10, width=50)
inputtxt.pack(pady=10)

open_button=tk.Button(aken, text="vali failid", command=open_directory)
open_button.pack(pady=10)

save_button=tk.Button(aken, text="salvesta pildid", command=save_images)
save_button.pack(pady=10)

dir_label=tk.Label(aken, text="")
dir_label.pack(pady=10)

aken.mainloop()
