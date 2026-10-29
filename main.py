from cifra_substituicao import criar_dicionario, criptografar, descriptografar
from hash_simples import calcula_hash, hash_real

dicionario = criar_dicionario()

MENU = """
=== Segurança Digital ===
1 - Criptografar (substituição)
2 - Descriptografar (substituição)
3 - Calcular hash simples
4 - Sair
"""

while True:
    print(MENU)
    opcao = input("Escolha: ").strip()
    if opcao == "1":
        print("Resultado:", criptografar(input("Texto: "), dicionario))
    elif opcao == "2":
        print("Resultado:", descriptografar(input("Texto cifrado: "), dicionario))
    elif opcao == "3":
        senha = input("Senha: ")
        print("Hash simples:", calcula_hash(senha))
        print("SHA-256 (real):", hash_real(senha))
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida.")
