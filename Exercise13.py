def inverter_frase(frase):
    """
    Inverte a frase recebida utilizando slicing.
    """
    return frase[::-1] 

def main():
    """
    Lê uma frase do usuário e exibe a frase invertida.
    """
    frase = input("Entre com uma frase: ")
    frase_invertida = inverter_frase(frase)
    print(f"A frase invertida é: {frase_invertida}")

main()
