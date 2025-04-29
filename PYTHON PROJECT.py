import tkinter as tk
import random

class MatematikaIgra:
    def __init__(self, root):
        self.root = root
        self.root.title("Matematika")
        self.bodovi = 0
        self.pitanje_broj = 0
        self.ukupno_pitanja = 10

        self.zadatak_labela = tk.Label(root, text="", font=("Arial", 20))
        self.zadatak_labela.pack(pady=20)

        self.odgovor_entry = tk.Entry(root, font=("Arial", 16))
        self.odgovor_entry.pack()

        self.provjeri_btn = tk.Button(root, text="Provjeri", command=self.provjeri_odgovor)
        self.provjeri_btn.pack(pady=10)

        self.rezultat_labela = tk.Label(root, text="", font=("Arial", 16))
        self.rezultat_labela.pack()

        self.generisi_novi_zadatak()

    def generisi_novi_zadatak(self):
        operacije = ['+', '-', '*', '/']
        self.op = random.choice(operacije)
        self.a = random.randint(1, 20)
        self.b = random.randint(1, 20)

        if self.op == '/':
            self.a = self.a * self.b

        self.tacan_odgovor = round(eval(f"{self.a} {self.op} {self.b}"), 2)
        self.zadatak_labela.config(text=f"{self.a} {self.op} {self.b} = ?")
        self.odgovor_entry.delete(0, tk.END)
        self.rezultat_labela.config(text="")

    def provjeri_odgovor(self):
        pokusaj = self.odgovor_entry.get()
        try:
            if abs(float(pokusaj) - self.tacan_odgovor) < 0.01:
                self.bodovi += 1
                self.rezultat_labela.config(text="Tačno!", fg="green")
            else:
                self.rezultat_labela.config(
                    text=f"Netačno! Tačno je: {self.tacan_odgovor}", fg="red"
                )
        except:
            self.rezultat_labela.config(text="Unesi broj.", fg="orange")
            return

        self.pitanje_broj += 1
        if self.pitanje_broj < self.ukupno_pitanja:
            self.root.after(1500, self.generisi_novi_zadatak)
        else:
            self.root.after(2000, self.kraj_igre)

    def kraj_igre(self):
        self.zadatak_labela.config(
            text=f"Igra gotova! Bodovi: {self.bodovi}/{self.ukupno_pitanja}"
        )
        self.odgovor_entry.destroy()
        self.provjeri_btn.destroy()

root = tk.Tk()
app = MatematikaIgra(root)
root.mainloop()
