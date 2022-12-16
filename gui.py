import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

def clear_window(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_main():
    login_frame.grid(row=2, column=0, sticky="nesw")
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
    vendors_frame.grid(row= 3, column= 2, sticky="nesw")
    vendors_frame.tkraise()
    for column in [0,1,2]:
        vendors_frame.columnconfigure(column, weight=1)

    logo_img = ImageTk.PhotoImage(file=r"C:\Users\User\Desktop\BurgerShop\assets\logo.png")
    logo_widget = tk.Label(vendors_frame, image= logo_img)
    logo_widget.image = logo_img
    logo_widget.grid(row=0, column=0)
    
    logout_button = tk.Button(vendors_frame, text="Logout", bg="red")
    logout_button.grid(row=0, column=1)
    
    container = tk.Frame(vendors_frame, width=500)
    for i in [0,1,2]:
        container.columnconfigure(i, weight=1)
    left_side = tk.Label(container,height=300 ,text="Hello there")
    left_side.grid(column=0, row=0)
    right_side = tk.Label(container, height=400 ,text="This is another hello there")
    right_side.grid(column=2, row=0)
    container.grid(row=2)
    
    cancel_button = tk.Button(vendors_frame, text="Cancel")
    cancel_button.grid(column=0, row=3)

    submit_button = tk.Button(vendors_frame, text="Submit")
    submit_button.grid(row=3, column=2)
    vendors_frame.pack()

    


def load_adminUI():
    pass


root = tk.Tk()
root.title("Pabletoo's Burger")
login_frame = tk.Frame(root)
vendors_frame = tk.Frame(root)
admin_frame = tk.Frame(root)

load_main()

root.mainloop()