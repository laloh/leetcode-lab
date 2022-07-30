from heapq import heappop, heappush, heapify


# creating empty heap
heap = []
heapify(heap)

# adding items to the heap using heappush
# function by multiplying them with -1
heappush(heap, -1 * 10)
heappush(heap, -1 * 30)
heappush(heap, -1 * 20)
heappush(heap, -1 * 400)

# print the value of maximum element
print("Head value of heap: " + str(-1 * heap[0]))

# print the elements of the heap
print("The heap elements: ")
for i in heap:
    print((-1*i), end=" ")
print("\n")

element = heappop(heap)

# priting the elements of the heap
print("The heap elements: ")
for i in heap:
    print(-1 * i, end = ' ')