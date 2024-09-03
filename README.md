# DAA-Hands-On-2

Que- Argue selection sort correctness

Ans- To prove we need to show three things abut a loop variant.

  -> Initialization
  -> Maintenance
  -> Termination

Initialization — At the first iteration, i = 0, so the subarray from the beginning up to index i is trivially sorted (an empty subarray), and there is no element in the sorted part. Hence, the loop invariant holds.

Maintenance - At the start of any arbitrary iteration, no element from 0 to i − 1 can ever be disturbed again. During the step, the inner for loop will find the smallest element in A[i + 1 . . . n − 1] and will swap it for the A[i] element. This element is swapped into the i th position. The new A[i] element cannot be smaller than any element in A[0 . . . i − 1] because the loop invariant is true prior to the start of the iteration, so it will simultaneously be the smallest element from i to the right and no smaller than any element to its left. Thus, the loop invariant is maintained throughout each iteration.

Termination - When the last iteration of the algorithm terminates, the loop counter will be on n − 2. If the i th element is smaller, it will be exchanged with the n − 1 st element. Given that the sublist to the left of i is already sorted and neither A[n − 2] nor A[n − 1] can be smaller than any item in A[0 . . . n − 2] because of the loop invariant, the combined list will be in sorted order. If the i th element is not smaller, the list is already sorted.

Que- Benchmark the runtime of each algorithm. Your benchmarks should include information about your computer (ram, cpu etc.) and be run with various input sizes; from small (array of size 5,10,20) all the way up to large arrays (where your computer is struggling). I should at the very least see a plot of time vs input size n. Feel free to use benchmarking software.

Computer Information: 

Silicon M3 Chip
16GB Ram
8-core CPU
10-core GPU

Enter different input sizes separated by spaces: 5 10 50 100 500 700 1000 5000
Insertion sort - Input size 5: 0.001438 seconds
Selection sort - Input size 5: 0.001684 seconds
Bubble sort - Input size 5: 0.001924 seconds
Insertion sort - Input size 10: 0.006113 seconds
Selection sort - Input size 10: 0.003894 seconds
Bubble sort - Input size 10: 0.004861 seconds
Insertion sort - Input size 50: 0.035957 seconds
Selection sort - Input size 50: 0.020179 seconds
Bubble sort - Input size 50: 0.035228 seconds
Insertion sort - Input size 100: 0.083118 seconds
Selection sort - Input size 100: 0.061186 seconds
Bubble sort - Input size 100: 0.148211 seconds
Insertion sort - Input size 500: 2.659554 seconds
Selection sort - Input size 500: 1.815511 seconds
Bubble sort - Input size 500: 3.722120 seconds
Insertion sort - Input size 700: 5.674610 seconds
Selection sort - Input size 700: 3.663761 seconds
Bubble sort - Input size 700: 7.791280 seconds
Insertion sort - Input size 1000: 12.404903 seconds
Selection sort - Input size 1000: 7.540265 seconds
Bubble sort - Input size 1000: 16.797383 seconds
Insertion sort - Input size 5000: 342.123140 seconds
Selection sort - Input size 5000: 186.129209 seconds
Bubble sort - Input size 5000: 460.696264 seconds
![Graph](https://github.com/user-attachments/assets/82b8a792-4d5b-4938-af9a-48798c0c37db)

