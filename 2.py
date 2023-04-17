import math
lista = []
def raiz_exata(n):
    if math.sqrt(n)%1==0:
        return True
    return False
def isFibo(n):
    if raiz_exata(5*(n**2)+4) or raiz_exata(5*(n**2)-4):
        return True
    return False
n = int(input("Digite um número: "))
if isFibo(n):
    print(f"O número {n} pertence à sequencia de Fibonacci")
else:
    print(f"O número {n} não pertence à sequencia de Fibonacci")
