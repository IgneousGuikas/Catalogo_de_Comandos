dicionario = {}
dicionario2 = dict()
dicionario3 = {'casa': 3.3, 'teste': 9}

dicionario['teste'] = 9 # dicionario[chave] = value
dicionario['casa'] = 3.3
dicionario['predio'] = 4


print(dicionario)
print(dicionario3)


for i in dicionario:
    print(i)
    print(i,' ',dicionario[i])
    print()

print()
for i,e in dicionario.items():
    print(i)
    print(e)
    print()

chaves = dicionario.keys()
print('''
_______________________________________________________________________________
''')
for i in chaves:
    print(i)

valores = dicionario.values()
print('''
_______________________________________________________________________________
''')
for i in valores:
    print(i)

print('''
_______________________________________________________________________________
''')

del dicionario['casa']
print(dicionario)

print('''
_______________________________________________________________________________
''')


d = {}

while True:
    esp = input('Esporte: ')
    if esp == 'fim':
        break
    elif esp in d:
        d[esp] += 1
    else:
        d[esp] = 1
print(d)

for i,e in d.items():
    print(i,' ',e)


print('''
_______________________________________________________________________________
''')

p = dict()

for i in 'parrot':
    if i not in p:
        p[i] = 1
    else:
        p[i] += 1

print(p)

def inverter_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


inverso = inverter_dict(p)
print(inverso)

print('''
_______________________________________________________________________________
''')





















print('''
_______________________________________________________________________________
''')


def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError('o valor não aparece no dicionário')

h = {'a': 1, 'b': 2}

print(h)
print(h.items())
print(h)
print(h.keys())
print(h)
print(h.values())
print(h)
print(h.get('a'))
print(h)





k = reverse_lookup(h,1)
print(k)
print(h.pop('a'))
print(h)
k = reverse_lookup(h,1)
print(k)