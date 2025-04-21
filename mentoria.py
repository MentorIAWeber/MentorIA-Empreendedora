import sqlite3

def obter_dica(maestria):
    conn = sqlite3.connect('mentoria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM conteudos WHERE maestria = ?', (maestria,))
    dica = cursor.fetchone()
    conn.close()
    return dica

def main():
    print("Bem-vindo à MentorIA Empreendedora!")
    print("Escolha uma maestria: Emocional, Empreendedora, Empresarial")
    maestria = input("Digite sua escolha: ").capitalize()
    
    if maestria not in ['Emocional', 'Empreendedora', 'Empresarial']:
        print("Maestria inválida! Escolha entre Emocional, Empreendedora ou Empresarial.")
        return
    
    dica = obter_dica(maestria)
    if dica:
        print(f"\nTema: {dica[2]}")
        print(f"Conhecimento: {dica[3]}")
        print(f"Habilidade: {dica[4]}")
        print(f"Atitude: {dica[5]}")
    else:
        print(f"Nenhuma dica encontrada para a maestria {maestria}!")

if __name__ == "__main__":
    main()