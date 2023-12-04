from datetime import date
import time
escolha=True
while escolha:
    print("\n")
    print("\033[1;36m=\033[m"*60)
    print("\t\t\t\t\tEstação do Ano")
    print("\033[1;36m=\033[m" * 60)
    print("""
    1.\tEstações do Ano \n
    2.\tActual Estação do Ano \n
    3.\tEstação do Ano de uma data qualquer\n
    4.\tExit/Quit/Saída
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        time.sleep(2)
        print("\n")
        print("\033[1;34mPrimavera:\033[m \033[1;93m20 de março a 21 de junho\033[m")
        print("\033[1;94mVerão:\033[m \033[1;92m21 de junho a 23 de setembro\033[m")
        print("\033[1;91mOutono:\033[m \033[1;33m23 de setembro a 21 de dezembro\033[m")
        print("\033[1;96mInverno:\033[m \033[1;34m21 de dezembro a 20 de março\033[m")
        time.sleep(2)
    elif escolha == "2":
        today = date.today()
        mes = today.month
        dia = today.day
        if mes in (1,2,3):
            estacao = 'no Inverno'
        elif mes in (4,5,6):
            estacao = 'na Primavera'
        elif mes in (7, 8, 9):
            estacao = 'no Verão'
        else:
            estacao = 'no Outono'
        if (mes ==4) and (dia > 19):
            estacao = 'na Primavera'
        elif (mes == 6) and (dia > 20):
            estacao = 'no Verão'
        elif (mes == 9) and (dia > 21):
            estacao = 'no Outono'
        elif (mes == 12) and (dia > 20):
            estacao = 'no Inverno'
        time.sleep(3)
        print(f"\n\033[1;93mEstamos {estacao}.\033[m")
        time.sleep(2)
    elif escolha == "3":

        dia1 = int(input("Digite o dia do mês: "))
        mes1 = int(input("Digite o número do mês: "))
        if mes1 in (1,2,3):
            estacao1 = 'o Inverno'
        elif mes1 in (4,5,6):
            estacao1 = 'a Primavera'
        elif mes1 in (7, 8, 9):
            estacao1 = 'o Verão'
        else:
            estacao1 = 'o Outono'
        if (mes1 ==4) and (dia1 > 19):
            estacao1 = 'a Primavera'
        elif (mes1 == 6) and (dia1 > 20):
            estacao1 = 'o Verão'
        elif (mes1 == 9) and (dia1 > 21):
            estacao1 = 'o Outono'
        elif (mes1 == 12) and (dia1 > 20):
            estacao1 = 'o Inverno'
        if  mes1==1:
            nome_mês = "Janeiro"
        elif mes1==2:
            nome_mês = "Fevereiro"
        elif mes1 == 3:
            nome_mês = "Março"
        elif mes1 == 4:
            nome_mês = "Abril"
        elif mes1 == 5:
            nome_mês = "Maio"
        elif mes1 == 6:
            nome_mês = "Junho"
        elif mes1 == 7:
            nome_mês = "Julho"
        elif mes1 == 8:
            nome_mês = "Agosto"
        elif mes1 == 9:
            nome_mês = "Setembro"
        elif mes1 == 10:
            nome_mês = "Outubro"
        elif mes1 == 11:
            nome_mês = "Novembro"
        else:
            nome_mês = "Dezembro"


        print(f"\n\033[1;34mNo dia {dia1} do mês {nome_mês} a estação do ano é {estacao1}.\033[m")
    elif escolha=="4":
      print("\n Fim do Programa")
      escolha = None
    else:
       print("\n Escolha não válida.\n Tente outra vez.")