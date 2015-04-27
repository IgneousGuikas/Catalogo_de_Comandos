class Ponto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})" .format(self.x, self.y)

class Ponto3D(Ponto, object):
    def __init__(self, x, y, z):
        Ponto.__init__(self, x, y)
        self.z = z
    def __str__(self):
        return "({0},{1},{2})" .format(self.x, self.y, self.z)


A = Ponto(2,3)
print(A)
B = Ponto3D(4,5,6)
print(B)


# Tente fazer mudanças nos atributos de Ponto() para ver o que acontece com o resultado em Ponto3D