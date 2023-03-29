import tkinter as tk
import tkinter.ttk as ttk
import pyperclip
from tkinter import filedialog
from tkinter import messagebox
import random
import string
import os

def generate_password(length, include_digits=False, include_uppercase=False, include_special=False):
    # Créer une liste de caractères possibles en fonction des options choisies
    chars = string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_special:
        chars += string.punctuation

    # Générer un mot de passe aléatoire en utilisant la liste de caractères possibles
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def export_password(password):
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichier texte", "*.txt")])
    if filename:
        with open(filename, "w") as f:
            f.write(password)

def generate_password_gui():
    # Créer une fenêtre Tkinter
    window = tk.Tk()
    window.title("Générateur de mot de passe | Shoqapique#0001 on Discord")
    # Ajouter des widgets pour les options de mot de passe
    length_label = tk.Label(window, text="Nombre de caractères :")
    length_label.grid(row=0, column=0, padx=5, pady=5)
    length_entry = tk.Entry(window)
    length_entry.grid(row=0, column=1, padx=5, pady=5)
    digits_var = tk.BooleanVar()
    digits_check = tk.Checkbutton(window, text="Chiffres", variable=digits_var)
    digits_check.grid(row=1, column=0, padx=5, pady=5)
    uppercase_var = tk.BooleanVar()
    uppercase_check = tk.Checkbutton(window, text="Majuscules", variable=uppercase_var)
    uppercase_check.grid(row=1, column=1, padx=5, pady=5)
    special_var = tk.BooleanVar()
    special_check = tk.Checkbutton(window, text="Caractères spéciaux", variable=special_var)
    special_check.grid(row=1, column=2, padx=5, pady=5)

    # Ajouter un widget pour afficher le mot de passe généré
    password_frame = ttk.Frame(window)
    password_frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
    password_label = tk.Label(password_frame, text="")
    password_label.pack(side=tk.LEFT)
    copy_button = ttk.Button(password_frame, text="Copier", command=lambda: pyperclip.copy(password_label.cget("text")) if password_label.cget("text") else None, state=tk.DISABLED)
    copy_button.pack(side=tk.LEFT)
    export_button = ttk.Button(password_frame, text="Exporter sous TXT", command=lambda: export_password(password_label.cget("text")) if password_label.cget("text") else None, state=tk.DISABLED)
    export_button.pack(side=tk.LEFT)

    # Ajouter un bouton pour générer le mot de passe
    def generate():
        length = int(length_entry.get())
        include_digits = digits_var.get()
        include_uppercase = uppercase_var.get()
        include_special = special_var.get()
        password = generate_password(length, include_digits, include_uppercase, include_special)
        password_label.config(text=password)
        copy_button.config(state=tk.NORMAL if password else tk.DISABLED)
        export_button.config(state=tk.NORMAL if password else tk.DISABLED)

    generate_button = tk.Button(window, text="Générer", command=generate, state=tk.DISABLED)
    generate_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)


    # Vérifier que les options de mot de passe sont correctement définies
    def check_options():
        length = length_entry.get()
        digits = digits_var.get()
        uppercase = uppercase_var.get()
        special = special_var.get()
        if length.isdigit() and int(length) > 0 and (digits or uppercase or special):
            generate_button.config(state=tk.NORMAL)
        else:
            generate_button.config(state=tk.DISABLED)

    length_entry.bind("<KeyRelease>", lambda event: check_options())
    digits_var.trace_add("write", lambda *args: check_options())
    uppercase_var.trace_add("write", lambda *args: check_options())
    special_var.trace_add("write", lambda *args: check_options())

# Afficher la fenêtre Tkinter
    window.mainloop()


generate_password_gui()