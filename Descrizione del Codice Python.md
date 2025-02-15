# TESI INFORMATICA
## Introduzione
Il codice presentato ha l'obiettivo di generare dati utente casuali, salvarli in un file Excel e successivamente importarli in un database SQL.
Questo processo è utile per simulare l'inserimento e la gestione di dati utente in un contesto di sviluppo e testare applicazioni.
Il codice utilizza le librerie `Faker` per la generazione di dati casuali, `pandas` per la manipolazione dei dati e `sqlite3` per la gestione del database.
Per rendere il programma funzionante bisogna prima installare le librerie faker, pandas e openpyxl se non presenti in Python(es. pip install faker pandas openpyxl).

### Descrizione del Codice

### Importazione delle Librerie
Il codice inizia importando le librerie necessarie:

python
from faker import Faker
import pandas as pd
import sqlite3

- `Faker`: utilizzata per generare dati casuali.
- `pandas`: utilizzata per creare e manipolare DataFrame.
- `sqlite3`: utilizzata per interagire con un database SQL.


### Inizializzazione di Faker
python
fake = Faker()
Faker.seed(12345)


- crea un'istanza di `Faker` per generare dati casuali.
- Il seed viene impostato a `12345` per garantire la riproducibilità dei dati generati.


### Generazione dei Dati Utente
python
users = [{"Nome": fake.first_name(),
          "Cognome": fake.last_name(),
          "Email": fake.email(),
          "Telefono": fake.phone_number()} for _ in range(10)]


- Viene creato un elenco di 10 dizionari, ognuno contenente un nome, cognome, email e numero di telefono generati casualmente.


### Creazione del DataFrame e Salvataggio in Excel
python
df = pd.DataFrame(users)
df.to_excel("utenti.xlsx", index=False)
print("File Excel 'utenti.xlsx' generato con successo!")


- I dati generati vengono convertiti in un DataFrame `pandas`.
- Il DataFrame viene salvato in un file Excel denominato `utenti.xlsx`.


### Lettura dei Dati dal File Excel
python
df_excel = pd.read_excel("utenti.xlsx")


- Il file Excel appena creato viene letto e caricato in un nuovo DataFrame `pandas`.


### Connessione al Database SQLite
python
conn = sqlite3.connect("database_utenti.db")
cursor = conn.cursor()


- Viene stabilita una connessione a un database SQLite denominato `database_utenti.db`.
- crea un cursore per eseguire comandi SQL.


### Creazione della Tabella SQL
python
cursor.execute("""
CREATE TABLE IF NOT EXISTS utenti (
    Nome TEXT,
    Cognome TEXT,
    Email TEXT,
    Telefono TEXT
)
""")


- creazione di una tabella denominata `utenti` con le colonne `Nome`, `Cognome`, `Email` e `Telefono`.



### Inserimento dei Dati nella Tabella SQL
python
df_excel.to_sql("utenti", conn, if_exists="replace", index=False)
print("Tabella SQL creata con successo nel database 'database_utenti.db'!")


- I dati del DataFrame vengono inseriti nella tabella `utenti` del database SQLite.
- Se la tabella esiste già, viene sostituita.

### Visualizzazione dei Dati dalla Tabella SQL
python
query = "SELECT * FROM utenti"
df_sql = pd.read_sql_query(query, conn)
print("\nDati nella tabella SQL:")
print(df_sql)


- Viene eseguita una query SQL per selezionare tutti i dati dalla tabella `utenti`.
- I dati risultanti vengono caricati in un DataFrame e stampati.



### Chiusura della Connessione al Database
python
conn.close()


- La connessione al database viene chiusa.



## Conclusioni
Il codice presentato fornisce un esempio pratico di come generare, salvare e gestire dati utente utilizzando librerie Python. Questo processo è fondamentale per testare applicazioni che richiedono l'interazione con dati utente senza dover utilizzare dati reali. Il codice è stato scritto in modo modulare e può essere facilmente adattato per generare un numero diverso di utenti o per aggiungere ulteriori campi di dati.
