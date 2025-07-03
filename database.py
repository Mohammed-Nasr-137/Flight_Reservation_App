import sqlite3

def connect():
    db = sqlite3.connect("flights.db")
    cursor = db.cursor()
    return db, cursor

def create_table():
    db, cursor = connect()
    table = """ CREATE TABLE IF NOT EXISTS Reservations(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                flight_number TEXT NOT NULL,
                departure TEXT NOT NULL,
                destination TEXT NOT NULL,
                date TEXT NOT NULL,
                seat_number TEXT NOT NULL
            );"""
    cursor.execute(table)
    db.close()


def read():
    db, cursor = connect()
    cursor.execute("SELECT * FROM reservations")
    results = cursor.fetchall()
    # print(results, type(results))
    db.close()
    return results


def insert(data):
    db, cursor = connect()
    cursor.execute("""
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["flight_number"],
        data["departure"],
        data["destination"],
        data["date"],
        data["seat_number"]
    ))
    db.commit()
    db.close()


def update(res_id, data):
    db, cursor = connect()
    cursor.execute("""
        UPDATE reservations
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    """, (
        data["name"],
        data["flight_number"],
        data["departure"],
        data["destination"],
        data["date"],
        data["seat_number"],
        res_id
    ))
    db.commit()
    db.close()


def delete(res_id):
    db, cursor = connect()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (res_id,))
    db.commit()
    db.close()
