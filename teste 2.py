arquivo = open('teste2.txt','r+')
ler = arquivo.readlines()
print(ler)
print(ler[0])

linha = ler[0]
print(linha)

valores = linha.split(',')
print(valores)

soma = 0

for i in valores:
    soma += int(i)
    print(i)
print('Soma = ' + soma)

arquivo.write(','+str(soma))
arquivo.close()