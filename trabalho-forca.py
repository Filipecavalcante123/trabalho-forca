trabalho-forca.py

import random

def desenhar_forca(tentativas):
    forca = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
               |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        '''
    ]
    print(forca[tentativas])

def jogar_forca():
    palavras = {
        'países': ['brasil', 'canadá', 'espanha']
        'animais': ['gato', 'cachorro', 'elefante']
        'comidas': ['pizza', 'hamburguer', 'churrasco']
    }

    tema = input("Escolha o tema (países, animais, comidas): ").lower()
    while tema not in palavras.keys():
        tema = input("Tema inválido. Por favor, escolha um dos temas disponíveis: ").lower()

    palavra = random.choice(palavras[tema])
    palavra_secreta = list('_' * len(palavra))
    tentativas = 6
    letras_erradas = []

    print("\nJogo da Forca")
    print("Tema:", tema)
    print("A palavra possui", len(palavra), "letras.")

    while True:
        desenhar_forca(tentativas)
        print("Palavra:", " ".join(palavra_secreta))
        print("Letras erradas:", " ".join(letras_erradas))
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_secreta[i] = letra

            if "_" not in palavra_secreta:
                print("Parabéns! Você acertou a palavra:", palavra)
                break
        else:
            letras_erradas.append(letra)
            tentativas -= 1

            if tentativas == 0:
                desenhar_forca(tentativas)
                print("Você perdeu! A palavra era:", palavra)
                break

jogar_forca()