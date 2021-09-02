premio = float(input("Qual o valor total do prêmio recebido?"))
imposto = (7*premio)/100
novo = premio - imposto
ganhador1 = (46*novo)/100
ganhador2 = (32*novo)/100
ganhador3 = (22*novo)/100
print("Você recebeu R${} de premiação, pagará R${} de impostos e restará R${}. \nNa qual o primeiro ganhador receberá R${}, o segundo R${} e o terceiro R${}.".format(premio, imposto, novo, ganhador1, ganhador2, ganhador3))