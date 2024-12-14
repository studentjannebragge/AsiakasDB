import sqlite3
import random
import string
from datetime import datetime, timedelta

# Funktio satunnaisen nimen luomiseen
def generate_random_name():
    first_names = ['Matti', 'Liisa', 'Pekka', 'Kaisa', 'Jari', 'Anna', 'Heikki', 'Laura', 'Timo', 'Marja']
    last_names = ['Virtanen', 'Korhonen', 'Nieminen', 'Mäkinen', 'Hämäläinen', 'Laine', 'Heikkinen', 'Koskinen']
    return random.choice(first_names), random.choice(last_names)

# Funktio satunnaisen sähköpostin luomiseen
def generate_random_email(first_name, last_name):
    domains = ['example.com', 'test.com', 'mail.com', 'demo.com']
    return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

# Funktio satunnaisen osoitteen luomiseen
def generate_random_address():
    streets = ['Esimerkkikatu', 'Mallitie', 'Kivitie', 'Puistokatu', 'Harjutie']
    cities = ['Helsinki', 'Tampere', 'Turku', 'Oulu', 'Jyväskylä']
    return f"{random.randint(1, 100)} {random.choice(streets)}", random.choice(cities), f"{random.randint(10000, 99999)}"

# Funktio satunnaisen päivämäärän luomiseen
def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Pseudodatan lisääminen tietokantaan
def generate_pseudodata():
    try:
        # Yhdistä SQLite-tietokantaan
        connection = sqlite3.connect("AsiakasTietokanta.db")
        cursor = connection.cursor()

        # Lisää satunnaisia asiakkaita
        for _ in range(100):  # 100 asiakasta
            first_name, last_name = generate_random_name()
            email = generate_random_email(first_name, last_name)
            phone_number = f"0{random.randint(400, 500)}-{random.randint(100000, 999999)}"
            address, city, postal_code = generate_random_address()
            registration_date = generate_random_date(
                datetime(2022, 1, 1), datetime(2024, 12, 14)).strftime('%Y-%m-%d')

            cursor.execute("""
                INSERT INTO Asiakkaat (Etunimi, Sukunimi, Sahkoposti, Puhelinnumero, Osoite, Kaupunki, Postinumero, RekisterointiPvm)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, (first_name, last_name, email, phone_number, address, city, postal_code, registration_date))

        # Hae kaikkien asiakkaiden ID:t, jotta niitä voidaan käyttää tilauksissa
        cursor.execute("SELECT AsiakasID FROM Asiakkaat;")
        asiakas_idt = [row[0] for row in cursor.fetchall()]

        # Lisää satunnaisia tilauksia
        for _ in range(200):  # 200 tilausta
            asiakas_id = random.choice(asiakas_idt)
            order_date = generate_random_date(
                datetime(2023, 1, 1), datetime(2024, 12, 14)).strftime('%Y-%m-%d')
            order_amount = round(random.uniform(20.0, 500.0), 2)

            cursor.execute("""
                INSERT INTO Tilaukset (AsiakasID, TilausPvm, TilausSumma)
                VALUES (?, ?, ?);
            """, (asiakas_id, order_date, order_amount))

        # Tallenna muutokset
        connection.commit()
        print("Pseudodata lisätty tietokantaan.")

    except sqlite3.Error as e:
        print(f"Virhe: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Yhteys SQLite-tietokantaan suljettu.")

if __name__ == "__main__":
    generate_pseudodata()
