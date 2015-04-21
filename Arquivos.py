fin = open('teste.txt','r+')
print(type(fin))
line = fin.readline()
print(type(line))
print(line)
fin.close()


print('''
-----------------------------------------
''')

fin = open('teste2.txt','r')
palavras = []

for i in fin:
    palavras.append(i)
print(palavras)
fin.close()

fin = open('teste2.txt','r')

palavras2 = []
for i in fin:
    word2 = i.strip()
    palavras2.append(word2)
print(palavras2)
fin.close()

print('''
-----------------------------------------
''')

fin = open('teste.txt','r')
palavras3 = (fin.readline()).split()
print(palavras3)
fin.close()

for letter in palavras3:
    for i in letter:
        if i == 'e':
            print(letter)

print('''
-----------------------------------------
''')

fin = open('output.txt','w')
fin.write('Hello\n')
fin.write('World')
fin.close()

fin = open('output2.txt','a')
x = 52
fin.write(str(x))
fin.close()

print('''
-----------------------------------------
''')

import os
'''
os.mkdir('a')
os.mkdir('b')
os.mkdir('c')

    Colocar isso no console
'''
print(os.getcwd())
os.chdir('a')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('b')
print(os.getcwd())
os.chdir('../c')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
# Muda a programação em execução para outras pastas para acessar arquivos de texto



print('''
-----------------------------------------
''')


fin = open('teste3.txt','w+',encoding = 'utf-8')
fin.write('áááééóó')
fin.close()
'''
os.rename(nome_atual,	novo_nome)
os.remove(nome_do_arquivos)
os.mkdir(nome_da_pasta)
os.chdir(nome_da_pasta)
'''


print('''
-----------------------------------------
''')


fin = open('teste2.txt','r+')

for i in fin.readline():
    print(i)
fin.close()

fin = open('teste2.txt','r+')

for i in fin.readlines():
    print(i)
fin.close()

