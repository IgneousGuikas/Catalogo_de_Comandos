class Comandos(object):
    
    # Método construtor da classe
    def __init__(self, termo):
        self.atributo = termo
    
    # permite retornar o número de elementos de self.atributo quando for chamada em len(var)
    def __len__(self):
        return len(self.atributo)
    
    # permite que objetos de classes sejam utilizados em blocos de 'for' como um string ou uma lista
    def __iter__(self):
        return iter(self.atributo)
    
    # permite retornar um elemento de self.atributo se for uma string ou uma lista quando chamado em var[index]
    def __getitem__(self, index):
        return self.atributo[index]
    
    #  permite retornar valor de self em forma de string quando for chamado em print(var) ao invés de 
    # seu tipo de classe e sua localização na memória
    def __str__(self):
        if isinstance(self.atributo, (str, int, float, bool)):
            return self.atributo
        else:
            return str(self.atributo)
    
    # regula a interpretação que o console fará do objeto quando fora de um print(A) ou na função repr(A)
    def __repr__(self):
        return "<Classe {0} em 0x{1:x}" .format('Comandos', id(self))
    
    # permite que == seja usado para comparar valores de objetos ao invés de perguntar se são o mesmo objeto
    # funciona também com != , embora o método __neq__ permita especificar essa ação de forma mais detalhada
    def __eq__(self, objeto2):
        return self.atributo == objeto2.atributo
    def __neq__(self, objeto2):
        return self.atributo == objeto2.atributo
    
    # semelhante aos métodos __eq__ e __neq__, permitem fazer comparação entre valores de objetos
    def __lt__(self, objeto2):
        return self.atributo < objeto2.atributo
    def __gt__(self, objeto2):
        return self.atributo > objeto2.atributo
    def __le__(self, objeto2):
        return self.atributo <= objeto2.atributo
    def __ge__(self, objeto2):
        return self.atributo >= objeto2.atributo