def formatar_nome(nome_completo):
    """
    Formata o nome completo no formato "SOBRENOME, Nome".

    Args:
        nome_completo (str): A entrada de nome e sobrenome.

    Returns:
        str: O nome formatado no formato solicitado.
    """
    partes = nome_completo.split()
    sobrenome = partes[-1].upper()  
    nome = " ".join(partes[:-1])   
    return f"{sobrenome}, {nome}"


def main():
    """
    Lê uma entrada de nome e sobrenome na mesma linha e exibe no formato "SOBRENOME, Nome".
    """
    nome_completo = input("Digite o nome e sobrenome: ").strip()
    if len(nome_completo.split()) >= 2:
        nome_formatado = formatar_nome(nome_completo)
        print(f"Nome formatado: {nome_formatado}")
    else:
        print("Erro: Digite pelo menos um nome e um sobrenome.")

main()
