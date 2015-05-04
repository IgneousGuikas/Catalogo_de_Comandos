class Livro(object):
    '''
            Livro
    
    + nome: str
    + autor: Autor
    + preco: float
    + estoque: int
    
    + __init__(self, nome, autor, preco, estoque)
    + getNome(self): str
    + setAutor(self, autor)
    + getAutor(self): str
    + getPreco(self): float
    + setPreco(self, preco)
    + getEstoque(self): int
    + setEstoque(self, estoque)
    
    '''
    def __init__(self, nome, autor, preco, estoque):
        self.nome = nome
        self.autor = autor
        self.preco = preco
        self.estoque = estoque
    
    def getNome(self):
        return self.nome
    
    def setAutor(self, autor):
        self.autor.nome = autor
    
    def getAutor(self):
        return self.autor.nome
    
    def getPreco(self):
        return self.preco
    
    def setPreco(self, preco):
        self.preco = preco
    
    def getEstoque(self):
        return self.estoque
    
    def setEstoque(self, estoque):
        self.estoque = estoque

class Autor(object):
    '''
            Autor
    
    + nome = str
    + email = str
    + genero = str
    
    + __init__(self, nome, email, genero)
    + __str__(self): str
    + getNome(self): str
    + getEmail(self): str
    + setEmail(self, email)
    + getGenero(self): str
    + setGenero(self, genero)
    
    '''
    def __init__(self, nome, email, genero):
        self.nome = nome
        self.email = email
        self.genero = genero
    
    def __str__(self):
        return 'Nome: {0}\nEmail: {1}\nGênero: {2}'.format(self.nome, self.email, self.genero)
    
    def getNome(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
    
    def getGenero(self):
        return self.genero
    
    def setGenero(self, genero):
        self.genero = genero

autor = Autor('Olaf', 'olaf.o@hotmail.com', 'masculino')
print(autor)
L1 = Livro('abc', autor, 12.5, 20)

'''
________________________________________________________________________________________________
'''