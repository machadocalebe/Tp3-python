def is_leap_year(year):
    """
    Verifica se um ano é bissexto.
    Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_valid_date(day, month, year):
    """
    Verifica se uma data é válida considerando o número de dias em cada mês.
    """
    if month < 1 or month > 12:
        return False

    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return 1 <= day <= days_in_month[month - 1]

def main():
    """
    Lê uma data no formato "dd/mm/aaaa" e valida-a.
    """
    while True:
        data = input("Digite uma data no formato 'dd/mm/aaaa': ").strip()
        partes = data.split("/")
        
        if len(partes) == 3 and all(parte.isdigit() for parte in partes):
            dia, mes, ano = map(int, partes)
            if is_valid_date(dia, mes, ano):
                print("Data válida.")
                break
            else:
                print("Data inválida. Certifique-se de que o dia, mês e ano são consistentes.")
        else:
            print("Erro: Formato inválido. Digite no formato 'dd/mm/aaaa'.")

main()
