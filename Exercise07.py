def verificar_palindromo(palavra):
    """
    Verifica se a palavra fornecida é um palíndromo.
    """
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

def main():
    """
    Solicita uma palavra ao usuário e verifica se é um palíndromo.
    """
    palavra = input("Digite uma palavra: ").strip()
    if verificar_palindromo(palavra):
        print(f"'{palavra}' é um palíndromo!")
    else:
        print(f"'{palavra}' não é um palíndromo.")

main()
