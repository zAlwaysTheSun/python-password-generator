import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import random
import string

# Génère un mot de passe aléatoire en fonction des options sélectionnées
def generate_password():
    length = int(length_entry.get())
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    chars = ""
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Erreur", "Veuillez sélectionner au moins une option.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Enregistre le mot de passe dans un fichier TXT crypté
def save_password():
    password = password_entry.get()
    name = name_entry.get()

    if not password or not name:
        messagebox.showerror("Erreur", "Veuillez saisir un nom et un mot de passe.")
        return

    # Crypte le mot de passe
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())

    with open("passwords.txt", "a") as file:
        file.write(f"{name}: {encrypted_password.decode()}\n")

    messagebox.showinfo("Succès", "Le mot de passe a été enregistré avec succès.")

# Crée une fenêtre
window = tk.Tk()
window.title("Générateur de mot de passe")
window.geometry("400x250")

# Étiquette et champ pour le nom du mot de passe
name_label = tk.Label(window, text="Nom:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Longueur du mot de passe
length_label = tk.Label(window, text="Longueur:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.insert(tk.END, "8")  # Longueur par défaut
length_entry.pack()

# Options de composition du mot de passe
options_frame = tk.LabelFrame(window, text="Options")
options_frame.pack(fill=tk.BOTH, expand=True)

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(options_frame, text="Minuscules", variable=lowercase_var)
lowercase_check.pack(anchor=tk.W)

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(options_frame, text="Majuscules", variable=uppercase_var)
uppercase_check.pack(anchor=tk.W)

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(options_frame, text="Chiffres", variable=digits_var)
digits_check.pack(anchor=tk.W)

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(options_frame, text="Caractères spéciaux", variable=special_chars_var)
special_chars_check.pack(anchor=tk.W)

# Étiquette et champ pour le mot de passe généré
password_label = tk.Label(window, text="Mot de passe:")
password_label.pack()
password_entry = tk.Entry(window)
password_entry.pack()

# Bouton pour générer un mot de passe
generate_button = tk.Button(window, text="Générer", command=generate_password)
generate_button.pack()

# Bouton pour enregistrer le mot de passe
save_button = tk.Button(window, text="Enregistrer", command=save_password)
save_button.pack()

# Lance la boucle principale de l'interface graphique
window.mainloop()
