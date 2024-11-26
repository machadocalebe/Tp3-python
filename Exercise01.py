def concatNomes():
    """
    Função principal que lê um nome e um sobrenome, e exibe ambos na mesma linha.
    """
    nome = input("Entre com um nome: ")
    sobrenome = input("Entre com um sobrenome: ")
    nome_completo = nome + " " + sobrenome
    print("Nome completo: ", nome_completo)

concatNomes()    