import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

def clear_window(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_main():
    login_frame.grid(row=3, column=0, sticky="nesw")
    login_frame.tkraise()

    #Logo
    logo_img = ImageTk.PhotoImage(file=r"C:\Users\User\Desktop\BurgerShop\assets\logo.png")
    logo_widget = tk.Label(login_frame, image= logo_img)
    logo_widget.image = logo_img
    logo_widget.pack()

    user = ttk.Entry(login_frame, textvariable="User", width= 40).pack(pady=10)
    password =ttk.Entry(login_frame, show="*", width= 40).pack()


    tk.Button(
        login_frame,
        text="Login",
        width=15,
        bg="red",
        fg="white",
        cursor="hand2"
    ).pack(pady=20)
    

def load_vendorsUI():
    pass

def load_adminUI():
    pass


root = tk.Tk()
root.title("Pabletoo's Burger")
login_frame = tk.Frame(root, width= 800, height=600)
vendors_frame = tk.Frame(root, width= 800, height=600)
admin_frame = tk.Frame(root, width= 800, height=600)

load_main()
root.mainloop()