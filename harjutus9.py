#12.02.2025 Andre Meronen
#harjutus 9

import tkinter as tk
from tkinter import messagebox


aken=tk.Tk()
aken.title("Pitsa tellmisvorm")
aken.geometry("400x350")


def show_selection():
    # print("Hind:", selected_color.get())
    # print(var1.get()),float(var2.get()), (var3.get())
    # print(selected_option.get())
    if selected_option.get()=="Kuller (3€)":
        trans=3
    else:
        trans=0
    summa=selected_color.get()+var1.get()+float(var2.get()+var3.get())+trans
    print(summa)

# StringVar, mis hoiab valitud värvi nime
selected_color = tk.StringVar(value=5)

tk.Label(aken, text="Kasutaja ID", font="Arial 16").pack(pady=10)
sisestus1 = tk.Entry(aken).pack()

tk.Label(aken, text="Vali suurus", font="Arial 16").pack(pady=10)


# Loome raadionupud
radio_red = tk.Radiobutton(aken, text="Väike (5€)", variable=selected_color, value=5)
radio_green = tk.Radiobutton(aken, text="Suur (8€)", variable=selected_color, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere (12€)", variable=selected_color, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()
def show_selection():
    print(var1.get(), var2.get())

var1=tk.IntVar(value=0)
var2=tk.StringVar(value=0)
var3=tk.IntVar(value=0)

checkbox1 = tk.Checkbutton(aken, text="Juust(+1€)", variable=var1, onvalue=1, offvalue=0)
checkbox2 = tk.Checkbutton(aken, text="Pepperoni(+1.5€)", variable=var2, onvalue=1.5, offvalue=0)
checkbox3=tk.Checkbutton(aken, text="Seen(+1€)", variable=var3, onvalue=1, offvalue=0)
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

valikud = ["Kuller (3€)", "Kohapeal (0€)"]
selected_option = tk.StringVar()
selected_option.set("Vali üksus")

# Dropdown menüü loomine
dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()

def valik():
    print("Valitud üksus:", selected_option.get())

def show_message():
    messagebox.showinfo("Pitsa hind", "Sinu pitsa hind on: {summa}")

btn_confirm = tk.Button(aken, text="Arvuta hind", command=show_selection)
btn_confirm.pack()

aken.mainloop()