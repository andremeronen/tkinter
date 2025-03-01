#04.02.2025
#harjutus 2

import tkinter as tk
from PIL import Image, ImageTk

def loe_fail(failinimi):
    with open(failinimi, "r", encoding="utf-8") as file:
        return file.read()
def kuva_pilt(aken, failinimi):
    pilt = Image.open(failinimi)
    pilt=pilt.crop((0, 0, 200, 200))
    foto = ImageTk.PhotoImage(pilt)
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

def main():
    aken = tk.Tk()
    aken.title("Andre ülesanded")
    aken.geometry("200x200")
    

    kuva_pilt(aken, "chuck.png")

    aken.mainloop()



if __name__ == "__main__":
    main()