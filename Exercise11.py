def formatar_cpf(cpf):
    """
    Formata um número de CPF no padrão 999.999.999-99.
    """
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def validar_cpf(cpf):
    """
    Valida se o CPF contém exatamente 11 dígitos numéricos.
    """
    return len(cpf) == 11 and cpf.isdigit()

def main():
    """
    Lê um CPF do usuário, valida a entrada e exibe o CPF formatado.
    """
    while True:
        cpf = input("Digite um CPF com 11 dígitos numéricos: ")
        if validar_cpf(cpf):
            cpf_formatado = formatar_cpf(cpf)
            print(f"O CPF formatado é: {cpf_formatado}")
            break
        else:
            print("Erro: o CPF deve conter exatamente 11 dígitos numéricos. Tente novamente.")

main()
