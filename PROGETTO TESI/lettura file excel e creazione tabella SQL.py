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
