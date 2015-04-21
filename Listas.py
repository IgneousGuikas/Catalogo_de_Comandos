from random import shuffle

list1 = [1,2,3,4,5,6,7,8,9]
list2 = list(range(2, 6))

termo = int(input('Digite um termo: '))
if termo in list1:
    print('O termo %d está em list1' %termo)

print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))

print(list1[2 : 4])
print(list1[:: -1])

print(list2)

shuffle(list1)
print(list1)

for u in list1:
    print(u)

del list1[1]
print(list1)

list3 = [x for x in range(5)]
print(list3)
list4 = [0.5*x for x in list3]
print(list4)
list5 = [x for x in list4 if x < 1.5]
print(list5)

list6 = [2,3,4,7,21,4]
list6.append(19)
print(list6)
print('')
print(list6.count(4))
print('')#Returns the number of times element x appears in the list
list6.extend(list1)
print(list6)
print('')
print(list6.index(21))
print('''
_______________________________________________________________________________
''')
list6.insert(4, 22)# list6.insert(index, object)
print('')
print(list6)
list6.sort()
print(list6)
list6.reverse()
print(list6)

print('')
list7 = 'Rodrigo Ronchail Gikas'.split()
print(list7)

print('')
list8 = []
for i in range(10):
    list8.append(eval(input('Digite números de 0 a 9 por Enter: ')))
print(list8)

s = input('Digite números de 0 a 9 entre Espaços: ')
d = s.split()
list9 = [eval(x) for x in d]
print(list9)

list10 = ['alpha','beta','gamma']

print(list10.index('alpha'))

for x, e in enumerate(list10):
    print(x)
    print(e)

list11 = list('palavra')
print(list11)
