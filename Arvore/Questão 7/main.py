from heap import MinHeap,MaxHeap



def Heapify (vetor,tamanho,selection):
    if selection == 1:
        escolha = MinHeap(tamanho)
        for numero in vetor:
            escolha.insert(numero)
        escolha.printGraph()


    if selection == 2:
        escolha = MaxHeap(tamanho)
        for numero in vetor:
            escolha.insert(numero)
        escolha.printGraph()



selection = 0
i = 0
vetor = []




tamanho = int(input("Digite o tamanho de seu vetor: "))


while i < tamanho:
    vetor.append(input("Digite os numeros de seu vetor: "))
    i = i+1

selection = int(input("Selecione 1 para MinHeap e 2 para MaxHeap: "))

Heapify(vetor,tamanho,selection)
