import ctypes
import sys
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox

import mysql.connector
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
        popup_window.update()
        width = popup_window.winfo_reqwidth()
        height = popup_window.winfo_reqheight()
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        popup_window.geometry(f"{width}x{height}+{x}+{y}")

    def handle_submitted_data(self, data, type):
        self.text.delete('1.0', tk.END)
        if type == "patient":
            self.text.insert(tk.END, insert_patient(mycursor, data))
        elif type == "medecin":
            self.text.insert(tk.END, insert_medecin(mycursor, data))
        elif type == "pharmacien":
            self.text.insert(tk.END, insert_pharmacien(mycursor, data))
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

        self.parent.columnconfigure(0, weight=1)
        self.parent.columnconfigure(1, weight=1)
        self.parent.columnconfigure(2, weight=1)

    def validate_data(self, form_data, type):
        if type == "patient":
            # Only mail and telephone could be empty
            for i in range(0, len(form_data) - 2):
                if form_data[i] == "":
                    messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoire")
                    return False
                if not form_data[0].isnumeric():
                    messagebox.showerror("Erreur", "Veuillez entrer un numéro de registre national valide")
                    return False
                elif not form_data[5].isnumeric():
                    messagebox.showerror("Erreur", "Veuillez entrer un INAMI médecin valide")
                    return False
                elif not form_data[6].isnumeric():
                    messagebox.showerror("Erreur", "Veuillez entrer un INAMI pharmacien valide")
                    return False
                elif not form_data[8].isnumeric():
                    messagebox.showerror("Erreur", "Veuillez entrer un numéro de téléphone valide")
                    return False

        elif type == "medecin":
            # Only mail could be empty
            for i in range(0, len(form_data) - 1):
                if form_data[i] == "":
                    messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoire")
                    return False
                if not form_data[0].isnumeric():
                    messagebox.showerror("Erreur", "Veuillez entrer un INAMI valide")
                    return False
                elif not form_data[3].isnumeric():
                    messagebox.showerror("Erreur", "Veuillez entrer un numéro de téléphone valide")
                    return False
        elif type == "pharmacien":
            # Only mail could be empty
            for i in range(0, len(form_data) - 1):
                if form_data[i] == "":
                    messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoire")
                    return False
                elif not form_data[0].isnumeric():
                    messagebox.showerror("Erreur", "Veuillez entrer un INAMI valide")
                    return False
                elif not form_data[3].isnumeric():
                    messagebox.showerror("Erreur", "Veuillez entrer un numéro de téléphone valide")
                    return False
        return True

    def create_form(self, *args):
        # Clear existing form elements
        for widget in self.winfo_children():
            # Do not delete RadioButtons
            if not isinstance(widget, tk.Radiobutton):
                widget.destroy()

        selected_type = self.type.get()
        if selected_type == "patient":
            self.label_niss_patient = tk.Label(self, text="NISS(*):")
            self.label_niss_patient.grid(row=1, column=0, padx=10, pady=10)
            self.entry_niss_patient = tk.Entry(self)
            self.entry_niss_patient.grid(row=1, column=1, padx=10, pady=10)

            self.label_nom_patient = tk.Label(self, text="Nom(*):")
            self.label_nom_patient.grid(row=2, column=0, padx=10, pady=10)
            self.entry_nom_patient = tk.Entry(self)
            self.entry_nom_patient.grid(row=2, column=1, padx=10, pady=10)

            self.label_prenom_patient = tk.Label(self, text="Prénom(*):")
            self.label_prenom_patient.grid(row=3, column=0, padx=10, pady=10)
            self.entry_prenom_patient = tk.Entry(self)
            self.entry_prenom_patient.grid(row=3, column=1, padx=10, pady=10)

            self.label_date_naissance_patient = tk.Label(self, text="Date de naissance(*):")
            self.label_date_naissance_patient.grid(row=4, column=0, padx=10, pady=10)
            self.entry_date_naissance_patient = DateEntry(self)
            self.entry_date_naissance_patient.grid(row=4, column=1, padx=10, pady=10)

            self.label_genre_patient = tk.Label(self, text="Genre(*):")
            self.label_genre_patient.grid(row=5, column=0, padx=10, pady=10)
            self.entry_genre_patient = tk.Entry(self)
            self.entry_genre_patient.grid(row=5, column=1, padx=10, pady=10)

            self.label_inami_medecin_patient = tk.Label(self, text="INAMI du médecin traitant(*):")
            self.label_inami_medecin_patient.grid(row=6, column=0, padx=10, pady=10)
            self.entry_inami_medecin_patient = tk.Entry(self)
            self.entry_inami_medecin_patient.grid(row=6, column=1, padx=10, pady=10)

            self.label_inami_pharmacien_patient = tk.Label(self, text="INAMI du pharmacien(*):")
            self.label_inami_pharmacien_patient.grid(row=7, column=0, padx=10, pady=10)
            self.entry_inami_pharmacien_patient = tk.Entry(self)
            self.entry_inami_pharmacien_patient.grid(row=7, column=1, padx=10, pady=10)

            self.label_mail_patient = tk.Label(self, text="Mail:")
            self.label_mail_patient.grid(row=8, column=0, padx=10, pady=10)
            self.entry_mail_patient = tk.Entry(self)
            self.entry_mail_patient.grid(row=8, column=1, padx=10, pady=10)

            self.label_telephone_patient = tk.Label(self, text="Téléphone:")
            self.label_telephone_patient.grid(row=9, column=0, padx=10, pady=10)
            self.entry_telephone_patient = tk.Entry(self)
            self.entry_telephone_patient.grid(row=9, column=1, padx=10, pady=10)

        elif selected_type == "medecin":
            self.label_nom_medecin = tk.Label(self, text="Nom(*):")
            self.label_nom_medecin.grid(row=2, column=0, padx=10, pady=10)
            self.entry_nom_medecin = tk.Entry(self)
            self.entry_nom_medecin.grid(row=2, column=1, padx=10, pady=10)

            self.label_inami_medecin = tk.Label(self, text="INAMI(*):")
            self.label_inami_medecin.grid(row=3, column=0, padx=10, pady=10)
            self.entry_inami_medecin = tk.Entry(self)
            self.entry_inami_medecin.grid(row=3, column=1, padx=10, pady=10)

            self.label_specialite_medecin = tk.Label(self, text="Spécialité(*):")
            self.label_specialite_medecin.grid(row=4, column=0, padx=10, pady=10)
            self.entry_specialite_medecin = tk.Entry(self)
            self.entry_specialite_medecin.grid(row=4, column=1, padx=10, pady=10)

            self.label_telephone_medecin = tk.Label(self, text="Telephone(*):")
            self.label_telephone_medecin.grid(row=5, column=0, padx=10, pady=10)
            self.entry_telephone_medecin = tk.Entry(self)
            self.entry_telephone_medecin.grid(row=5, column=1, padx=10, pady=10)

            self.label_mail_medecin = tk.Label(self, text="Mail:")
            self.label_mail_medecin.grid(row=6, column=0, padx=10, pady=10)
            self.entry_mail_medecin = tk.Entry(self)
            self.entry_mail_medecin.grid(row=6, column=1, padx=10, pady=10)
        else:
            self.label_nom_pharmacien = tk.Label(self, text="Nom(*):")
            self.label_nom_pharmacien.grid(row=2, column=0, padx=10, pady=10)
            self.entry_nom_pharmacien = tk.Entry(self)
            self.entry_nom_pharmacien.grid(row=2, column=1, padx=10, pady=10)

            self.label_inami_pharmacien = tk.Label(self, text="INAMI(*):")
            self.label_inami_pharmacien.grid(row=3, column=0, padx=10, pady=10)
            self.entry_inami_pharmacien = tk.Entry(self)
            self.entry_inami_pharmacien.grid(row=3, column=1, padx=10, pady=10)

            self.label_telephone_pharmacien = tk.Label(self, text="Telephone(*):")
            self.label_telephone_pharmacien.grid(row=4, column=0, padx=10, pady=10)
            self.entry_telephone_pharmacien = tk.Entry(self)
            self.entry_telephone_pharmacien.grid(row=4, column=1, padx=10, pady=10)

            self.label_mail_pharmacien = tk.Label(self, text="Mail:")
            self.label_mail_pharmacien.grid(row=5, column=0, padx=10, pady=10)
            self.entry_mail_pharmacien = tk.Entry(self)
            self.entry_mail_pharmacien.grid(row=5, column=1, padx=10, pady=10)

        self.button_submit = tk.Button(self, text="Enregistrer", command=self.submit)
        self.button_submit.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    def submit(self):
        if self.type.get() == "patient":
            self.submit_patient()
        elif self.type.get() == "medecin":
            self.submit_medecin()
        else:
            self.submit_pharmacien()

    def submit_patient(self):
        date_naissance = datetime.strftime(self.entry_date_naissance_patient.get_date(), "%Y-%m-%d")
        form_data = [self.entry_niss_patient.get(),
                     self.entry_nom_patient.get().upper(),
                     self.entry_prenom_patient.get().capitalize(),
                     date_naissance,
                     self.entry_genre_patient.get(),
                     self.entry_inami_medecin_patient.get(),
                     self.entry_inami_pharmacien_patient.get(),
                     self.entry_mail_patient.get(),
                     self.entry_telephone_patient.get()
                     ]

        data_validated = self.validate_data(form_data, "patient")

        if data_validated:
            self.parent.handle_submitted_data(form_data, "patient")
            self.destroy()

    def submit_medecin(self):
        form_data = [self.entry_inami_medecin.get().capitalize(),
                     self.entry_nom_medecin.get().upper(),
                     self.entry_specialite_medecin.get(),
                     self.entry_telephone_medecin.get(),
                     self.entry_mail_medecin.get()
                     ]

        data_validated = self.validate_data(form_data, "medecin")

        if data_validated:
            self.parent.handle_submitted_data(form_data, "medecin")
            self.destroy()

    def submit_pharmacien(self):
        form_data = [self.entry_inami_pharmacien.get(),
                     self.entry_nom_pharmacien.get(),
                     self.entry_telephone_pharmacien.get(),
                     self.entry_mail_pharmacien.get()
                     ]

        data_validated = self.validate_data(form_data, "pharmacien")
        if data_validated:
            self.parent.handle_submitted_data(form_data, "pharmacien")
            self.destroy()


def reset_db():
    print("DELETING DATABASE...")
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
    reset_db()
    create_database(db)

    mycursor.execute("USE mydatabase")
    import_data(db, os_name)

    """ GUI SETUP """
    root = tk.Tk()
    MainApplication(root).grid(row=0, column=0, sticky="nsew")
    root.mainloop()
