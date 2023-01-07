from ordenacao import *


class Pessoa:
    def __init__(self):
        self.nome = input("Digite o nome do aluno: ")
        self.nota = input("Digite a nota do aluno: ")
        self.matricula = input("Digite a matricula: ")

    def __str__(self):
        return self._repr_()

    def __repr__(self) -> str:
        return str(self.matricula)+";"+self.nome+";"+str(self.nota)



tamanho = int(input("Digite a quantidade de alunos: "))

pessoa = [0]*tamanho

i = 0

while i < tamanho:
    pessoa[i] = Pessoa()
    i = i+1

    
lista = []

for i in range(tamanho):
    lista.append(pessoa[i])


selection = int(input("Digite o tipo de ordenacao\n 1 - Quick Sort\n 2 - Selection Sort\n 3 - Merge sort \n 4 - Insertion Sort \n 5 - MinHeapSort \n 6 - MaxHeapSort \n: "))
selectionType = int(input("Digite o parametro da ordenacao\n 1 - Nome\n 2 - Nota\n 3 - Matricula\n: "))


print(lista)
if selection == 1:
    quickSort(lista, selectionType)
    print(lista)
if selection == 2:
    selectionSort(lista, selectionType)
    print(lista)
if selection == 3:
    mergeSort(lista, selectionType)
    print(lista)
if selection == 4:
    insertionSort(lista, selectionType)
    print(lista)


i = 0

if selection == 5 or selection == 6:
    alunosSort = []
    if selection == 5:
        heap = MinHeap(tamanho) 
        for i in range(tamanho):
            heap.insert(pessoa[i], selectionType)

    if selection == 6:
        heap = MaxHeap(tamanho)
        for i in range(tamanho):
            heap.insert(pessoa[i], selectionType)
    while i <= tamanho:
        alunosSort.append(heap.remove(selectionType))
        i = i+1
    print(alunosSort)

