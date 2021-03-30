def verificarCPF(cpf):"""

    :param cpf: Os 11 dígitos do CPF sem pontos e traços
    :return: Se o CPF é válido, e sendo válido retorna de qual região é o CPF
    """
    soma = 0  # acumula o valor da soma da multiplicação
    cod = 10  # valor a ser multiplicado
    for c in range(0, 9):
        ver = cpf[c]  # fatia a string na posição do range (c)
        soma += int(ver) * cod  # tranforma a string em inteiro e multiplica pelo cod
        cod -= 1  # diminui o cod, pois o valor a ser multiplicado é decrescente
    cod1 = soma % 11  # resto da divisão inteira da soma
    if cod1 == 0 or cod1 == 1:  # se o resto for igual a 0 ou 1
        dig1 = 0  # o primeiro digito verificador recebe 0
    else:  # se o resto for diferente de 0 ou 1
        dig1 = 11 - cod1 # o primeiro digito verificador recebe 11 menos o resto
    soma = 0
    cod = 10
    for c in range(1, 10):
        ver = cpf[c]
        soma += int(ver) * cod
        cod -= 1
    cod2 = soma % 11
    if cod2 == 0 or cod2 == 1:
        dig2 = 0
    else:
        dig2 = 11 - cod2
    dig1 = str(dig1)
    dig2 = str(dig2)
    dig3 = dig1 + dig2
    print(f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
    if cpf[9:] == dig3:
        print('CPF válido')
        if cpf[8] == '0':
            print('Seu CPF foi feito em RS.')
        elif cpf[8] == '1':
            print('Seu CPF foi feito na região Centro-Oeste.')
        elif cpf[8] == '2':
            print('Seu CPF foi feito na região Norte')
        elif cpf[8] == '3':
            print('Seu CPF foi feito em CE, MA ou PI.')
        elif cpf[8] == '4':
            print('Seu CPF foi feito em AL, PB, PE ou RN.')
        elif cpf[8] == '5':
            print('Seu CPF foi feito em BA ou SE.')
        elif cpf[8] == '6':
            print('Seu CPF foi feito em MG.')
        elif cpf[8] == '7':
            print('Seu CPF foi feito em RJ ou ES.')
        elif cpf[8] == '8':
            print('Seu CPF foi feito em SP.')
        elif cpf[8] == '9':
            print('Seu CPF foi feito em PR ou SC.')

    else:
        print('CPF inválido')
