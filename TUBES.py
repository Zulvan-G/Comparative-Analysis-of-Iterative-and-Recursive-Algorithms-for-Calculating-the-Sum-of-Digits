import time                     # Used to measure execution time of algorithms
import random                   # Used to generate random test inputs
import matplotlib.pyplot as plt # Used to plot execution time graphs

def sum_of_digits_iterative(n):
    total = 0                   # Initialize variable to store sum of digits
    while n > 0:                # Loop runs once for each digit in n
        total += n % 10         # Extract last digit and add it to total
        n //= 10                # Remove last digit from n
    return total                # Return the final sum of digits

def sum_of_digits_recursive(n):
    if n == 0:                  # Base case: if no digits remain
        return 0                # Return 0 as sum
    return (n % 10) + sum_of_digits_recursive(n // 10)
                                # Recursive case:
                                # Add last digit to the result of recursive call
                                # on the remaining digits

def measure_time(func, n):
    start = time.perf_counter() # Record start time with high precision
    func(n)                     # Execute the given function with input n
    end = time.perf_counter()   # Record end time after execution
    return end - start          # Return execution time in seconds

input_sizes = [1, 5, 10, 50, 100, 300, 500, 900]
                                # List of input sizes representing
                                # the number of digits in the test numbers

iter_times = []                 # List to store execution times of iterative algorithm
rec_times = []                  # List to store execution times of recursive algorithm

for size in input_sizes:
    n = random.randint(10**(size-1), 10**size - 1)
                                # Generate a random integer with exactly
                                # 'size' number of digits
    iter_times.append(measure_time(sum_of_digits_iterative, n))
                                # Measure and store execution time of iterative version
    rec_times.append(measure_time(sum_of_digits_recursive, n))
                                # Measure and store execution time of recursive version

plt.plot(input_sizes, iter_times, marker='o', label='Iterative')
                                # Plot execution time of iterative algorithm
plt.plot(input_sizes, rec_times, marker='s', label='Recursive')
                                # Plot execution time of recursive algorithm
plt.xlabel("Number of Digits")  # Label x-axis as input size
plt.ylabel("Running Time (seconds)")
                                # Label y-axis as execution time
plt.title("Sum of Digits: Iterative vs Recursive")
                                # Set title of the graph
plt.legend()                    # Display legend to distinguish algorithms
plt.grid(True)                  # Add grid for better readability
plt.show()                      # Display the plotted graph
