matriz = []

for i in range(4):
    linhas = [0]*4
    matriz.append(linhas)
print(matriz)


for i in range(4):
    for j in range(4):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0
print(matriz)

print('''
-----------------------------------------
''')


from numpy import *

m = zeros([4,4])
s = ones([2,3])

print(m)
print()
print(s)

print('''
-----------------------------------------
''')


a = array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

print()

a[1][1] = 15
print(a)

print()

a[0][0] = 15
print(a)

a = array([[1,2,3],[4,5,6],[7,8,9]])
print(a.dot(ones([3,3])))

print('''
-----------------------------------------
''')


a = ([[1,2,1],[2,-1,1],[3,1,-1]])
b = ([8,3,2])
x = linalg.solve(a,b) #sistemas lineares
print(x)