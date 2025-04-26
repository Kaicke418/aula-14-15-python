# ***1: Verificando se o número é par ou ímpar***

num = int(input('digite um número>>'))
match num:
    case x if x % 2 == 0:
        print('é par')
    case _:
        print('é impar')

# ***2: Verificando se um número é positivo, negativo ou zero***
numero = int(input('digite um número>>'))
match  numero:
    case 0:
        print('é zero')
    case x if x > 0:
        print('é positivo')
    case _: 
        print('é negativo')
# ***3: Verificando se uma string é vazia ou não***
string = input('digite algo ou um espaço vazio>>')
match string:
    case '':
        print('é vazia')
    case _:
        print(f'está escrito {string} na string')
# ***4: Verificando se um número é maior, menor ou igual a 10***
number = int(input('digite um numero>>'))

match number:
    case x if x > 10:
        print('é maior que 10')
    case _:
        print('é menor que 10 ou igual')
# ***5: Classificando uma idade em faixas etárias -  criança, jovem, adulto, idoso***
idade = int(input('digite sua idade>>'))

match idade:
    case x if x >= 13 and x <= 17:
        print('voc~e é um adolescente')
    case x if x >= 18 and x < 60:
        print('você é um adulto')
    case x if x >= 60:
        print('você é um idoso')
    case _:
        print('você é uma criança')