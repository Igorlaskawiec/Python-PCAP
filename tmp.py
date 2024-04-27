from tkinter import *
from tkinter import messagebox

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def show_login_page():
    clear_window(root)
    user_name = Label(root, text = "Username").place(x = 40,y = 60)  
    user_name_input_area = Entry(root, textvariable=username_var, width = 30).place(x = 110, y = 60)
    user_password = Label(root, text = "Password").place(x = 40,y = 100) 
    password_input_area = Entry(root, textvariable=password_var, show="*", width = 30).place(x = 110, y = 100)
    save_button = Button(root, text="Submit", command=save_credentials).place(x = 110, y = 140)

def show_success_page():
    clear_window(root)
    success_label = Label(root, text="Login successful!").pack()
    back_button = Button(root, text="Back", command=show_login_page).pack()

def save_credentials():
    username = username_var.get().lower()
    password = password_var.get()
    if username == admin_username and password == admin_password:
        show_success_page()
    else:
        messagebox.showerror("Error", "Invalid username or password")

root=Tk()
root.title("testowa aplikacja")
root.geometry("800x800")
root.configure(bg='#32353b')

admin_username = "admin"
admin_password = "qazwsx"

username_var = StringVar()
password_var = StringVar()

show_login_page()

root.mainloop()