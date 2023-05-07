import tkinter as tk
from tkinter import ttk
import ctypes
import mysql.connector

from create_database import create_database
from import_data import import_data
from requetes import *

usr32 = ctypes.windll.user32
# get the screen resolution of the device
screen_width = usr32.GetSystemMetrics(0)
screen_height = usr32.GetSystemMetrics(1)

# set the dimensions of the window
window_width = 510
window_height = 300

# calculate the x and y coordinates of the window
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)



db = mysql.connector.connect(
    host="localhost",
    user="alex",
    passwd="alex"
)
mycursor = db.cursor()
mycursor.execute("USE mydatabase")


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")

        self.parent.title("Projet DB")

        # set the geometry of the window to position it in the center
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.text = tk.Text(self.parent, height=40)
        self.text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=5)

        self.button1 = ttk.Button(self.parent, text="requete1", command=self.afficher_requete1)
        self.button1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.button2 = ttk.Button(self.parent, text="requete2", command=self.afficher_requete2)
        self.button2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.button3 = ttk.Button(self.parent, text="requete3", command=self.afficher_requete3)
        self.button3.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        self.button4 = ttk.Button(self.parent, text="requete4", command=self.afficher_requete4)
        self.button4.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

        self.button5 = ttk.Button(self.parent, text="requete5", command=self.afficher_requete5)
        self.button5.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

        self.button6 = ttk.Button(self.parent, text="requete6", command=self.afficher_requete6)
        self.button6.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.button7 = ttk.Button(self.parent, text="requete7", command=self.afficher_requete7)
        self.button7.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.button8 = ttk.Button(self.parent, text="requete8", command=self.afficher_requete8)
        self.button8.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        self.button9 = ttk.Button(self.parent, text="requete9", command=self.afficher_requete9)
        self.button9.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

        self.button10 = ttk.Button(self.parent, text="requete10", command=self.afficher_requete10)
        self.button10.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")

        # configure grid weights to make the text widget expand to fill any extra space
        self.parent.columnconfigure(1, weight=1)
        self.parent.rowconfigure(0, weight=1)

    def afficher_requete1(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete1(mycursor))

    def afficher_requete2(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete2(mycursor))

    def afficher_requete3(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete3(mycursor))

    def afficher_requete4(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete4(mycursor))

    def afficher_requete5(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete5(mycursor))

    def afficher_requete6(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete6(mycursor))

    def afficher_requete7(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete7(mycursor))

    def afficher_requete8(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete8(mycursor))

    def afficher_requete9(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete9(mycursor))

    def afficher_requete10(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, requete10(mycursor))



if __name__ == "__main__":
    """ DATABASE SETUP """

    # create_database(db)
    # import_data(db)

    """ GUI SETUP """
    root = tk.Tk()
    MainApplication(root).grid(row=0, column=0, sticky="nsew")
    root.mainloop()
