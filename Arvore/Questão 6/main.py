from heap import MinHeap,MaxHeap




selection = 0
i = 0
vetor = []
isMin = 0
isMax = 0
noHeap = 0




tamanho = int(input("Digite o tamanho de seu vetor: "))
min = MinHeap(tamanho)
max = MaxHeap(tamanho)


while i < tamanho:
    vetor.append(input("Digite os numeros de seu vetor: "))
    i = i+1


i = 0

for numero in vetor:
    min.insert(numero)
    max.insert(numero)

    if(numero == min.storage[i]):
        
        isMin = isMin +1

    if(numero == max.storage[i]):

        isMax = isMax +1

    i =  i+1
if (isMin == tamanho):
    print("-1")

if(isMax == tamanho):
    print("1")

if(isMin != tamanho and isMax != tamanho):
    print("0")


