from time import sleep
print('-=-' * 10)
print('Calculadora de juros compostos mensal!')
print('-=-' * 10)
x = 1
soma = float(input('Qual o valor do depósito inicial? R$'))
juros = float(input('Qual a taxa de juros mensal (em %) da polpança? '))
print('Mês 1: {}'.format(soma))
sleep(1)
while x <= 23:
    cjuros = soma * (juros / 100)
    soma = cjuros + soma
    x = x + 1
    print('Mês {}: {:.2f}'.format(x, soma))
    sleep(0.5)
    #soma1 = float(input('Quanto a mais vai colocar? '))
   # soma = soma + soma1

print('Total em um ano: {:.2f}'.format(soma))
