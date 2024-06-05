from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import subprocess
import os
import ctypes
import sys


root=ctk.CTk()
root.title("Windows Debloat Tool")
root.geometry("800x800")
root.configure(bg='#32353b')

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# ---------------------------------------POWERSHELL FUNCTIONS---------------------------------------

def InProgress():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, "Scripts\\TBA.bat")
    subprocess.run([script_path], check=True)

def Uninstall_all_built_in_apps():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, "Scripts\\Uninstall all built in apps.ps1")
    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script_path], check=True)

def WindowsUpdate():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, "Scripts\\WindowsUpdate.ps1")
    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script_path, "-Verb", "RunAs"], check=True)


# ---------------------------------------MAIN FUNCTIONS---------------------------------------
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def show_login_page():
    clear_window(root)
    titleLabel = ctk.CTkLabel(root, text="Windows Debloat Tool", font=ctk.CTkFont(size=30, weight="bold")).place(x = 220, y = 10)
    user_name = ctk.CTkLabel(root, text = "Username").place(x = 220,y = 100)  
    user_name_input_area = ctk.CTkEntry(root, textvariable=username_var, width = 200).place(x = 290, y = 100)
    user_password = ctk.CTkLabel(root, text = "Password").place(x = 220,y = 140) 
    password_input_area = ctk.CTkEntry(root, textvariable=password_var, show="*", width = 200).place(x = 290, y = 140)
    submit_button = ctk.CTkButton(root, text="Submit", command=save_credentials).place(x = 290, y = 200)

def show_main_page():
    clear_window(root)
    titleLabel = ctk.CTkLabel(root, text="Windows Debloat Tool", font=ctk.CTkFont(size=30, weight="bold")).place(x = 220, y = 10)
    close_button = ctk.CTkButton(root, text="Close", command=root.destroy).place(relx=0.4, rely=1.0, y=-20, anchor='sw')

    """ success_label = ctk.CTkLabel(root, text="Login successful!")
    success_label.pack()
    root.after(2500, success_label.destroy) """

    RunButton1 = ctk.CTkButton(root, text="Run", font=ctk.CTkFont(size=15), command=InProgress).place(x = 50, y = 70)
    RunLabel1 = ctk.CTkLabel(root, text="Uninstall all built-in apps", font=ctk.CTkFont(size=15)).place(x = 200, y = 70)

    RunButton2 = ctk.CTkButton(root, text="Run", font=ctk.CTkFont(size=15), command=WindowsUpdate).place(x = 50, y = 105)
    RunLabel2 = ctk.CTkLabel(root, text="Run all updates", font=ctk.CTkFont(size=15)).place(x = 200, y = 105)

    RunButton3 = ctk.CTkButton(root, text="Run", font=ctk.CTkFont(size=15), command=InProgress).place(x = 50, y = 140)
    RunLabel3 = ctk.CTkLabel(root, text="Setup Autologon", font=ctk.CTkFont(size=15)).place(x = 200, y = 140)

    RunButton4 = ctk.CTkButton(root, text="Run", font=ctk.CTkFont(size=15), command=InProgress).place(x = 50, y = 175)
    RunLabel4 = ctk.CTkLabel(root, text="XD", font=ctk.CTkFont(size=15)).place(x = 200, y = 175)


def save_credentials():
    username = username_var.get().lower()
    password = password_var.get()
    if username == admin_username and password == admin_password:
                    show_main_page()
    else:
        messagebox.showerror("Error", "Invalid username or password")


# ---------------------------------------MAIN---------------------------------------



admin_username = "admin"
admin_password = "qazwsx"

username_var = StringVar()
password_var = StringVar()

#show_login_page()
show_main_page()
root.mainloop()









""" def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if __name__ == "__main__":
    if is_admin():
        # Kod twojej aplikacji tutaj
        pass
    else:
        # Uruchom ponownie z uprawnieniami administratora
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) """