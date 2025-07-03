import tkinter as tk
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservations import EditReservationPage
import database

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.shared_data = {"edit_id": None}
        self.frames = {}
        self.title("Booking App")
        self.geometry("1024x600")
        self.minsize(800, 200)
        self.resizable(False, False)
        database.create_table()
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        

        self.show_frame("HomePage")

    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.grid(row=0, column=0, sticky="nsew")
        frame.configure(bg="#E1E9EC")
        # print("showing", page_name)
        frame.tkraise()
        
        if page_name == "EditReservationPage":
            frame.load_data()
        elif page_name == "ReservationsPage":
            frame.update_table()

        if page_name == "BookingPage":
            self.geometry("300x500")
        else:
            self.geometry("1024x600")  # default size



if __name__ == "__main__":
    app = App()
    app.mainloop()
