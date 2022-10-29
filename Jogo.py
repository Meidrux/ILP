# Alunos: Júlio Alisson e Daniel Correia
# Ainda pretendo colocar uma UI
import random
vida = int(input('Insira o número de vidas: '))
palavras = []
palavraTraco = []
lugar = []
pospalavrasecreta = 0
quantidade = 0


def aleatorizar(palavras):
    palavras.remove("iniciar")  # Aleatorizar lista
    random.shuffle(palavras)


while True:
    palavras.append(
        input('Insira as palavras para o jogo: [Digite iniciar para começar o jogo] '))
    if 'iniciar' in palavras:
        aleatorizar(palavras)
        palavraSecreta = palavras[0]
        quantidade = len(palavras)
        break
for c in range(0, len(palavraSecreta)):
    palavraTraco.append('-')  # Colocar a palavra randomizada em -
traco = [str(x) for x in palavraTraco]
print(''.join(traco))


while True:
    chute = input('Insira uma letra: ')
    if chute in palavraSecreta:
        print("Você acertou uma letra.")
        for (pos, char) in enumerate(palavraSecreta):
            if(char == chute):   # Substituir a letra acertada no lugar do -

                traco[pos] = chute
        print(''.join(traco))
    else:
        print('Você perdeu uma vida.')
        vida = vida - 1
        print('Vida total: ', vida)
    if vida <= 0:
        print("Você perdeu o jogo.")
        print("A palavra era:", palavraSecreta)
        break

    if "-" not in traco:
        print("Você acertou a palavra.")
        continuar = str(input("Deseja continuar? [S/N] "))
        continuar = continuar.upper()

        if "S" in continuar:
            del palavras[0]
            if len(palavras) == 0:
                palavras.append("Você chegou ao final da lista.")
                print(
                    "Você chegou ao final da lista, obrigado por jogar, até a próxima.")
                break
            traco = traco.clear()
            palavraTraco.clear()
            palavraSecreta = palavras[0]
            for c in range(0, len(palavraSecreta)):
                palavraTraco.append('-')
            traco = [str(x) for x in palavraTraco]
            print(''.join(traco))
            continue
        else:
            print("Obrigado por jogar, até a próxima.")
            break
