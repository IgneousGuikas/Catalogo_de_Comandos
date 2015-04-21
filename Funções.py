def multiplo (a,b):
    return (a%b == 0)
print(multiplo(8,4))

print()

def maximo (a,b):
    L = [a,b]
    return max(L)
print(maximo(5,30))

print()

def quadrado (l):
    return (l**2)
print(quadrado(5))

def triangulo (b,h):
    return ((b*h)/2)
print(triangulo(4,5))

print()

def pesquisa (lista, termo):
    if termo in lista:
        return lista.index(termo)
    return None
lista1 = ['alpha','beta','gamma']
print(pesquisa(lista1,'gamma'))

print()

a = 5
def mudar ():
    a = 7
    print('Dentro: %d' %a)
print('Antes: %d' %a)
mudar()
print('Depois: %d' %a)

print()

a = 5
def mudar ():
    global a
    a = 7
    print('Dentro: %d' %a)
print('Antes: %d' %a)
mudar()
print('Depois: %d' %a)

print()

def fatorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)
print(fatorial(5))

def mdc (a,b): # Maior Divisor Comum
    if b == 0:
        return a
    elif b > a:
        return 'Inválido. b > a'
    else:
        return mdc(b,(a%b))
    return None
print(mdc(20,12))

def mmc (a,b):
    if b == 0 or b == a:
        return a
    else:
        return (abs(a*b))/mdc(a,b)
print(mmc(20,12))

print()

def tamanho_string(string,minimo,maximo):
    v = len(string)
    if v > minimo and v < maximo:
        return True
    else:
        return False
print(tamanho_string(input('Digite uma string: '),3,6))

print()

def barra (n=40, caractere='*'):
    print(caractere*n)
barra()
barra(10)
barra(10,'-')

print()
print('alpha')
print()

def soma (primeiro, segundo, caractere='*'):
    s = primeiro+segundo
    print(caractere*s)
soma(2,3)
soma(primeiro=3,segundo=4)
soma(segundo=4,primeiro=3)

print()
print('beta')
print()

def insira (a,b,foper):
    return foper(a,b)
insira(2,3,soma)

print()
print('gamma')
print()

def empacotado (n=10,c='*'):
    print('\n',c*n)
    print('a')
L = [2,'*']
V = [ [10,'-'] , [5,'*'] , [8,'/'] ]
empacotado()
empacotado(*L)
for e in V:
    empacotado(*e)

print()
print('theta')
print()

def soma_empacotada (*numeros):
    s = 0
    for x in numeros:
        s += x
    return s
C = [1,2,3,4,5,6,7]
print(soma_empacotada(*C))
print(soma_empacotada(4,5,6))

print()
print('pi')
print()

alpha = lambda x: x*2
print(alpha(4))

print()
print('omega')
print()

def localize(cidade):
    if cidade == 'Sao Paulo':
        return ("23° 32' 51\" S","46° 38' 10\" W")
    elif cidade == 'Rio de Janeiro':
        return ("22° 54' 10\" S","43° 12' 27\" W")

print(localize('Sao Paulo'))
cidade = 'Sao Paulo'
latitude,longitude = localize('Sao Paulo')
print('%s está localizado a %s, %s.'%(cidade,latitude,longitude))

print("""

lambda

""")

def fibonacci (n):
    L = [0,1]
    for x in range(2,n):
        L += [L[x-1] + L[x-2]]
    return L
print(fibonacci(5))