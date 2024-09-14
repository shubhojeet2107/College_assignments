import timeit
import matplotlib.pyplot as plt

# Input Array elments
def Input(Array, n):
    # iterating till the range
    for i in range(0, n):
        ele = int(input("Arr : "))
        # adding the element
        Array.append(ele)

# Binary Searching
def binary_search(Array, key):
    while len(Array) > 0:
        mid = (len(Array))//2
        if Array[mid] == key:
            return True
        elif Array[mid] < key:
            Array = Array[mid + 1:]
        else:
            Array = Array[:mid]
    return False

# Main Block()
N = []
CPU = []
trail = int(input("Enter no. of trails : "))
for t in range(0, trail):
    Array = []
    print("-----> TRAIL NO : ", t + 1)
    n = int(input("Enter number of elements : "))
    Input(Array, n)
    print(Array)
    key = int(input("Enter key :"))
    start = timeit.default_timer()
    s = binary_search(Array, key)            
    print("Element Found = ", s)
    times = timeit.default_timer() - start
    N.append(n)
    CPU.append(round(float(times) * 1000000, 2))
print("N CPU")
for t in range(0, trail):
    print(N[t], CPU[t])

# Plotting Graph
plt.plot(N, CPU)
plt.scatter(N, CPU, color= "red", marker= "*", s=50)
# naming the x axis
plt.xlabel('Array Size - N')
# naming the y axis
plt.ylabel('CPU Processing Time')
# giving a title to graph
plt.title('Binary Search Time efficiency')
# function to show the plot
plt.show()