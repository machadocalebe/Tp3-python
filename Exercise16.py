def calcular_media(numero1, numero2):
    """
    Calcula a média de dois números.
    """
    return (numero1 + numero2) / 2

def main():
    """
    Lê dois números do usuário, calcula a média e exibe o resultado formatado.
    """
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        media = calcular_media(numero1, numero2)
        print(f"A média dos números {numero1} e {numero2} é {media:.2f}.")
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")

main()
