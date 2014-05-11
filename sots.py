def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more
    
def heapSort(arr):
    for start in range((len(arr) - 2) // 2, -1, -1):
        siftdown(arr, start, len(arr) - 1)
        
    for end in range(len(arr) - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        siftdown(arr, 0, end - 1)
    return arr
 
def siftdown(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break
    
def bubbleSort(arr):
    changed = True
    while changed:
        changed = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
    return arr

def permuteArray(arr):
    import random
    
    random.shuffle(arr)
    return arr
 
def genArray(size):
    import random
    return [random.randint(1, 65536) for _ in range(size)]

def printArray(title, arr, timeTaken):
    print("{} took {:.10f} seconds".format(title, timeTaken))
    for n in range(0, len(arr), 10):
        print("\t".join(map(str, arr[n:n + 10])))
    print("*"*78)
    
def printTable(times):
    print("Sorting of 10,000 integers using the following algorithms:\n")
    print("{:<15} {:<25}".format("Algorithm", "Time (seconds)"))
    print("--"*15)
    for i in range(0, 3):
        print("{:<15} {:<25.10f}".format(times["Algorithm"][i], times["Time (seconds)"][i]))
    print("--"*15)
    
def testProg():
    from timeit import default_timer as timer
    
    start = timer()
    size = 100
    A = genArray(size)
    timeTaken = timer() - start
    printArray("Generating Original set", A, timeTaken)

    start = timer()
    A = quickSort(A)
    timeTaken = timer() - start
    printArray("Quick Sort", A, timeTaken)
    
    resetArr(A)
    
    start = timer()
    A = heapSort(A)
    timeTaken = timer() - start
    printArray("Heap Sort", A, timeTaken)
    
    resetArr(A)
    
    start = timer()
    A = bubbleSort(A)
    timeTaken = timer() - start
    printArray("Bubble Sort", A, timeTaken)
       
    print("END OF TEST")
    
def resetArr(arr):
    arr = permuteArray(arr)
    
def partTwo():
    from timeit import default_timer as timer
    times = {"Algorithm": ["quickSort", "heapSort", "bubbleSort"], "Time (seconds)": [0.0, 0.0, 0.0]}
    
    size = 10000
    A = genArray(size)

    start = timer()
    A = quickSort(A)
    timeTaken = timer() - start
    times["Time (seconds)"][0] = timeTaken
    
    resetArr(A)
    
    start = timer()
    A = heapSort(A)
    timeTaken = timer() - start
    times["Time (seconds)"][1] = timeTaken
    
    resetArr(A)
    
    start = timer()
    A = bubbleSort(A)
    timeTaken = timer() - start
    times["Time (seconds)"][2] = timeTaken
    
    printTable(times)
       
testProg()
partTwo()
