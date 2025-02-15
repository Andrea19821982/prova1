from faker import Faker
import pandas as pd
import sqlite3

# Inizializza Faker per generare dati casuali
fake = Faker()

# Imposta il seed per garantire che i dati generati siano sempre uguali
Faker.seed(12345)

# Genera dati casuali per 10 utenti (nome, cognome, email, telefono) 
users = [{"Nome": fake.first_name(),
          "Cognome": fake.last_name(),
          "Email": fake.email(),
          "Telefono": fake.phone_number()} for _ in range(10)]

# Crea un DataFrame e salva i dati in un file Excel
df = pd.DataFrame(users)
df.to_excel("utenti.xlsx", index=False)
print("File Excel 'utenti.xlsx' generato con successo!")

# Leggi i dati dal file Excel generato
df_excel = pd.read_excel("utenti.xlsx")

# Connessione al database SQLite
conn = sqlite3.connect("database_utenti.db")
cursor = conn.cursor()

# Creazione della tabella SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS utenti (
    Nome TEXT,
    Cognome TEXT,
    Email TEXT,
    Telefono TEXT
)
""")

# Inserisci i dati dal DataFrame nella tabella SQL
df_excel.to_sql("utenti", conn, if_exists="replace", index=False)
print("Tabella SQL creata con successo nel database 'database_utenti.db'!")

# Visualizza i dati della tabella SQL
query = "SELECT * FROM utenti"
df_sql = pd.read_sql_query(query, conn)
print("\nDati nella tabella SQL:")
print(df_sql)

# Chiudi la connessione al database
conn.close()
