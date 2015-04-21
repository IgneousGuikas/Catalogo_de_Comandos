palavra = 'Insper'

print(len(palavra))
print(palavra[0])
print(palavra[1])
print(palavra[2])
print(palavra[3])
print(palavra[4])
print(palavra[5])

print(palavra*2)
print(palavra[0:3])

palavra.find('er')
palavra.replace('Ins','Su')

print('Meu %s'%(palavra))

print('= %5.3f'%(1.123456789))
# %5.3f   5 espaços: _ _ _ _ _
#         3 números antes da vírgula: 21.123

print(palavra.upper())
print(palavra.lower())
print(palavra.swapcase())
print(palavra[::-1])

print("""
        Olá,
        como vai você.
        """)
# %s = substituido por Strings
# %d = substituido por números inteiros
# %f = substituido por números decimais