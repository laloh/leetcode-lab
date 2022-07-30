import sys

class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1 

    # function to return the position of
    # parent for the node currently at pos
    def parent(self, pos):
        return pos // 2
    

    # function to return the position of the 
    # left child for the node currently at pos
    def leftChild(self, pos):
        return 2 * pos
    

    # function to return the position of the
    # right child for the node currently at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
    

    # function that returns true if the passed node
    # is a leaf node
    def isLeaf(self, pos):
        return pos * 2 > self.size


    # function to swap two node of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]


    # function to heapify the node at pos
    def minHeapify(self, pos):

        # if the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
                self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # swap with the left child and heapify the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                # swap with right child and heapify the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    
    # function to print the contents of the heap
    def print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                    str(self.Heap[2 * i])+" RIGHT CHILD : "+
                    str(self.Heap[2 * i + 1]))


    # function to build the min heap using the
    # minHeapify function
    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            print(pos)
            self.minHeapify(pos)


    # function to remove and return the minimum element
    # from the heap
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped


if __name__ == "__main__":

    print("The minHeap is")
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()

    minHeap.print()
    print("The Min val is " + str(minHeap.remove()))