#06.02.2025 Andre Meronen
#harjutus 6

import tkinter as tk

aken = tk.Tk()
aken.geometry("400x300")
font = "Arial 10"
padx = 5
pady = 5

nupp_00 = tk.Button(aken, text="PILT", font=font, bg="silver")
nupp_00.grid(row=1, column=0, rowspan=5, columnspan=2, padx=padx, pady=pady, sticky="nsew")

label=tk.Label(aken, text="Palun sisestage oma andmed: ", font=font).pack()
label.grid(row=0, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")

nimi=tk.Label(aken, text="Palun sisestage oma nimi: ", font=font).pack()
nimi.grid(row=1, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")

silmad=tk.Label(aken, text="Palun sisestage oma silma värv: ", font=font).pack()
silmad.grid(row=2, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")

pikkus=tk.Label(aken, text="Palun sisestage oma pikkus: ", font=font).pack()
pikkus.grid(row=3, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")

kaal=tk.Label(aken, text="Palun sisestage oma kaal: ", font=font).pack()
kaal.grid(row=4, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")

cm=tk.Label(aken, text="cm", font=font).pack()
cm.grid(row=4, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")


kg=tk.Label(aken, text="kg", font=font).pack()
kg.grid(row=4, column=2, columnspan=3, padx=padx, pady=pady, sticky="nsew")


#sisestused
sisestus1=tk.entry(aken).grid(row=1,column=3,padx=padx,pady=pady,sticky="nsew")
sisestus1=tk.entry(aken).grid(row=2,column=3,padx=padx,pady=pady,sticky="nsew")
sisestus1=tk.entry(aken).grid(row=3,column=3,padx=padx,pady=pady,sticky="nsew")
sisestus1=tk.entry(aken).grid(row=4,column=3,padx=padx,pady=pady,sticky="nsew")

nupp_13 = tk.Button(aken, text="Salvesta", font=font)
nupp_13.grid(row=5, column=3, padx=padx, pady=pady, sticky="nsew")



# Nuppude seadistamine
aken.grid_columnconfigure(0, weight=2)


aken.mainloop()