from binarytree import build #somente para o build professor, perdao

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
    def insert(self, data):
        if(self.isFull()):
            print("Está Cheio!")
        self.storage[self.size] = data
        self.size +=1
        self.upHeap(self.size -1)


# Organiza o Heap de baixo para cima
    def upHeap(self, index):
        while(self.hasFather(index) and self.father(index) > self.storage[index]):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)


    def downHeap(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index] < self.storage[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
     
    def remove(self):
        if self.size == 0:
            print("Heap Vazio!")
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size-1]
            self.size -= 1
            self.downHeap()
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
    def insert(self, data):
        if(self.isFull()):
            print("Está Cheio!")
        self.storage[self.size] = data
        self.size +=1
        self.upHeap(self.size -1)


# Organiza o Heap de baixo para cima
    def upHeap(self, index):
        while(self.hasFather(index) and self.father(index) < self.storage[index]):
            self.swap(self.fatherIndex(index),index)
            index = self.fatherIndex(index)


    def downHeap(self):
        index = 0
        while(self.hasLeft(index)):
            smallerChildIndex = self.leftChildIndex(index)
            if self.hasRight(index) and self.rightChild(index) > self.leftChild(index):
                smallerChildIndex = self.rightChildIndex(index)
            if self.storage[index] > self.storage[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex
     
    def remove(self):
        if self.size == 0:
            print("Heap Vazio!")
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size-1]
            self.size -= 1
            self.downHeap()
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