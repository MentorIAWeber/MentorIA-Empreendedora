import sqlite3
import random

def obter_dicas(maestria):
    conn = sqlite3.connect('mentoria.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM conteudos WHERE maestria = ?', (maestria,))
    dicas = cursor.fetchall()  # Pega todas as dicas
    conn.close()
    return dicas

def main():
    print("Bem-vindo à MentorIA Empreendedora!")
    while True:
        print("\nEscolha uma maestria: Emocional, Empreendedora, Empresarial")
        maestria = input("Digite sua escolha (ou 'sair' para encerrar): ").capitalize()
        
        if maestria == 'Sair':
            print("Obrigado por usar a MentorIA Empreendedora!")
            break
        
        if maestria not in ['Emocional', 'Empreendedora', 'Empresarial']:
            print("Maestria inválida! Escolha entre Emocional, Empreendedora ou Empresarial.")
            continue
        
        dicas = obter_dicas(maestria)
        if dicas:
            dica = random.choice(dicas)  # Escolhe uma dica aleatoriamente
            print(f"\nTema: {dica[2]}")
            print(f"Conhecimento: {dica[3]}")
            print(f"Habilidade: {dica[4]}")
            print(f"Atitude: {dica[5]}")
            print(f"OODA - Observar: {dica[6]}")
            print(f"OODA - Orientar: {dica[7]}")
            print(f"OODA - Decidir: {dica[8]}")
            print(f"OODA - Agir: {dica[9]}")
        else:
            print(f"Nenhuma dica encontrada para a maestria {maestria}!")

if __name__ == "__main__":
    main()