#06.02.2025 Andre Meronen
#harjutus 7

import tkinter as tk

def valideeriTeksti(*args):
    text = entry_var.get()
    if len(text) == 11:
        sugunr=int(text[0])
        if sugunr%2==0:
            sugu="naine"
        else:
            sugu="mees"
        sp=f"{text[5]}{text[6]}.{text[3]}{text[4]}.{text[1]}{text[2]}"
        validation_label.config(text=f"Sugu: {sugu}\nSünnipäev {sp}", fg="green")
    else:
        validation_label.config(text="Sisesta 11 märki!", fg="red")

aken = tk.Tk()
aken.title("Validaator")
aken.geometry("400x300")

label=tk.Label(aken, text="Isikukood", font="Arial 16").pack()

entry_var = tk.StringVar()
entry_var.trace_add("write", valideeriTeksti)

entry = tk.Entry(aken, textvariable=entry_var)
entry.pack()

validation_label = tk.Label(aken, text="Isikukood peab olema 11 märki pikk!", fg="red")
validation_label.pack()

aken.mainloop()