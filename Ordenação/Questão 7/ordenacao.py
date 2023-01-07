#Selection Sort
def selectionSort(lista, type):
    tamanho = len(lista)
    if type == 1:
        for i in range(tamanho-1):
            minIndex = i
            for j in range(i, tamanho):
                if lista[j].matricula < lista[minIndex].matricula:
                    minIndex = j
            if lista[i].matricula > lista[minIndex].matricula:
                lista[i], lista[minIndex] = lista[minIndex], lista[i]
    elif type == 2:
        for i in range(tamanho-1):
            minIndex = i
            for j in range(i, tamanho):
                if lista[j].nome < lista[minIndex].nome:
                    minIndex = j
            if lista[i].nome > lista[minIndex].nome:
                lista[i], lista[minIndex] = lista[minIndex], lista[i]
    else:
        for i in range(tamanho-1):
            minIndex = i
            for j in range(i, tamanho):
                if lista[j].nota < lista[minIndex].nota:
                    minIndex = j
            if lista[i].nota > lista[minIndex].nota:
                lista[i], lista[minIndex] = lista[minIndex], lista[i]

#Insertion Sort
def insertionSort(lista, type):
    tamanho = len(lista)
    if type == 1:
        for i in range(1, tamanho):
            key = lista[i]
            j = i-1
            while j>=0 and lista[j].matricula > key.matricula:
                lista[j+1] = lista[j]
                j -=1
            lista[j+1] = key
    elif type == 2:
        for i in range(1, tamanho):
            key = lista[i]
            j = i-1
            while j>=0 and lista[j].nome > key.nome:
                lista[j+1] = lista[j]
                j -=1
            lista[j+1] = key
    else:
        for i in range(1, tamanho):
            key = lista[i]
            j = i-1
            while j>=0 and lista[j].nota > key.nota:
                lista[j+1] = lista[j]
                j -=1
            lista[j+1] = key

#Merge Sort
def mergeSort(lista, type, init=0, end=None):
    if end is None:
        end = len(lista)
    if (end-init) > 1:
        middle = (end+init)//2
        mergeSort(lista, type, init, middle)
        mergeSort(lista, type, middle, end)
        merge(lista, type, init, middle, end)

def merge(lista, type, init, middle, end):
    leftList = lista[init:middle]
    rightList = lista[middle:end]
    topLeft, topRight = 0, 0
    if type == 1:
        for i in range(init, end):
            if topLeft >= len(leftList):
                lista[i] = rightList[topRight]
                topRight +=1
            elif topRight >= len(rightList):
                    lista[i] = leftList[topLeft]
                    topLeft +=1
            elif leftList[topLeft].matricula < rightList[topRight].matricula:
                lista[i] = leftList[topLeft]
                topLeft +=1
            else:
                lista[i] = rightList[topRight]
                topRight +=1
    elif type == 2:
        for i in range(init, end):
            if topLeft >= len(leftList):
                lista[i] = rightList[topRight]
                topRight +=1
            elif topRight >= len(rightList):
                    lista[i] = leftList[topLeft]
                    topLeft +=1
            elif leftList[topLeft].nome < rightList[topRight].nome:
                lista[i] = leftList[topLeft]
                topLeft +=1
            else:
                lista[i] = rightList[topRight]
                topRight +=1
    else:
        for i in range(init, end):
            if topLeft >= len(leftList):
                lista[i] = rightList[topRight]
                topRight +=1
            elif topRight >= len(rightList):
                    lista[i] = leftList[topLeft]
                    topLeft +=1
            elif leftList[topLeft].nota < rightList[topRight].nota:
                lista[i] = leftList[topLeft]
                topLeft +=1
            else:
                lista[i] = rightList[topRight]
                topRight +=1


#Quick Sort
def quickSort(lista, type, init=0, end=None):
    if end is None:
        end = len(lista)-1
    if init < end:
        pivot = partition(lista, type, init, end)
        quickSort(lista, type, init, pivot-1)
        quickSort(lista, type, pivot+1, end)

def partition(lista, type, init, end):
    pivot = lista[end]
    index = init
    if type == 1:
        for j in range(init, end):
            if lista[j].matricula <= pivot.matricula:
                lista[j], lista[index] = lista[index], lista[j]
                index +=1
        lista[index], lista[end] = lista[end], lista[index]
        return index
    elif type == 2:
        for j in range(init, end):
            if lista[j].nome <= pivot.nome:
                lista[j], lista[index] = lista[index], lista[j]
                index +=1
        lista[index], lista[end] = lista[end], lista[index]
        return index
    else:
        for j in range(init, end):
            if lista[j].nota <= pivot.nota:
                lista[j], lista[index] = lista[index], lista[j]
                index +=1
        lista[index], lista[end] = lista[end], lista[index]
        return index



class MinHeap:
    def __init__(self, capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size = 0

 # Métodos de procura de index dos pais e dos filhos
 
    def fatherIndex(self, index):
        return (index-1)//2

    def leftChildIndex(self, index):
        return 2*index + 1

    def rightChildIndex(self, index):
        return 2*index + 2

# Métodos para verificar a existência dos pais e dos filhos

    def hasFather(self, index):
        return self.fatherIndex(index) >=0

    def hasLeft(self, index):
        return self.leftChildIndex(index) < self.size

    def hasRight(self, index):
        return self.rightChildIndex(index) < self.size

# Métodos para definir as folhas

    def father(self, index):
        return self.storage[self.fatherIndex(index)]

    def leftChild(self, index):
        return self.storage[self.leftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.rightChildIndex(index)]

# Verifica se está cheio
    def isFull(self):
        return self.size == self.capacity

# Método de troca
    def swap(self, index1, index2):
        aux = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = aux
    
# Método de inserção
    def insert(self, data, type):
        if(self.isFull()):
            print("Está Cheio!")
        self.storage[self.size] = data
        self.size +=1
        if type == 1:
            self.upHeapNome(self.size -1)
        if type == 2:
            self.upHeapNota(self.size -1)
        if type == 3:
            self.upHeapMatricula(self.size -1)


# Organiza o Heap de baixo para cima
    def upHeapNome(self, index):
        while(self.hasFather(index) and self.father(index).nome > self.storage[index].nome):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)

    def upHeapNota(self, index):
        while(self.hasFather(index) and self.father(index).nota > self.storage[index].nota):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)
            
    def upHeapMatricula(self, index):
        while(self.hasFather(index) and self.father(index).matricula > self.storage[index].matricula):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)


    def downHeapNome(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index).nome < self.leftChild(index).nome:
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index].nome < self.storage[smallerChildIndex].nome:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

    def downHeapNota(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index).nota < self.leftChild(index).nota:
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index].nota < self.storage[smallerChildIndex].nota:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
     
    def downHeapMatricula(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index).matricula < self.leftChild(index).matricula:
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index].matricula < self.storage[smallerChildIndex].matricula:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
     
     
    def remove(self, type):
        if self.size == 0:
            print("Heap Vazio!")
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size-1]
            self.size -= 1
            if type == 1:
                self.downHeapNome()
            if type == 2:
                self.downHeapNota()
            if type == 3:
                self.downHeapMatricula()
            return data
    
    def __str__(self):
        aux = self.storage
        prim = ''
        for i in aux:
            prim += str(i) + '; '
        return prim

    def isEmpty(self):
        return self.size == 0

    def toList(self):
        if not self.isEmpty() :
            return self.storage[0:]
        else:
            return ["Empty Heap"]

    def printGraph(self):
        heap_list = self.toList()
        values = []
        for x in heap_list:
            values.append(f"{x}")
        root = build(values)
        print("\nDesenho da Heap")
        print(root)


class MaxHeap:
    def __init__(self, capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size = 0

 # Métodos de procura de index dos pais e dos filhos
 
    def fatherIndex(self, index):
        return (index-1)//2

    def leftChildIndex(self, index):
        return 2*index + 1

    def rightChildIndex(self, index):
        return 2*index + 2

# Métodos para verificar a existência dos pais e dos filhos

    def hasFather(self, index):
        return self.fatherIndex(index) >=0

    def hasLeft(self, index):
        return self.leftChildIndex(index) < self.size

    def hasRight(self, index):
        return self.rightChildIndex(index) < self.size

# Métodos para definir as folhas

    def father(self, index):
        return self.storage[self.fatherIndex(index)]

    def leftChild(self, index):
        return self.storage[self.leftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.rightChildIndex(index)]

# Verifica se está cheio
    def isFull(self):
        return self.size == self.capacity

# Método de troca
    def swap(self, index1, index2):
        aux = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = aux
    
# Método de inserção
    def insert(self, data, type):
        if(self.isFull()):
            print("Está Cheio!")
        self.storage[self.size] = data
        self.size +=1
        if type == 1:
            self.upHeapNome(self.size -1)
        if type == 2:
            self.upHeapNota(self.size -1)
        if type == 3:
            self.upHeapMatricula(self.size -1)


# Organiza o Heap de baixo para cima
    def upHeapNome(self, index):
        while(self.hasFather(index) and self.father(index).nome < self.storage[index].nome):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)

    def upHeapNota(self, index):
        while(self.hasFather(index) and self.father(index).nota < self.storage[index].nota):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)

    def upHeapMatricula(self, index):
        while(self.hasFather(index) and self.father(index).matricula < self.storage[index].matricula):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)


    def downHeapNome(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index).nome > self.leftChild(index).nome:
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index].nome > self.storage[smallerChildIndex].nome:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
     

    def downHeapNota(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index).nota > self.leftChild(index).nota:
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index].nota > self.storage[smallerChildIndex].nota:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
     

    def downHeapMatricula(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index).matricula > self.leftChild(index).matricula:
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index].matricula> self.storage[smallerChildIndex].matricula:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

     
    def remove(self, type):
        if self.size == 0:
            print("Heap Vazio!")
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size-1]
            self.size -= 1
            if type == 1:
                self.downHeapNome()
            if type == 2:
                self.downHeapNota()
            if type == 3:
                self.downHeapMatricula()
            return data
    
    def __str__(self):
        aux = self.storage
        prim = ''
        for i in aux:
            prim += str(i) + '; '
        return prim

    def isEmpty(self):
        return self.size == 0

    def toList(self):
        if not self.isEmpty() :
            return self.storage[0:]
        else:
            return ["Empty Heap"]

    def printGraph(self):
        heap_list = self.toList()
        values = []
        for x in heap_list:
            values.append(f"{x}")
        root = build(values)
        print("\nDesenho da Heap")
        print(root)