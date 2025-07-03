import tkinter as tk
import database
from tkinter import ttk
from tkinter import messagebox

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Top nav bar
        nav_bar = tk.Frame(self, bg="#3c7da8", height=50)
        nav_bar.pack(fill="x")
        title = tk.Label(nav_bar, text="✈ FlySky Reservations", bg="#3c7da8", fg="white", font=("Arial", 14, "bold"))
        title.pack(expand=True, fill="both", side="left", padx=10)


        def search_reservations(e):
            query = search_entry.get().strip().lower()
            rows = database.read()
            filtered = [
                row for row in rows
                if query in row[1].lower()
                or query in row[2].lower()
                or query in row[4].lower()
            ]
            self.tree.delete(*self.tree.get_children())
            for row in filtered:
                self.tree.insert("", "end", values=row)

        top_frame = tk.Frame(self, bg="#E1E9EC", height=50)
        top_frame.pack(fill="x")
        tk.Label(top_frame, text="Your Reservations", font=("Arial", 24, "bold"), pady=20, bg="#E1E9EC").pack(side="left")
        
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
        
        search_entry = tk.Entry(top_frame, width=30)
        search_entry.pack(side="right", padx=50)
        add_placeholder(search_entry, "Search by name, flight, or destination")
        search_entry.bind("<KeyRelease>", search_reservations)

        table_frame = tk.Frame(self, bg="#E1E9EC", height=50)
        table_frame.pack(fill="x")
        columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        self.tree.pack(side="left", fill="both", expand=True)

        for col in columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, anchor="center", stretch=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        # self.update_table()

        action_frame = tk.Frame(self, bg="#E1E9EC", bd=0, padx=20, pady=20)
        action_frame.pack(pady=10)

        def get_selected_id():
            selected = self.tree.selection()
            if not selected:
                messagebox.showwarning("No Selection", "Please select a reservation.")
                return None
            return self.tree.item(selected[0])["values"][0] 

        def edit():
            res_id = get_selected_id()
            if res_id is not None:
                self.controller.shared_data["edit_id"] = res_id
                self.controller.show_frame("EditReservationPage")

        def home():
            controller.show_frame("HomePage")

        def delete():
            res_id = get_selected_id()
            if res_id is not None:
                if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?"):
                    database.delete(res_id)
                    self.update_table()
        
        def on_enter(e):
            if (e.widget["text"] == "Delete Selected"):
                e.widget.configure(bg="#de1818", cursor="hand2")
            else:
                e.widget.configure(bg="#00436c", cursor="hand2")
            e.widget.configure(bd=1, relief="raised", highlightbackground="#aaa")

        def on_leave(e):
            if (e.widget["text"] == "Delete Selected"):
                e.widget.configure(bg="#D3DADE")
            else:
                e.widget.configure(bg="#006BB3")
            e.widget.configure(bd=0, relief="groove", highlightbackground="#CACBD3")

        edit_btn = tk.Button(action_frame, text="Edit Selected", width=12, height=2,
                            bg="#006BB3", fg="white", font=("Arial", 10, "bold"),
                            bd=0, relief="groove", highlightbackground="#CACBD3", command=edit)
        edit_btn.pack(side="left", padx=10)
        edit_btn.bind("<Enter>", on_enter)
        edit_btn.bind("<Leave>", on_leave)

        home_btn = tk.Button(action_frame, text="Home", width=12, height=2,
                            bg="#006BB3", fg="white", font=("Arial", 10, "bold"),
                            bd=0, relief="groove", highlightbackground="#CACBD3", command=home)
        home_btn.pack(side="left", padx=10)
        home_btn.bind("<Enter>", on_enter)
        home_btn.bind("<Leave>", on_leave)

        delete_btn = tk.Button(action_frame, text="Delete Selected", width=12, height=2,
                                bg="#D3DADE", fg="white", font=("Arial", 10, "bold"),
                                bd=0, relief="groove", highlightbackground="#CACBD3", command=delete)
        delete_btn.pack(side="left", padx=10)
        delete_btn.bind("<Enter>", on_enter)
        delete_btn.bind("<Leave>", on_leave)

    def update_table(self):
        rows = database.read()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", "end", values=row)