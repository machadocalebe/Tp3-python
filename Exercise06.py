def obter_nome_mes(mes):
    """
    Retorna o nome do mês correspondente ao número.
    """
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    return meses[mes - 1]

def exibir_data_formatada(data):
    """
    Converte uma data no formato 'dd/mm/aaaa' para o formato 'dia de nome_do_mês de ano'.
    """
    partes = data.split("/")
    if len(partes) == 3 and all(parte.isdigit() for parte in partes):
        dia, mes, ano = map(int, partes)
        if 1 <= mes <= 12:
            nome_mes = obter_nome_mes(mes)
            print(f"{dia:02d} de {nome_mes} de {ano}")
        else:
            print("Erro: Mês inválido.")
    else:
        print("Erro: Formato de data inválido. Use 'dd/mm/aaaa'.")

def main():
    """
    Solicita a data do usuário e exibe no formato solicitado.
    """
    data = input("Digite uma data no formato 'dd/mm/aaaa': ").strip()
    exibir_data_formatada(data)

main()
