import sqlite3

def criar_banco():
    conn = sqlite3.connect('mentoria.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conteudos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            maestria TEXT,
            tema TEXT,
            conhecimento TEXT,
            habilidade TEXT,
            atitude TEXT,
            ooda_observar TEXT,
            ooda_orientar TEXT,
            ooda_decidir TEXT,
            ooda_agir TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco()