#Encapsulamento exemplo


class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

conta = Conta(200)
conta.depositar(25)
print(conta.consultar_saldo())



 

#Polimorfismo exemplo


class Cachorro: 
    def emitir_som(self): 
        print("Au au!") 
 
class Gato: 
  def emitir_som(self): 
        print("Miau!") 
 
animal1 = Cachorro() 
animal2 = Gato() 
 
animal1.emitir_som() 
animal2.emitir_som() 
