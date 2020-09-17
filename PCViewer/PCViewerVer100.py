import datetime
import subprocess
import time
import tkinter as tk  # ładowanie modułu tkinter (w wersji 3+)
from tkinter import *
from tkinter import messagebox


date = datetime.datetime.now().strftime('%Y-%m-%d')

print(date)


def Close():

 tk._exit()

def Start():

  subprocess.call([r'tcl\tzdata\spec.bat'])
  messagebox.showinfo(title="Info!", message="Raport PCInfo.csv został zapisany w folderze głównym programu .")

if date > "2020-09-24":
    messagebox.showinfo(title="Demo!", message="To była wersja testowa aplikacji. Dostęp wyłączono 24.09.2020")
    tk._exit()

window = tk.Tk()  # tworzenie okna głównego
messagebox.showinfo(title = "Demo!",message = "To wersja testowa aplikacji. Dostęp zostanie wyłączony dnia 24.09.2020")
messagebox.showinfo(title = "Demo!",message = "Jest to wersja 1.0.0 Jest możliwość rozbudowy o dalsze funkcje. W razie pytań prosze o telefon 796 852 909")
window.title("PCSpecViewer ver:1.0.0")  # ustawienie tytułu okna głównego
# tworzenie kontrolki typu label
text = tk.StringVar()
label = tk.Label(window, textvariable=text, padx=20, pady=20)
label.pack()  # podpinanie kontrolki pod okno

description = tk.Label(text="Aplikacja umożliwia pobranie specyfikacji tego komputera oraz zapisanie jej do pliku.").pack()
description = tk.Label(text="Kliknij [Start] aby rozpocząć proces wyszukiwania.").pack()
description = tk.Label(text="\n").pack()

name = "coś"

StartButton = tk.Button(window, text="Start", width=20, command=Start)
StartButton.pack(side=LEFT)
CloseButton = tk.Button(window, text="Zakończ", width=20, command=Close)
CloseButton.pack(side=RIGHT)
description = tk.Label(text="\n").pack()
description = tk.Label(text="\n").pack()
description = tk.Label(text="Copyright © by HardwareTech.pl").pack()
tk.mainloop()  # wywołanie pętli komunikatów

