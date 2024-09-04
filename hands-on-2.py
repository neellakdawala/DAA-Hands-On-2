import timeit
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):   #Insertion sort
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap elements
            j -= 1
    return arr

def selection_sort(arr):   #Selection sort
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i, len(arr)):
           if arr[j] < arr[min_idx]:
               min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap elements    
    return arr

def bubble_sort(arr):    #Bubble sort               
    for i in range(len(arr) - 1, -1, -1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                did_swap = True
        if not did_swap:  # If no elements were swapped, the array is already sorted
            break      
    return arr

if __name__ == "__main__":
    input_sizes = list(map(int, input("Enter different input sizes separated by spaces: ").split()))

    insertion_times = []
    selection_times = []
    bubble_times = []
    
    for n in input_sizes:
        arr = [random.randint(0, 100) for _ in range(n)]
        
        # Time for insertion sort
        insertion_time = timeit.timeit(stmt="insertion_sort(arr.copy())", globals=globals(), number=1000)
        insertion_times.append(insertion_time)
        print(f"Insertion sort - Input size {n}: {insertion_time:.6f} seconds")

        # Time for selection sort
        selection_time = timeit.timeit(stmt="selection_sort(arr.copy())", globals=globals(), number=1000)
        selection_times.append(selection_time)
        print(f"Selection sort - Input size {n}: {selection_time:.6f} seconds")

        # Time for bubble sort
        bubble_time = timeit.timeit(stmt="bubble_sort(arr.copy())", globals=globals(), number=1000)
        bubble_times.append(bubble_time)
        print(f"Bubble sort - Input size {n}: {bubble_time:.6f} seconds")

    # Plot the results
    plt.plot(input_sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(input_sizes, selection_times, label='Selection Sort', marker='s')
    plt.plot(input_sizes, bubble_times, label='Bubble Sort', marker='^')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Sorting Algorithms')
    plt.legend()
    plt.show()
