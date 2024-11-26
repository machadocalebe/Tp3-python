def inverter_frase(frase):
    """
    Inverte a frase recebida utilizando um loop for.
    """
    frase_invertida = ""
    for char in frase:
        frase_invertida = char + frase_invertida
    return frase_invertida

def main():
    """
    Lê uma frase do usuário e exibe a frase invertida.
    """
    frase = input("Entre com uma frase: ")
    frase_invertida = inverter_frase(frase)
    print(f"A frase invertida é: {frase_invertida}")

main()
