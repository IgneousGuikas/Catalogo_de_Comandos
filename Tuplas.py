t = 'a'
print(type(t))
t = 'a',
print(type(t))

print('''
_________________________________________________________________
''')


t2 = tuple('arroz')
print(t2)


print('''
_________________________________________________________________
''')


print(t2)
t2 = ('A',) + t2[1:]
print(t2)
t2 = ('A',) + t2[0:]
print(t2)


print('''
_________________________________________________________________
''')


s = 'abc'
n = [0,1,2]
list_of_tuples = list(zip(s,n))
print(list_of_tuples)
for letter,number in list_of_tuples:
    print(letter,number)
dicionario = dict(list_of_tuples)
print(dicionario)


print('''
_________________________________________________________________
''')


dicionario2 = dict()
first = input('digite seu primeiro nome: ')
last = input('digite seu último nome: ')
number = input('digite seu telefone: ')
dicionario2[last,first] = number
print(dicionario2)


print('''
_________________________________________________________________
''')


a = (0,1,2)
b = (0,2,2)
if a < b:
    print(True)