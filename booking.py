import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
import database

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Top nav bar
        nav_bar = tk.Frame(self, bg="#3c7da8", height=50)
        nav_bar.pack(fill="x")
        title = tk.Label(nav_bar, text="✈ FlySky Reservations", bg="#3c7da8", fg="white", font=("Arial", 14, "bold"))
        title.pack(expand=True, fill="both", side="left", padx=10)

        tk.Label(self, text="Book a Flight", font=("Arial", 24, "bold"), pady=20, bg="#E1E9EC").pack()
        form = tk.Frame(self, bg="white", highlightbackground="#CACBD3", highlightthickness=2, bd=0, padx=20, pady=20)
        form.pack(pady=40)
        form.grid_columnconfigure(0, weight=1, uniform="col")
        form.grid_columnconfigure(1, weight=1, uniform="col")

        self.fields = {}
        def add_placeholder(entry, text):
            entry.insert(0, text)
            entry.config(fg="gray")
    
            def on_focus_in(event):
                if entry.get() == text:
                    entry.delete(0, "end")
                    entry.config(fg="black")

            def on_focus_out(event):
                if entry.get() == "":
                    entry.insert(0, text)
                    entry.config(fg="gray")

            entry.bind("<FocusIn>", on_focus_in)
            entry.bind("<FocusOut>", on_focus_out)


        # Full Name
        tk.Label(form, text="Full Name", bg="white").grid(row=0, column=0, sticky="w")
        self.fields["name"] = tk.Entry(form, width=40)
        self.fields["name"].grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="ew")

        # Flight Number
        tk.Label(form, text="Flight Number", bg="white").grid(row=2, column=0, sticky="w")
        self.fields["flight_number"] = tk.Entry(form, width=40)
        self.fields["flight_number"].grid(row=3, column=0, columnspan=2, pady=(0, 10), sticky="ew")

        # Departure + Destination
        tk.Label(form, text="Departure", bg="white").grid(row=4, column=0, sticky="w")
        tk.Label(form, text="Destination", bg="white").grid(row=4, column=1, sticky="w", padx=10)
        self.fields["departure"] = tk.Entry(form)
        self.fields["destination"] = tk.Entry(form)
        self.fields["departure"].grid(row=5, column=0, sticky="ew", padx=0, pady=5)
        self.fields["destination"].grid(row=5, column=1, sticky="ew", padx=10, pady=5)

        # Date + Seat Number
        tk.Label(form, text="Date", bg="white").grid(row=6, column=0, sticky="w")
        tk.Label(form, text="Seat Number", bg="white").grid(row=6, column=1, sticky="w", padx=10)
        self.fields["date"] = DateEntry(form, width=18, background="#007ACC", foreground='white', borderwidth=2)
        self.fields["date"].grid(row=7, column=0, sticky="ew", padx=0, pady=5)
        self.fields["seat_number"] = tk.Entry(form)
        self.fields["seat_number"].grid(row=7, column=1, sticky="ew", padx=10, pady=5)

        add_placeholder(self.fields["name"], "Enter your full name")
        add_placeholder(self.fields["flight_number"], "e.g. FS123")
        add_placeholder(self.fields["departure"], "e.g. New York")
        add_placeholder(self.fields["destination"], "e.g. London")
        add_placeholder(self.fields["seat_number"], "e.g. 12A")

        def validate_fields():
            required = ["name", "flight_number", "departure", "destination", "date", "seat_number"]
            for field in required:
                value = self.fields[field].get().strip()
                if not value or "e.g." in value or "Enter your" in value:
                    return False, f"{field.replace('_', ' ').title()} is required."
            return True, ""
        
        def cancel():
            controller.show_frame("HomePage")

        def submit_booking():
            valid, msg = validate_fields()
            if not valid:
                messagebox.showerror("Invalid Input", msg)
                return
            try:
                data = {key: widget.get().strip() for key, widget in self.fields.items()}
                database.insert(data)
                messagebox.showinfo("Success", "Flight booked successfully!")
                controller.show_frame("HomePage")
            except Exception as e:
                messagebox.showerror("Database Error", str(e))


        def on_enter(e):
            if (e.widget["text"] == "Cancel"):
                e.widget.configure(bg="#de1818", cursor="hand2")
            else:
                e.widget.configure(bg="#00436c", cursor="hand2")
            e.widget.configure(bd=1, relief="raised", highlightbackground="#aaa")

        def on_leave(e):
            if (e.widget["text"] == "Cancel"):
                e.widget.configure(bg="#D3DADE")
            else:
                e.widget.configure(bg="#006BB3")
            e.widget.configure(bd=0, relief="groove", highlightbackground="#CACBD3")

        cancel_btn = tk.Button(form, text="Cancel", width=12, height=2,
                                bg="#D3DADE", fg="white", font=("Arial", 10, "bold"),
                                bd=0, relief="groove", highlightbackground="#CACBD3", command=cancel)
        cancel_btn.grid(row=8, column=0, sticky="w", padx=10, pady=20)
        cancel_btn.bind("<Enter>", on_enter)
        cancel_btn.bind("<Leave>", on_leave)

        submit_btn = tk.Button(form, text="Book Flight", width=12, height=2,
                                bg="#006BB3", fg="white", font=("Arial", 10, "bold"),
                                bd=0, relief="groove", highlightbackground="#CACBD3", command=submit_booking)
        submit_btn.grid(row=8, column=1, sticky="e", padx=10, pady=20)
        submit_btn.bind("<Enter>", on_enter)
        submit_btn.bind("<Leave>", on_leave)
