# batalha_naval.py

import random

# Criar o tabuleiro (5x5)
tabuleiro = [["~"] * 5 for _ in range(5)]

# Gerar posição aleatória para o navio
linha_navio = random.randint(0, 4)
coluna_navio = random.randint(0, 4)

def mostrar_tabuleiro():
    print("  0 1 2 3 4")
    for i, linha in enumerate(tabuleiro):
        print(i, " ".join(linha))

def jogar():
    tentativas = 5
    print("🌊 Bem-vindo ao Batalha Naval!")
    print("Você tem 5 tentativas para encontrar o navio.")
    
    while tentativas > 0:
        mostrar_tabuleiro()
        try:
            linha = int(input("Escolha a linha (0-4): "))
            coluna = int(input("Escolha a coluna (0-4): "))
        except ValueError:
            print("Entrada inválida! Use números de 0 a 4.")
            continue

        if linha == linha_navio and coluna == coluna_navio:
            print("💥 BOOM! Você acertou o navio!")
            tabuleiro[linha][coluna] = "X"
            break
        elif tabuleiro[linha][coluna] == "O":
            print("Você já tentou essa posição.")
        else:
            print("🌊 Água!")
            tabuleiro[linha][coluna] = "O"
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")
    
    if tentativas == 0:
        print("😢 Fim de jogo! O navio estava em:", linha_navio, coluna_navio)

    mostrar_tabuleiro()

if __name__ == "__main__":
    jogar()
