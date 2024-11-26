def dia_da_semana(numero):
    """
    Retorna o dia da semana correspondente ao número.
    """
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    return dias.get(numero, None)

def main():
    """
    Lê um número do usuário, valida a entrada e exibe o dia da semana correspondente.
    """
    while True:
        try:
            numero = int(input("Entre com um número entre 1 e 7: "))
            if 1 <= numero <= 7:
                dia = dia_da_semana(numero)
                print(f"O dia correspondente é: {dia}")
                break
            else:
                print("Erro: número inválido. Por favor, entre com um número entre 1 e 7.")
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número inteiro.")

main()
