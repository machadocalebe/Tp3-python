def substituir_ponto_e_virgula(entrada):
    """
    Substitui todos os ';' por ',' na string recebida.
    """
    return entrada.replace(";", ",")

def main():
    """
    Lê uma entrada do usuário, substitui ';' por ',' e exibe o resultado.
    """
    entrada = input("Digite a entrada com ';': ")
    resultado = substituir_ponto_e_virgula(entrada)
    print(f"Saída: {resultado}")

main()
