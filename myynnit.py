import sqlite3
import random
from datetime import datetime, timedelta

def create_sales_table_and_add_data():
    try:
        # Yhdistä SQLite-tietokantaan
        connection = sqlite3.connect("AsiakasTietokanta.db")
        cursor = connection.cursor()

        # Luo Myynnit-taulu
        myynnit_table = """
        CREATE TABLE IF NOT EXISTS Myynnit (
            MyyntiID INTEGER PRIMARY KEY AUTOINCREMENT,
            AsiakasID INTEGER,
            Tuote VARCHAR(50),
            MyyntiSumma REAL,
            MyyntiPvm TEXT,
            FOREIGN KEY (AsiakasID) REFERENCES Asiakkaat(AsiakasID)
        );
        """
        cursor.execute(myynnit_table)
        print("Taulu 'Myynnit' luotu tai se on jo olemassa.")

        # Hae kaikkien asiakkaiden ID:t
        cursor.execute("SELECT AsiakasID FROM Asiakkaat;")
        asiakas_idt = [row[0] for row in cursor.fetchall()]

        # Lisää satunnaisia myyntejä asiakkaille
        tuotteet = ['Tietokone', 'Puhelin', 'Hiiri', 'Näppäimistö', 'Kuulokkeet', 'Näyttö']
        for _ in range(300):  # 300 myyntitapahtumaa
            asiakas_id = random.choice(asiakas_idt)
            tuote = random.choice(tuotteet)
            myynti_summa = round(random.uniform(10.0, 1500.0), 2)  # Myyntihinta 10–1500 €
            myynti_pvm = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')

            cursor.execute("""
                INSERT INTO Myynnit (AsiakasID, Tuote, MyyntiSumma, MyyntiPvm)
                VALUES (?, ?, ?, ?);
            """, (asiakas_id, tuote, myynti_summa, myynti_pvm))

        # Tallenna muutokset
        connection.commit()
        print("Pseudodata lisätty tauluun 'Myynnit'.")

    except sqlite3.Error as e:
        print(f"Virhe: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Yhteys SQLite-tietokantaan suljettu.")

if __name__ == "__main__":
    create_sales_table_and_add_data()
