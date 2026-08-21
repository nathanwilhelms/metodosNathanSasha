import numpy as np
import matplotlib.pyplot as plt
import math as math

# criterio de parada SCARVOROUGHT, 1966
na = 6
Eppara = 0.5*10**(2-na)
print("Valor de Eppara:", Eppara)

u = 6.737947e-3
x = 5

# ---------------- Abordagem 1: série direta de e^-x ----------------

def serieDireta(x, n):
    return ((-1)**n)*(x**n)/math.factorial(n) # alternada


soma = 0
Ept = 100
Epest = 100
i = 0
ITERACAO1 = []
SOMA1 = []
EPT1 = []
EPEST1 = []

while Epest > Eppara:
    somaant = soma
    soma += serieDireta(x, i)
    Ept = abs((u-soma)/u)*100

    if i == 0:
        Epest = 100
    else:
        Epest = abs((soma-somaant)/soma)*100

    ITERACAO1.append(i)
    SOMA1.append(soma)
    EPT1.append(Ept)
    EPEST1.append(Epest)
    i += 1

print("Abordagem 1 (série direta) - termos necessários:", i, " soma final:", soma)

plt.plot(ITERACAO1, SOMA1, '--or', label='Estimativa')
plt.legend()
plt.title('Abordagem 1: série direta de $e^{-x}$')
plt.xlabel('Iterações')
plt.ylabel('Estimativa $e^{-5}$')
plt.grid()
plt.show()

plt.plot(ITERACAO1, EPT1, '--or', label='Ept (verdadeiro)')
plt.plot(ITERACAO1, EPEST1, '--ob', label='Epest (estimado)')
plt.legend()
plt.title('Abordagem 1: série direta de $e^{-x}$')
plt.xlabel('Iterações')
plt.ylabel('Erro (%)')
plt.grid()
plt.show()

# ---------------- Abordagem 2: e^-x = 1/e^x ----------------

def serieMac(x, n):
    return (x**n)/math.factorial(n)

somax = 0
soma = 0
Ept = 100
Epest = 100
i = 0
ITERACAO2 = []
SOMA2 = []
EPT2 = []
EPEST2 = []

while Epest > Eppara:
    somaant = soma
    somax += serieMac(x, i)
    soma = 1/somax
    Ept = abs((u-soma)/u)*100

    if i == 0:
        Epest = 100
    else:
        Epest = abs((soma-somaant)/soma)*100

    ITERACAO2.append(i)
    SOMA2.append(soma)
    EPT2.append(Ept)
    EPEST2.append(Epest)
    i += 1

print("Abordagem 2 (1/e^x) - termos necessários:", i, " soma final:", soma)

plt.plot(ITERACAO2, SOMA2, '--or', label='Estimativa')
plt.legend()
plt.title('Abordagem 2: $e^{-x} = 1/e^{x}$')
plt.xlabel('Iterações')
plt.ylabel('Estimativa $e^{-5}$')
plt.grid()
plt.show()

plt.plot(ITERACAO2, EPT2, '--or', label='Ept (verdadeiro)')
plt.plot(ITERACAO2, EPEST2, '--ob', label='Epest (estimado)')
plt.legend()
plt.title('Abordagem 2: $e^{-x} = 1/e^{x}$')
plt.xlabel('Iterações')
plt.ylabel('Erro (%)')
plt.grid()
plt.show()
