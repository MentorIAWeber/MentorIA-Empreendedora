import sqlite3
import json

def inserir_conteudos():
    # Ler o conteudos.json
    with open('conteudos/conteudos.json', 'r', encoding='utf-8') as file:
        conteudos = json.load(file)

    # Conectar ao banco
    conn = sqlite3.connect('mentoria.db')
    cursor = conn.cursor()

    # Inserir cada conteúdo
    for conteudo in conteudos:
        cursor.execute('''
            INSERT INTO conteudos (
                maestria, tema, conhecimento, habilidade, atitude,
                ooda_observar, ooda_orientar, ooda_decidir, ooda_agir
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            conteudo['maestria'],
            conteudo['tema'],
            conteudo['conhecimento'],
            conteudo['habilidade'],
            conteudo['atitude'],
            conteudo['ooda_observar'],
            conteudo['ooda_orientar'],
            conteudo['ooda_decidir'],
            conteudo['ooda_agir']
        ))

    conn.commit()
    conn.close()
    print("Conteúdos inseridos com sucesso!")

if __name__ == "__main__":
    inserir_conteudos()