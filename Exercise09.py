def validar_telefone(numero):
    """
    Verifica se o número de telefone tem exatamente 11 dígitos.
    """
    return numero.isdigit() and len(numero) == 11

def formatar_telefone(numero):
    """
    Formata o número de telefone no formato (99) 99999-9999.
    """
    ddd = numero[:2]
    parte1 = numero[2:7]
    parte2 = numero[7:]
    return f"({ddd}) {parte1}-{parte2}"

def main():
    """
    Solicita um número de telefone ao usuário, valida a entrada e exibe o número formatado.
    """
    while True:
        numero = input("Digite o número de telefone com 11 dígitos (apenas números): ").strip()
        if validar_telefone(numero):
            telefone_formatado = formatar_telefone(numero)
            print(f"Número formatado: {telefone_formatado}")
            break
        else:
            print("Entrada inválida. Certifique-se de digitar exatamente 11 dígitos.")

main()
