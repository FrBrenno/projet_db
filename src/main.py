import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox

import mysql.connector
from tkcalendar import DateEntry

from create_database import create_database
from import_data import import_data
from requetes import *

def afficher_popup(window_size): 
    popup = tk.Toplevel(root)
    popup_width, popup_height = window_size
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = (screen_width // 2) - (popup_width // 2)
    y = (screen_height // 2) - (popup_height // 2)
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    popup.title("Entrez les paramètres de la requête")

    return popup




class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.style = ttk.Style(self.parent)
        self.style.theme_use("clam")
        self.parent.title("Projet DB")

        window_width = self.winfo_screenwidth()//2
        window_height = self.winfo_screenheight()//2
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")


        self.inscription = tk.Button(self.parent, text="Inscription", command=self.inscription_popup)
        self.inscription.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.connexion = tk.Button(self.parent, text="profil", command=self.profil_popup)
        self.connexion.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

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
        def submit():
            dci = entry.get()
            if dci:
                popup.destroy()
                self.text.delete('1.0', tk.END)
                res = run_requete(mycursor, 1, dci).strip()
                if res == "Requête 1 :":
                    self.text.insert(tk.END, "Aucun résultat, veuillez entrer un DCI valide")
                else:
                    self.text.insert(tk.END, res)

        popup = afficher_popup((200,100))
        # Label
        tk.Label(popup, text="Entrez le DCI :").pack()
        entry = tk.Entry(popup)
        entry.insert(0, "IBUPROFENE")
        entry.pack(pady=10)
        # Submit button
        submit_button = tk.Button(popup, text="Afficher la requête", command=submit)
        submit_button.pack()

    def afficher_requete2(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, run_requete(mycursor, 2))

    def afficher_requete3(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, run_requete(mycursor, 3))

    def afficher_requete4(self):
        def submit():
            nom_medicament = entry.get()
            date = date_entry.get()

            if nom_medicament and date:
                popup.destroy()
                self.text.delete('1.0', tk.END)
                res = run_requete(mycursor, 4, [date, nom_medicament]).strip()
                if res == "Requête 4 :":
                    self.text.insert(tk.END, "Aucun résultat, veuillez entrer des données valide")
                else:
                    self.text.insert(tk.END, res)

        popup = afficher_popup((400,350))
        # Labels
        tk.Label(popup, text="Entrez le nom du médicament :").pack()
        tk.Label(popup, text="Entrez la date :").pack()
        entry = tk.Entry(popup)
        date_entry = tk.Entry(popup)
        entry.pack(pady=10)
        date_entry.pack(pady=10)
        entry.insert(0, "Doliprane")
        date_entry.insert(0, "2001-07-30")
        # Submit button
        submit_button = tk.Button(popup, text="Afficher la requête", command=submit)
        submit_button.pack()

    def afficher_requete5(self):
        """check si correct"""
        def submit():
            dci = entry.get()
            if dci:
                popup.destroy()
                self.text.delete('1.0', tk.END)
                res = run_requete(mycursor, 5, dci).strip()
                if res == "Requête 5 :":
                    self.text.insert(tk.END, "Aucun résultat, veuillez entrer un DCI valide")
                else:
                    self.text.insert(tk.END, res)

        popup = afficher_popup((200,100))
        # Label
        tk.Label(popup, text="Entrez le DCI :").pack()
        entry = tk.Entry(popup)
        entry.insert(0, "MONTELUKAST")
        entry.pack(pady=10)
        # Submit button
        submit_button = tk.Button(popup, text="Afficher la requête", command=submit)
        submit_button.pack()

    def afficher_requete6(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, run_requete(mycursor, 6))

    def afficher_requete7(self):
        """Que des noms en "T" je sais pas si c'est normal"""
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, run_requete(mycursor, 7))

    def afficher_requete8(self):
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, run_requete(mycursor, 8))

    def afficher_requete9(self):
        #TODO écrire requête
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, run_requete(mycursor, 9))

    def afficher_requete10(self):
        def submit():
            dci = entry.get()
            if dci:
                popup.destroy()
                self.text.delete('1.0', tk.END)
                res = run_requete(mycursor, 10, dci).strip()
                if res == "Requête 10 :":
                    self.text.insert(tk.END, "Aucun résultat, veuillez entrer une date valide")
                else:
                    self.text.insert(tk.END, res)

        popup = afficher_popup((200,100))
        # Label
        tk.Label(popup, text="Entrez la date :").pack()
        entry = tk.Entry(popup)
        entry.insert(0, "2001-07-30")
        entry.pack(pady=10)
        # Submit button
        submit_button = tk.Button(popup, text="Afficher la requête", command=submit)
        submit_button.pack()

    def inscription_popup(self):
        popup_window = PopupWindow(self, "Inscription")
        popup_window.update()
        width = popup_window.winfo_reqwidth()
        height = popup_window.winfo_reqheight()
        x = (self.winfo_screenwidth() - width) // 2
        y = (self.winfo_screenheight() - height) // 2
        popup_window.geometry(f"{width}x{height}+{x}+{y}")

    def profil_popup(self):
        def check_NISS():
            niss = entry.get()
            for i in niss:
                if not i.isdigit():
                    return False

            if requet_check_NISS(mycursor, niss):
                affiche_menu_patient(niss)

            else:
                """TODO popup erreur"""
                popup_error = afficher_popup((200,100))
                tk.Label(popup_error, text="NISS incorrect").pack()

        def affiche_menu_patient(niss):
            #enleve les bouton et le text
            niss_text.destroy()
            entry.destroy()
            submit_button.destroy()
            #affiche les info du patient: niss, nom, prenom, date de naissance, genre, inami du medecin, inami du pharmacien, mail et telephone
            # et rajoute 3 boutons: rafrachir, modifier le medecin et modifier le pharmacien

            info_patient = requet_info_patient(mycursor, niss) #récupère les infos du patient

            tk.Label(popup_general, text="NISS : " + str(info_patient[0])).grid(row=0, column=0)
            tk.Button(popup_general, text="Rafraichir", command=lambda: affiche_menu_patient(niss)).grid(row=0, column=1)

            tk.Label(popup_general, text="Nom : " + info_patient[1]).grid(row=1, column=0)
            tk.Label(popup_general, text="Prenom : " + info_patient[2]).grid(row=2, column=0)
            tk.Label(popup_general, text="Date de naissance : " + str(info_patient[3])).grid(row=3, column=0)
            tk.Label(popup_general, text="Genre : " + str(info_patient[4])).grid(row=4, column=0)

            tk.Label(popup_general, text="Inami du medecin : " + str(info_patient[5])).grid(row=5, column=0)
            tk.Button(popup_general, text="changer de medecin", command=lambda: changer_medecin(niss)).grid(row=5, column=1, pady=5)

            tk.Label(popup_general, text="Inami du pharmacien : " + str(info_patient[6])).grid(row=6, column=0, padx=10)
            tk.Button(popup_general, text="changer de pharmacien", command=lambda:changer_pharmacien(niss)).grid(row=6, column=1)

            if info_patient[7] == None:
                info_patient[7] = "Pas de mail"
            tk.Label(popup_general, text="Mail : " + info_patient[7]).grid(row=7, column=0)

            if info_patient[8] == None:
                info_patient[8] = "Pas de telephone"
            tk.Label(popup_general, text="Telephone : " + str(info_patient[8])).grid(row=8, column=0, pady=10)

            # 2 boutons pour évoir ses informations médicale et voir ses traitements
            tk.Button(popup_general, text="Voir ses informations médicale", command=lambda: voir_info_medical(niss)).grid(row=9, column=0)
            tk.Button(popup_general, text="Voir ses traitements", command=lambda: voir_traitements(niss)).grid(row=9, column=1)

            # 1 zone de texte pour afficher les informations médicale et les traitements en dessous de la grid
            zone_text = tk.Text(popup_general, width=300, height=50)
            zone_text.place(x=0, y=300)

            def voir_info_medical(niss_patient):
                info_medical = requet_voir_info_medical(mycursor, niss_patient)
                zone_text.delete('1.0', tk.END)
                zone_text.insert(tk.END, "Informations médicale : \n")
                zone_text.insert(tk.END, "date de diagnostique, pathologie, specialité \n")
                zone_text.insert(tk.END, info_medical)

            def voir_traitements(niss_patient):
                traitements = requet_voir_traitements(mycursor, niss_patient)
                zone_text.delete('1.0', tk.END)
                zone_text.insert(tk.END, "Traitements : \n")
                zone_text.insert(tk.END, "medecin, inami medecin, pharmacien, inami pharmacien, nom commercial du medicament, DCI, date de préscription, date de vente, durée traitement \n")
                zone_text.insert(tk.END, traitements)

        def changer_medecin(niss_patient):
            popup_changement_medecin = afficher_popup((200,200))
            popup_changement_medecin.title("Changer de medecin")
            tk.Label(popup_changement_medecin, text="Entrez le nouveau inami du medecin :").pack()
            entry_inami_medecin = tk.Entry(popup_changement_medecin)
            entry_inami_medecin.pack(pady=10)

            button_changer = tk.Button(popup_changement_medecin, text="Changer", command=lambda: envoie_requet_changer_medecin(mycursor, niss_patient, entry_inami_medecin.get()) and popup_changement_medecin.destroy())
            button_changer.pack()


            def envoie_requet_changer_medecin(mycursor, niss_patient, inami_medecin):

                if requet_check_inami_medecin(mycursor, inami_medecin):
                    requet_changer_medecin(mycursor, niss_patient, inami_medecin)
                    db.commit()
                    return True
                else:
                    popup_error = afficher_popup((200, 100))
                    tk.Label(popup_error, text="INAMI incorrect").pack()

        def changer_pharmacien(niss_patient):
            popup_changement_pharmacien = afficher_popup((200, 200))
            popup_changement_pharmacien.title("Changer de pharmacien")
            tk.Label(popup_changement_pharmacien, text="Entrez le nouveau inami du pharmacien :").pack()
            entry_inami_pharmacien = tk.Entry(popup_changement_pharmacien)
            entry_inami_pharmacien.pack(pady=10)

            button_changer = tk.Button(popup_changement_pharmacien, text="Changer", command=lambda: envoie_requet_changer_pharmacien(mycursor,niss_patient, entry_inami_pharmacien.get()) and popup_changement_pharmacien.destroy())
            button_changer.pack()

            def envoie_requet_changer_pharmacien(mycursor, niss_patient, inami_pharmacien):
                # espcace de texte modifiable pour afficher les erreurs

                if requet_check_inami_pharmacien(mycursor, inami_pharmacien):
                    requete_changer_pharmacien(mycursor, niss_patient, inami_pharmacien)
                    db.commit()
                    return True
                else:
                    popup_error = afficher_popup((200, 100))
                    tk.Label(popup_error, text="INAMI incorrect").pack()





        popup_general = afficher_popup((700,700))
        niss_text = tk.Label(popup_general, text="Entrez votre NISS de patient :")
        niss_text.pack()
        entry = tk.Entry(popup_general)
        entry.pack(pady=10)
        submit_button = tk.Button(popup_general, text="Se connecter", command=check_NISS)
        submit_button.pack()



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
    #reset_db()
    #create_database(db)

    mycursor.execute("USE mydatabase")
    #import_data(db)

    """ GUI SETUP """
    root = tk.Tk()
    MainApplication(root).grid(row=0, column=0, sticky="nsew")
    root.mainloop()
