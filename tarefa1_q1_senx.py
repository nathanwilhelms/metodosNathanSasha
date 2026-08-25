import numpy as np
import matplotlib.pyplot as plt
import math as math

# criterio de parada SCARVOROUGHT, 1966
na = 6
Eppara = 0.5*10**(2-na)
print("Valor de Eppara:", Eppara)

def serieMacSen(x, n):
    return ((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1)

XVALORES = [math.pi/6, math.pi/2, 3*math.pi/2]

for x in XVALORES:

    u = math.sin(x)
    print("Valor de x:", x, " Valor de u:", u)

    soma = 0
    Ept = 100
    Epest = 100
    i = 0
    ITERACAO = []
    SOMA = []
    EPT = []
    EPEST = []

    while Epest > Eppara:
        somaant = soma
        soma += serieMacSen(x, i)
        Ept = abs((u-soma)/u)*100

        if i == 0:
            Epest = 100
        else:
            Epest = abs((soma-somaant)/soma)*100

        ITERACAO.append(i)
        SOMA.append(soma)
        EPT.append(Ept)
        EPEST.append(Epest)
        i += 1

    print("Termos necessarios:", i)
    print("Soma final:", soma)

    plt.plot(ITERACAO, SOMA, '--or', label='Estimativa')
    plt.legend()
    plt.title(f'Série de Maclaurin para sen(x), x={x:.3f}')
    plt.xlabel('Iterações')
    plt.ylabel('Estimativa $sen(x)$')
    plt.grid()
    plt.show()

    plt.plot(ITERACAO, EPT, '--or', label='Ept (verdadeiro)')
    plt.plot(ITERACAO, EPEST, '--ob', label='Epest (estimado)')
    plt.legend()
    plt.title(f'Série de Maclaurin para sen(x), x={x:.3f}')
    plt.xlabel('Iterações')
    plt.ylabel('Erro (%)')
    plt.grid()
    plt.show()
