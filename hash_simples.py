"""Hash simples: soma dos valores da tabela ASCII (didático, NÃO use em sistemas reais)."""
import hashlib


def calcula_hash(senha):
    valor = 0
    for letra in senha:
        valor += ord(letra)
    return valor


def hash_real(senha):
    """Comparação: SHA-256, usado de verdade (em sistemas reais ainda se usa 'salt')."""
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    print("olecram    ->", calcula_hash("olecram"))      # 739
    print("marcelo123 ->", calcula_hash("marcelo123"))
    print("marcelo    ->", calcula_hash("marcelo"))      # também 739: colisão!
    print("SHA-256 de olecram:", hash_real("olecram"))
    print("SHA-256 de marcelo:", hash_real("marcelo"))
