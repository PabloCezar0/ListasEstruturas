from fila import Queue
from pilha import Stack


fatorar = Queue()
decrescente = Stack()

d = 2
numero = int(input("Digite o numero a ser fatorado: "))



while numero != 1:
    if numero%d == 0:
        numero = numero/d
        fatorar.queue(d)
    else:
        d += 1 
    

while len(fatorar) > 0:
    decrescente.push(fatorar.dequeue())


while len(decrescente) > 0:
    print(decrescente.pop(),  end="*")