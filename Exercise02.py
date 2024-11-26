def validar_nome(nome_completo):
    """
    Valida se a entrada de nome e sobrenome é válida.
    Uma entrada válida tem pelo menos dois caracteres no nome e no sobrenome.

    Args:
        nome_completo (str): A entrada de nome e sobrenome.

    Returns:
        bool: True se a entrada for válida, False caso contrário.
    """
    partes = nome_completo.split()
    if len(partes) == 2 and all(len(parte) >= 2 for parte in partes):
        return True
    return False


def main():
    """
    Lê uma entrada de nome e sobrenome na mesma linha, valida, 
    e exibe o nome se a entrada for válida. Caso contrário, pede uma nova entrada.
    """
    while True:    
        nome_completo = input("Digite o nome completo: ").strip()
        if validar_nome(nome_completo):
            print("Nome válido!: ", nome_completo)
        else:
            print("Nome inválido! O nome deve conter pelo menos dois caracteres em cada parte.")

main()