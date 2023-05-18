import tkinter as tk
from datetime import datetime
from tkinter import ttk
import ctypes
import mysql.connector
import sys

from tkcalendar import DateEntry

from create_database import create_database
from import_data import import_data
from requetes import *

screen_width = 0
screen_height = 0
os_name = ""

# get the screen resolution of the device
if sys.platform.startswith('darwin'):
    print("Running on Mac")
    os_name = "Mac"
    screen_width = 2560
    screen_height = 1600
elif sys.platform.startswith('win'):
    print("Running on Windows")
    os_name = "Windows"
    usr32 = ctypes.windll.user32
    # get the screen resolution of the device
    screen_width = usr32.GetSystemMetrics(0)
    screen_height = usr32.GetSystemMetrics(1)

# set the dimensions of the window
window_width = 510
window_height = 400

# calculate the x and y coordinates of the window
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")

        self.parent.title("Projet DB")

        # set the geometry of the window to position it in the center
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.inscription = tk.Button(self.parent, text="Inscription", command=self.inscription_popup)
        self.inscription.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.text = tk.Text(self.parent, height=40)
        self.text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=5)

        self.button1 = ttk.Button(self.parent, text="requete1", command=self.afficher_requete1)
        self.button1.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.button2 = ttk.Button(self.parent, text="requete2", command=self.afficher_requete2)
        self.button2.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.button3 = ttk.Button(self.parent, text="requete3", command=self.afficher_requete3)
        self.button3.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        self.button4 = ttk.Button(self.parent, text="requete4", command=self.afficher_requete4)
        self.button4.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

        self.button5 = ttk.Button(self.parent, text="requete5", command=self.afficher_requete5)
        self.button5.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")

        self.button6 = ttk.Button(self.parent, text="requete6", command=self.afficher_requete6)
        self.button6.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.button7 = ttk.Button(self.parent, text="requete7", command=self.afficher_requete7)
        self.button7.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        self.button8 = ttk.Button(self.parent, text="requete8", command=self.afficher_requete8)
        self.button8.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        self.button9 = ttk.Button(self.parent, text="requete9", command=self.afficher_requete9)
        self.button9.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

        self.button10 = ttk.Button(self.parent, text="requete10", command=self.afficher_requete10)
        self.button10.grid(row=3, column=4, padx=10, pady=10, sticky="nsew")

        # configure grid weights to make the text widget expand to fill any extra space
        self.parent.columnconfigure(0, weight=1)
        self.parent.columnconfigure(1, weight=1)
        self.parent.columnconfigure(2, weight=1)
        self.parent.columnconfigure(3, weight=1)
        self.parent.columnconfigure(4, weight=1)
        self.parent.rowconfigure(1, weight=1)

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

    def inscription_popup(self):
        popup_window = PopupWindow(self, "Inscription")
        # # Save a reference to the popup window instance to access it later
        # self.popup_window = popup_window
        # popup_window.update()
        # width = popup_window.winfo_reqwidth()
        # height = popup_window.winfo_reqheight()
        # x = (self.winfo_screenwidth() - width) // 2
        # y = (self.winfo_screenheight() - height) // 2
        # popup_window.geometry(f"{width}x{height}+{x}+{y}")

    def handle_submitted_data(self, data):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, insert_patient(mycursor, data))
        db.commit()


class PopupWindow(tk.Toplevel):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.parent = parent
        self.title(title)

        self.type = tk.StringVar(value="patient")
        self.type_option_1 = tk.Radiobutton(self, text="Patient", variable=self.type, value="patient")
        self.type_option_2 = tk.Radiobutton(self, text="Médecin", variable=self.type, value="medecin")
        self.type_option_3 = tk.Radiobutton(self, text="Pharmacien", variable=self.type, value="pharmacien")
        self.type_option_1.grid(row=0, column=0, padx=10, pady=10)
        self.type_option_2.grid(row=0, column=1, padx=10, pady=10)
        self.type_option_3.grid(row=0, column=2, padx=10, pady=10)

        self.create_form()
        self.type.trace("w", self.create_form)

        self.button_submit = tk.Button(self, text="Enregistrer", command=self.submit_patient)
        self.button_submit.grid(row=11, column=0, columnspan=3, padx=10, pady=10)


        self.parent.columnconfigure(0, weight=1)
        self.parent.columnconfigure(1, weight=1)
        self.parent.columnconfigure(2, weight=1)


    def create_form(self, *args):
        # Clear existing form elements
        for widget in self.winfo_children():
            # Do not delete RadioButtons
            if not isinstance(widget, tk.Radiobutton):
                widget.destroy()

        selected_type = self.type.get()
        if selected_type == "patient":
            self.label_niss = tk.Label(self, text="NISS:")
            self.label_niss.grid(row=1, column=0, padx=10, pady=10)
            self.entry_niss = tk.Entry(self)
            self.entry_niss.grid(row=1, column=1, padx=10, pady=10)

            self.label_medecin = tk.Label(self, text="Medecin:")
            self.label_medecin.grid(row=2, column=0, padx=10, pady=10)
            self.entry_medecin = tk.Entry(self)
            self.entry_medecin.grid(row=2, column=1, padx=10, pady=10)

            self.label_inami_medecin = tk.Label(self, text="INAMI Medecin:")
            self.label_inami_medecin.grid(row=3, column=0, padx=10, pady=10)
            self.entry_inami_medecin = tk.Entry(self)
            self.entry_inami_medecin.grid(row=3, column=1, padx=10, pady=10)

            self.label_pharmacien = tk.Label(self, text="Pharmacien:")
            self.label_pharmacien.grid(row=4, column=0, padx=10, pady=10)
            self.entry_pharmacien = tk.Entry(self)
            self.entry_pharmacien.grid(row=4, column=1, padx=10, pady=10)

            self.label_inami_pharmacien = tk.Label(self, text="INAMI Pharmacien:")
            self.label_inami_pharmacien.grid(row=5, column=0, padx=10, pady=10)
            self.entry_inami_pharmacien = tk.Entry(self)
            self.entry_inami_pharmacien.grid(row=5, column=1, padx=10, pady=10)

            self.label_medicament_nom_commercial = tk.Label(self, text="Nom commercial medicament:")
            self.label_medicament_nom_commercial.grid(row=6, column=0, padx=10, pady=10)
            self.entry_medicament_nom_commercial = tk.Entry(self)
            self.entry_medicament_nom_commercial.grid(row=6, column=1, padx=10, pady=10)

            self.label_dci = tk.Label(self, text="DCI:")
            self.label_dci.grid(row=7, column=0, padx=10, pady=10)
            self.entry_dci = tk.Entry(self)
            self.entry_dci.grid(row=7, column=1, padx=10, pady=10)

            self.label_date_presciption = tk.Label(self, text="Date de prescription:")
            self.label_date_presciption.grid(row=8, column=0, padx=10, pady=10)
            self.entry_date_presciption = DateEntry(self, date_pattern="dd/mm/yyyy")
            self.entry_date_presciption.grid(row=8, column=1, padx=10, pady=10)

            self.label_date_vente = tk.Label(self, text="Date de vente:")
            self.label_date_vente.grid(row=9, column=0, padx=10, pady=10)
            self.entry_date_vente = DateEntry(self, date_pattern="dd/mm/yyyy")
            self.entry_date_vente.grid(row=9, column=1, padx=10, pady=10)

            self.label_duree_traitement = tk.Label(self, text="Duree de traitement:")
            self.label_duree_traitement.grid(row=10, column=0, padx=10, pady=10)
            self.entry_duree_traitement = tk.Entry(self)
            self.entry_duree_traitement.grid(row=10, column=1, padx=10, pady=10)

        elif selected_type == "medecin":
            self.label_msg = tk.Label(self, text="Medecin")
            self.label_msg.grid(row=1, column=0, padx=10, pady=10)
        else:
            self.label_msg = tk.Label(self, text="Pharmacien")
            self.label_msg.grid(row=1, column=0, padx=10, pady=10)

    def submit_patient(self):
        # Call a method in MainApplication to handle the submitted data
        date_prescription = datetime.strftime(self.entry_date_presciption.get_date(), "%Y-%m-%d")
        date_vente = datetime.strftime(self.entry_date_vente.get_date(), "%Y-%m-%d")
        self.parent.handle_submitted_data(
            [self.entry_niss.get(),
             self.entry_medecin.get(),
             self.entry_inami_medecin.get(),
             self.entry_pharmacien.get(),
             self.entry_inami_pharmacien.get(),
             self.entry_medicament_nom_commercial.get(),
             self.entry_dci.get(),
             date_prescription,
             date_vente,
             self.entry_duree_traitement.get()
             ]
        )
        self.destroy()


def reset_db():
    # Drop all tables
    mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
    db.commit()


if __name__ == "__main__":
    """ DATABASE SETUP """

    db = mysql.connector.connect(
        host="localhost",
        user="alex",
        passwd="alex",
        auth_plugin='mysql_native_password'
    )
    mycursor = db.cursor()
    create_database(db)

    mycursor.execute("USE mydatabase")
    import_data(db, os_name)

    """ GUI SETUP """
    root = tk.Tk()
    MainApplication(root).grid(row=0, column=0, sticky="nsew")
    root.mainloop()
