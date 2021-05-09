# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: __________@aluno.faculdadeimpacta.com.br

def eh_primo(n):

    if n < 2:
        return False

    for x in range(2, n):

        if n % x == 0:
            return False

    return True


def lista_primos(n):

    return [i for i in range(2, n) if eh_primo(i)]


def lista_primos(n):

    numeros_primos = list()

    for x in range(2, n):

        if eh_primo(x) == True:
            numeros_primos.append(x)

    return numeros_primos


def conta_primos(s):

    s = sorted(s)

    d = dict()

    for i in s:

        if eh_primo(i):

            if i in d:
                d[i] += 1

            else:
                d[i] = 1

    return d


def eh_armstrong(n):

    armstrong = len(str(n))
    i = 0
    aux = n
    while aux > 0:
       digit = aux % 10
       i += digit ** armstrong
       aux //= 10
    if n == i:
        return True
    else:
        return False


def eh_quase_armstrong(n):

    digitos = list()

    res = 0

    i = n

    while i > 0:
        digitos.append(i % 10)
        i //= 10

    n_digitos = len(digitos)

    for d in digitos:
        res += d**n_digitos

    return res == n + 1 or res == n + 1


def lista_armstrong(n):

    return [i for i in range(0, n) if eh_armstrong(i)]


def lista_armstrong(n):

    numeros = list()

    for x in range(0, n):

        if eh_armstrong(x) == True:
            numeros.append(x)

    return numeros


def eh_perfeito(n):

    div = list()

    for x in range(1, n):

        if n % x == 0:
            div.append(x)

    return sum(div) == n


def lista_perfeitos(n):

    return [i for i in range(1, n) if eh_perfeito(i)]


def lista_perfeitos(n):

    numeros = list()

    for x in range(1, n):

        if eh_perfeito(x):
            numeros.append(x)

    return numeros
