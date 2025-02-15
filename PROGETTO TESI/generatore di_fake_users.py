from faker import Faker
import pandas as pd
import sqlite3

# Inizializza Faker per generare dati casuali
fake = Faker()

# Imposta il seed per garantire che i dati generati siano sempre uguali
Faker.seed(12345)

# Genera dati casuali per 10 utenti (nome, cognome, email, telefono) 
users = [
    {
        "Nome": fake.first_name(),
        "Cognome": fake.last_name(),
        "Email": fake.email(),
        "Telefono": fake.phone_number()
    }
    for _ in range(10)
]

# Crea un DataFrame e salva i dati in un file Excel
df = pd.DataFrame(users)
df.to_excel("utenti.xlsx", index=False)
print("File Excel 'utenti.xlsx' generato con successo!")
