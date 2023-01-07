from pilha import Stack
import random



pilha1 = Stack()
pilha2 = Stack()
pilha3 = Stack()
pilha4 = Stack()


while len(pilha1) + len(pilha2) + len(pilha3) != 52:

        pilha = random.randint(1,6)
        cartaLetra = random.randint(1,4)

        if(cartaLetra == 1):
            carta = "♠" + str(random.randint(1,10))
        if(cartaLetra == 2):
            carta = "♣" + str(random.randint(1,10))
        if(cartaLetra == 3):
            carta = "♥" + str(random.randint(1,10))
        if(cartaLetra == 4):
            carta = "♦" + str(random.randint(1,10))

        if pilha == 1:
            pilha1.push(carta) 
        if pilha == 2:
            pilha2.push(carta) 
        if pilha == 3:
            pilha3.push(carta) 
        if pilha == 4 and len(pilha1) > 1:
            pilha1.pop() 
        if pilha == 5 and len(pilha2)> 1:
            pilha2.pop() 
        if pilha == 6 and len(pilha3)> 1:
            pilha3.pop() 

while len(pilha1) + len(pilha2) + len(pilha3) > 0:

        if len(pilha1) > 0:
            pilha4.push(pilha1.pop())

        if len(pilha2) > 0:
            pilha4.push(pilha2.pop())
    
        if len(pilha3) > 0:
            pilha4.push(pilha3.pop())
    
    


print("\nCartas embaralhadas:")


while len(pilha4) > 0:
    print(pilha4.pop()) 