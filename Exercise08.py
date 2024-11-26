def contar_vogais(frase):
    """
    Conta o número de vogais em uma frase.
    """
    vogais = "aeiou"
    frase = frase.lower()  
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

def main():
    """
    Solicita uma frase ao usuário e exibe o número de vogais contidas nela.
    """
    frase = input("Digite uma frase: ").strip()
    total_vogais = contar_vogais(frase)
    print(f"A frase '{frase}' tem {total_vogais} vogais.")

main()
