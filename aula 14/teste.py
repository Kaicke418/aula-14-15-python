import timeit  

# TESTE COM O MATCH*******


def teste1 ():
    escolha  =  'z'

    match escolha:
        case 'z':
            print('Acertou ')
        case _:
            print('errou') 

# teste1()
time = timeit.timeit(teste1, number=10)
print('função1', time)


# -----------------------------------

# TESTE COM CONDICIONAL IF*********

def teste2():
    escolha  =  'z'

    if escolha == 'z':
        print('Acertou ')
    else:
        print('errou') 

time = timeit.timeit(teste2, number=10)
print('função2', time)



