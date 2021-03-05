n1 = int(input('digite A: '))
n2 = str(input('digite B: '))
# if n1 > n2:
#     print (n1, 'é o maior número!')
if n1 == n2:
    print("Os numeros sao iguais")
else: 
    print (n2, 'é o maior número!')



'''
Em alguns casos precisamos de mais de um estrutura de 
ifs e acabamos criando um if dentro do outro, o que muitas
 vezes pode complicar o código. Esse tipo de "junção" de ifs
  é chamado de if aninhados (nested ifs).

numero = int(raw_input("Por favor, insira um número:"))
if numero > 0:
    print 'Você digitou um número positivo!'
else:
    if numero < 0:
        print 'Você digitou um número negativo'
    else:
        print 'Você digitou zero!'


Para simplificar isso temos o elif que é a junção de um else com um if. 

numero = int(raw_input("Por favor, insira um número:"))
if numero > 0:
    print 'Você digitou um número positivo!'
elif numero < 0:
    print 'Você digitou um número negativo'
else:
    print 'Você digitou zero!'


A estrutura de if/elif/else só tem 2 restrições:

Deve começar com um if, isto é, não podemos começar com um elif e muito menos com um else;
Só pode ter um ou nenhum else na estrutura, isto é, o else não é obrigatório, mas caso ele seja usado, só pode constar uma unica vez na estrutura;

Em suma, depois do if primordial podemos colocar quantos elifs quisermos e acabar a estrutura assim. Caso seja necessário podemos utilizar um, e apenas um, else.



'''