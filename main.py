import tkinter as tk

from tkinter import ttk
import sys
import ctypes
from requetes import *

usr32 = ctypes.windll.user32
width = usr32.GetSystemMetrics(0)
height = usr32.GetSystemMetrics(1)
res = str(width) + "x" + str(height)
print(width, height)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")

        self.parent.title("Main Application")

        self.parent.geometry(res)

        self.label = ttk.Label(self.parent, text="Hello World!")
        self.label.pack(padx=10, pady=10)

        self.text = tk.Text(self.parent, height=30, width=80)
        self.text.pack(padx=10, pady=100, side="right", anchor="e")

        self.button = ttk.Button(self.parent, text="requete1", command=self.afficher_requete1)
        self.button.pack(padx=10, pady=0, side=tk.LEFT)

        self.button = ttk.Button(self.parent, text="requete2", command=self.afficher_requete2)
        self.button.pack(padx=10, pady=0, side=tk.LEFT)

        self.button = ttk.Button(self.parent, text="requete3", command=self.afficher_requete3)
        self.button.pack(padx=10, pady=0, side=tk.LEFT)





    def open_new_window(self):
        self.new_window = tk.Toplevel(self.parent)
        self.app = NewWindow(self.new_window)

    def afficher_requete1(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete1())

    def afficher_requete2(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete2())
    def afficher_requete3(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete3())


class NewWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")

        self.parent.title("New Window")
        self.parent.geometry(res)

        self.label = ttk.Label(self.parent, text="Hello World!")
        self.label.pack(padx=10, pady=10)

        self.button = ttk.Button(self.parent, text="Close Window", command=self.close_window)
        self.button.pack(padx=10, pady=10)

    def close_window(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
