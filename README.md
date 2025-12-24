Comparative Analysis of Iterative and Recursive Algorithms for Calculating the Sum of Digits
Overview

This repository presents a comparative analysis of iterative and recursive algorithms for calculating the sum of digits of a non-negative integer. The project focuses on evaluating both theoretical time complexity and empirical execution time, highlighting the difference between asymptotic analysis and practical performance.

This work was developed as part of the Analysis of Algorithm Complexity course.

Problem Description

Given a non-negative integer 
𝑛
n, the objective is to compute the sum of its decimal digits.
For example, if 
𝑛
=
527
n=527, the output is:

5 + 2 + 7 = 14


In this project, the input size is defined as the number of digits of the integer, since both algorithms process the input digit by digit.

Implemented Algorithms
Iterative Algorithm

The iterative algorithm computes the sum of digits using a loop that repeatedly extracts the last digit using the modulo operator and removes it using integer division. The process continues until the number becomes zero.

Time Complexity: O(n)

Space Complexity: Θ(1)

Recursive Algorithm

The recursive algorithm computes the sum of digits by breaking the problem into smaller subproblems. At each recursive call, the last digit is added to the result of a recursive call on the remaining digits.

Time Complexity: O(n)

Space Complexity: Θ(n) (due to recursion stack)

Experimental Methodology

Both algorithms were implemented in Python. Execution time was measured using the time.perf_counter() function. Random integers were generated with different numbers of digits, and execution time was recorded for each input size.

The tested input sizes were:

1, 5, 10, 50, 100, 300, 500, 900 digits


The results were visualized in a graph comparing input size versus running time.

Results and Analysis

The experimental results show that both algorithms exhibit linear growth in execution time as the number of digits increases, which confirms the theoretical analysis.

However, the recursive algorithm consistently requires more execution time than the iterative algorithm. This difference is caused by the overhead of recursive function calls, including stack frame creation and return operations. Although both algorithms belong to the same asymptotic complexity class, the iterative algorithm performs better in practice due to smaller constant factors.



References

A. Levitin, The Design and Analysis of Algorithms. Pearson Education, 2003.

R. Neapolitan and K. Naimipour, Foundations of Algorithms. D.C. Heath and Company, 1996.
