import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

#Const
bg_color = "#262626"
bg_alternative = "#333430"
main_color = "#DCE38D"
main_variant = "#F6F2CD"

def clear_window(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def create_button(frame, text:str, color:str):
    button = tk.Button(
        frame,
        text=text,
        width=15,
        bg=color,
        fg="white",
        cursor="hand2",
        padx=5
    )
    return button

def load_main():

    logo_img = Image.open(r"C:\Users\User\Desktop\BurgerShop\assets\logo.png")
    logo_img = logo_img.resize((200,200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(logo_img)
    label_img = tk.Label(login_frame, image= img, bg=bg_color).pack()

    user = ttk.Entry(login_frame, width= 25).pack()
    password =ttk.Entry(login_frame, show="*", width= 25).pack()
    login_button = create_button(login_frame, "Login", main_color).pack()

    login_frame.pack()

def load_vendorsUI():
    vendors_frame.grid(row= 3, column= 2, sticky="nesw")
    vendors_frame.tkraise()
    for column in [0,1,2]:
        vendors_frame.columnconfigure(column, weight=1)

    logo_img = ImageTk.PhotoImage(file=r"C:\Users\User\Desktop\BurgerShop\assets\logo.png")
    logo_widget = tk.Label(vendors_frame, image= logo_img, bg= bg_color)
    logo_widget.image = logo_img
    logo_widget.grid(row=0, column=0)
    
    logout_button = create_button(vendors_frame, "Logout", "red")
    logout_button.grid(row=0, column=2)
    

    
    cancel_button = create_button(vendors_frame, "Cancel", "red")
    cancel_button.grid(column=0, row=3)

    submit_button = create_button(vendors_frame, "Submit", "green")
    submit_button.grid(row=3, column=2)

    vendors_frame.pack()

def load_adminUI():
    pass


root = tk.Tk()
root.title("Pabletoo's Burger")
root.geometry("800x600")
root.resizable(width=0, height=0)
login_frame = tk.Frame(root, bg= bg_color)
vendors_frame = tk.Frame(root, bg=bg_color)
admin_frame = tk.Frame(root, bg= bg_color)

load_main()

root.mainloop()