import copy

class ponto(object):
    '''
    Representa um ponto em um ambiente 2D
    '''
    def __init__(self):
        self.x = 0
        self.y = 0
    def printa(self):
        print('(%g, %g)' %(self.x, self.y))


class retangulo(object):
    '''
    Representa um retângulo
    '''
    
    def __init__(self, vertice, largura, comprimento):
        self.ver = vertice
        self.lar = largura
        self.comp = comprimento
    def printa(self):
        print('(%g, %g), %g, %g' %(self.ver.x, self.ver.y, self.lar, self.comp))
    


print('''
_______________________________________________________________________________
''')


p1 = ponto()
print(p1.x)
p1.x = 2
print(p1.x)

print('''
_______________________________________________________________________________
''')

p2 = p1
p3 = copy.copy(p1)

p1.printa()
p2.printa()
p3.printa()
print()
print(p2 is p1)
print(p2 == p1)
print()
print(p3 is p1)
print(p3 == p1)

print('''
_______________________________________________________________________________
''')

box1 = retangulo(p1, 50, 100)

box2 = copy.copy(box1)

box1.printa()
box2.printa()
print()
print(box2 is box1)
print(box2.ver is box1.ver)

print('\n\n')

box3 = copy.deepcopy(box1)

box1.printa()
box3.printa()
print()
print(box3 is box1)
print(box3.ver is box1.ver)