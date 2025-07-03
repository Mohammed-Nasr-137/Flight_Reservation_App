import tkinter as tk
from tkinter import PhotoImage
import os

BASE_DIR = os.path.dirname(__file__)
ICON_PATH = os.path.join(BASE_DIR, "icons")

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.plane_icon = PhotoImage(file=os.path.join(ICON_PATH, "icons8-plane-50.png"))
        self.list_icon = PhotoImage(file=os.path.join(ICON_PATH, "icons8-list-50.png"))

        # Top nav bar
        nav_bar = tk.Frame(self, bg="#3c7da8", height=50)
        nav_bar.pack(fill="x")
        title = tk.Label(nav_bar, text="✈ FlySky Reservations", bg="#3c7da8", fg="white", font=("Arial", 14, "bold"))
        title.pack(expand=True, fill="both", side="left", padx=10)

        # Welcome text
        tk.Label(self, text="Welcome to FlySky Reservations", font=("Arial", 28, "bold"), pady=20, bg="#E1E9EC").pack()
        tk.Label(self, text="Book your flights and manage your reservations in the click of a button.", font=("Arial", 22), bg="#E1E9EC").pack()

        # Button selection

        def on_enter(e):
            e.widget.configure(bg="#00436c", cursor="hand2")
            e.widget.configure(bd=1, relief="raised", highlightbackground="#aaa")

        def on_leave(e):
            e.widget.configure(bg="#006BB3")
            e.widget.configure(bd=0, relief="groove", highlightbackground="#CACBD3")

        book_button_frame = tk.Frame(self, bg="#E1E9EC", highlightbackground="#CACBD3", highlightthickness=2, bd=0, padx=20, pady=20)
        book_button_frame.pack(side="left", pady=40)
        tk.Label(book_button_frame, image=self.plane_icon, compound="top", text="Book a Flight", font=("Arial", 14, "bold"), pady=20, bg="#E1E9EC").pack()
        tk.Label(book_button_frame, text="Reserve your next flight by providing your details and flight information.", font=("Arial", 10, "bold"), pady=20, bg="#E1E9EC", fg="#4C4F50").pack()
        
        book_btn = tk.Button(book_button_frame, text="Book", width=20, height=2,
                             bg="#006BB3", fg="white", font=("Arial", 10, "bold"),
                             bd=0, relief="groove", highlightbackground="#CACBD3",
                             command=lambda: controller.show_frame("BookingPage"))
        book_btn.pack(pady=10)
        book_btn.bind("<Enter>", on_enter)
        book_btn.bind("<Leave>", on_leave)

        view_button_frame = tk.Frame(self, bg="#E1E9EC", highlightbackground="#CACBD3", highlightthickness=2, bd=0, padx=20, pady=20)
        view_button_frame.pack(side="left", pady=40)
        tk.Label(view_button_frame, image=self.list_icon, compound="top", text="View Reservations", font=("Arial", 14, "bold"), pady=20, bg="#E1E9EC").pack()
        tk.Label(view_button_frame, text="Manage your existing reservations, view details, edit or cancel if needed.", font=("Arial", 10, "bold"), pady=20, bg="#E1E9EC", fg="#4C4F50").pack()
        
        view_btn = tk.Button(view_button_frame, text="View", width=20, height=2,
                             bg="#006BB3", fg="white", font=("Arial", 10, "bold"),
                             bd=0, relief="groove", highlightbackground="#CACBD3",
                             command=lambda: controller.show_frame("ReservationsPage"))
        view_btn.pack(pady=10)
        view_btn.bind("<Enter>", on_enter)
        view_btn.bind("<Leave>", on_leave)


