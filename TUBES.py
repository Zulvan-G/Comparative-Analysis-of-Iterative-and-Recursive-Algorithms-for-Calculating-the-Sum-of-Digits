import time
import random
import matplotlib.pyplot as plt

def sum_of_digits_iterative(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def sum_of_digits_recursive(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits_recursive(n // 10)

def measure_time(func, n):
    start = time.perf_counter()
    func(n)
    end = time.perf_counter()
    return end - start

input_sizes = [1, 5, 10, 50, 100, 300, 500, 900]

iter_times = []
rec_times = []

for size in input_sizes:
    n = random.randint(10**(size-1), 10**size - 1)
    iter_times.append(measure_time(sum_of_digits_iterative, n))
    rec_times.append(measure_time(sum_of_digits_recursive, n))

plt.plot(input_sizes, iter_times, marker='o', label='Iterative')
plt.plot(input_sizes, rec_times, marker='s', label='Recursive')
plt.xlabel("Number of Digits")
plt.ylabel("Running Time (seconds)")
plt.title("Sum of Digits: Iterative vs Recursive")
plt.legend()
plt.grid(True)
plt.show()
