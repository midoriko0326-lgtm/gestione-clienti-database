import sqlite3

conn = sqlite3.connect("azienda.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clienti (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT
)
""")

conn.commit()

print("Database creato con successo")
