def extrair_caracteres(frase):
    """
    Retorna os cinco primeiros e os cinco últimos caracteres da frase.
    """
    primeiros = frase[:6]  
    ultimos = frase[-6:]   
    return primeiros, ultimos

def main():
    """
    Lê uma frase do usuário e exibe os cinco primeiros e os cinco últimos caracteres.
    """
    frase = input("Entre com uma frase: ")
    primeiros, ultimos = extrair_caracteres(frase)
    print(f"Cinco primeiros: {primeiros}")
    print(f"Cinco últimos: {ultimos}")

main()
