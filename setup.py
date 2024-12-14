import sqlite3
from sqlite3 import Error

def create_database_and_tables():
    try:
        # Yhdistä SQLite-tietokantaan (tiedosto luodaan automaattisesti, jos sitä ei ole)
        connection = sqlite3.connect("AsiakasTietokanta.db")
        print("Yhdistetty SQLite-tietokantaan!")

        # Luo kursori SQL-komentojen suorittamista varten
        cursor = connection.cursor()

        # Luo Asiakkaat-taulu
        asiakkaat_table = """
        CREATE TABLE IF NOT EXISTS Asiakkaat (
            AsiakasID INTEGER PRIMARY KEY AUTOINCREMENT,
            Etunimi TEXT,
            Sukunimi TEXT,
            Sahkoposti TEXT,
            Puhelinnumero TEXT,
            Osoite TEXT,
            Kaupunki TEXT,
            Postinumero TEXT,
            RekisterointiPvm TEXT
        );
        """
        cursor.execute(asiakkaat_table)
        print("Taulu 'Asiakkaat' luotu tai se on jo olemassa.")

        # Luo Tilaukset-taulu
        tilaukset_table = """
        CREATE TABLE IF NOT EXISTS Tilaukset (
            TilausID INTEGER PRIMARY KEY AUTOINCREMENT,
            AsiakasID INTEGER,
            TilausPvm TEXT,
            TilausSumma REAL,
            FOREIGN KEY (AsiakasID) REFERENCES Asiakkaat(AsiakasID)
        );
        """
        cursor.execute(tilaukset_table)
        print("Taulu 'Tilaukset' luotu tai se on jo olemassa.")

        # Lisää esimerkkidata Asiakkaat-tauluun
        asiakkaat_data = """
        INSERT INTO Asiakkaat (Etunimi, Sukunimi, Sahkoposti, Puhelinnumero, Osoite, Kaupunki, Postinumero, RekisterointiPvm)
        VALUES
        ('Matti', 'Virtanen', 'matti.virtanen@example.com', '0401234567', 'Esimerkkikatu 5', 'Helsinki', '00100', '2024-12-14'),
        ('Liisa', 'Korhonen', 'liisa.korhonen@example.com', '0507654321', 'Mallitie 10', 'Tampere', '33100', '2024-12-13');
        """
        cursor.execute(asiakkaat_data)

        # Lisää esimerkkidata Tilaukset-tauluun
        tilaukset_data = """
        INSERT INTO Tilaukset (AsiakasID, TilausPvm, TilausSumma)
        VALUES
        (1, '2024-12-14', 250.50),
        (2, '2024-12-13', 125.00);
        """
        cursor.execute(tilaukset_data)

        # Tallenna muutokset
        connection.commit()
        print("Esimerkkidata lisätty tauluihin.")

    except Error as e:
        print(f"Virhe: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Yhteys SQLite-tietokantaan suljettu.")

if __name__ == "__main__":
    create_database_and_tables()

