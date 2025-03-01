#05.02 2025 Andre Meronen
#harjutus 4

import tkinter as tk

def kuva_varv(v):
    vastus.config=()

def main():
    aken = tk.Tk()
    aken.geometry("400x100")
    aken.title="Värvi nupud"

    nupp1 = tk.Button(aken, bg="red", fg="white", font=("Arial", 16))
    nupp2 = tk.Button(aken, bg="orange", fg="white", font=("Arial", 16))
    nupp3 = tk.Button(aken, bg="green", fg="black", font=("Arial", 16))
    nupp4 = tk.Button(aken, bg="blue", fg="white", font=("Arial", 16))
    nupp5 = tk.Button(aken, bg="purple", fg="black", font=("Arial", 16))
    vastus = tk.Label(aken,text=f"Siia tuleb vastus")
    vastus.pack(side="bottom", expand="true", fill="x", anchor="center")
    nupp1.pack(side="right", expand="true", fill="x")
    nupp2.pack(side="right",expand="true", fill="x")
    nupp3.pack(side="right", expand="true", fill="x")
    nupp4.pack(side="right",expand="true", fill="x")
    nupp5.pack(side="right",expand="true", fill="x")
    
    
    aken.mainloop()

if __name__ == "__main__":
    main()

