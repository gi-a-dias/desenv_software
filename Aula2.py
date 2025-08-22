class Celular:
    def __init__(self, marca, ano, SO):
        #pubicos
        self.marca = marca
        self.ano = ano
        #privados
        self.__SO = SO
    #Override para print
    def __str__(self):
        return f"{self.marca} \nLançamento: {self.ano} \nSO: {self.__SO}"

#Instanciando
c1 = Celular("Samsung", 2023, "Android")
c2 = Celular("Iphone", 2024, "iOS")

#Usando os objetos
print(c1)
print(c2)
