def main():
    """
    Lê uma data no formato "dd/mm/aaaa" e exibe o dia, mês e ano como inteiros.
    """
    while True:
        data = input("Digite uma data no formato 'dd/mm/aaaa': ").strip()
        partes = data.split("/")
        
        if len(partes) == 3 and all(parte.isdigit() for parte in partes):
            dia, mes, ano = map(int, partes) 
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0:  
                print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
                break
            else:
                print("Erro: Data inválida. Certifique-se de usar um dia (1-31), mês (1-12) e ano válido.")
        else:
            print("Erro: Formato inválido. Digite no formato 'dd/mm/aaaa'.")

main()
