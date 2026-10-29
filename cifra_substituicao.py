"""Criptografia por substituição (dicionário) - o modelo INSEGURO da aula anterior."""
import random
import string

ALFABETO = string.ascii_uppercase + string.ascii_lowercase + string.digits


def criar_dicionario(semente=42):
    """Embaralha o alfabeto com uma semente fixa, para o resultado ser sempre o mesmo."""
    embaralhado = list(ALFABETO)
    random.Random(semente).shuffle(embaralhado)
    return dict(zip(ALFABETO, embaralhado))


def criptografar(texto, dicionario):
    # Caracteres que não estão no dicionário (espaço, símbolos) ficam como estão
    return "".join(dicionario.get(letra, letra) for letra in texto)


def descriptografar(texto, dicionario):
    inverso = {v: k for k, v in dicionario.items()}
    return "".join(inverso.get(letra, letra) for letra in texto)


def quebra_parcial(original, cifrado):
    """Mostra a fraqueza: com um par texto/cifra, o atacante já descobre parte do dicionário."""
    return {o: c for o, c in zip(original, cifrado) if o in ALFABETO}


if __name__ == "__main__":
    dic = criar_dicionario()
    cifrado = criptografar("Marcelo123", dic)
    print("Cifrado:", cifrado)
    print("Original:", descriptografar(cifrado, dic))
    print("Atacante descobre:", quebra_parcial("Marcelo123", cifrado))
