# CMPS 2200 Assignment 2

**Name:**__Disha Amin_________________

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py` and `test_main.py`. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
  * O(n ^ log_3(2))
  * We can apply the master method the format T(n) = aT(n/b)+f(n). In this recurrence, a = 2, b = 3, and f(n) = 1. We can now plug this into W(n) = Theta(n^log b (a)), to get an upper bound of O(n ^ log base3 (2)).
.  
.  
.  
.  
  * $W(n)=5W(n/4)+n$
  * O(n ^ log_4 (5))
  * We can apply the master method in the format T(n) = aT(n/b)+f(n). In this recurrence, a = 5, b = 4, and f(n) = n. We can plug these variables into T(n) = Theta(n ^ log_b (a) log ^ k n), to get Theta(n^ log_4(5)), which makes the upper bound O(n ^ log_4 (5)).
.  
.  
.  
.  
  * $W(n)=7W(n/7)+n$
  * O(n)
  * We can apply the master method in the format T(n) = aT(n/b)+f(n). In this recurrence, a = 7, b = 7, and f(n) = n. We can plug these into T(n) = Theta(n^log_b a * log^k n), which gives us T(n) = Theta (n^log_7 (7)) = O(n).
.  
.  
.  
.  
.  
  * $W(n)=9W(n/3)+n^2$
  * O(n^2 * log_3(n))
  * We can apply the master method in the format T(n) = aT(n/b)+f(n). In this recurrence, a = 9, b = 3, and n = n^2. We can plug these into T(n) = Theta(n^log_b a * log^k n), which gives us T(n) = Theta (n^log_3 (9) * log_3(n)) = O(n^2 * log_3(n)).
.  
.  
.  
.  
.  
  * $W(n)=8W(n/2)+n^3$
  * O(n^3 * log_2(n))
  * We can apply the master method in the format T(n) = aT(n/b)+f(n). In this recurrence, a = 8, b = 2, f(n) = n^3. We can plug these into T(n) = Theta(n^log_b a * log^k n), which gives us T(n) = Theta (n^ log_2 (8) * log_2(n)) = O(n^3 * log_2(n)).
.  
.  
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
  * O(n^3/2 * logn)
  * We can apply the master method in the format T(n) = aT(n/b)+f(n). Here, a = 49, b = 25, and f(n) = n^3/2. We can plug this into T(n) = Theta(n^log_b a * log^k n), where k = 1. 
  
.  
.  
.  
.  
  * $W(n)=W(n-1)+2$
  * O(2n)
  * If we recursively go through this recurrence, we can see that each n value will equal 2 times itself (ex. W(2) = 4, W(4) = 8). So the aymptotic upper bound for this recurrence is O(2n).
  * 
.  
.  
.  
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
  * O(n^c)
.  
.  
.  
.  
.  
  * $W(n)=W(\sqrt{n})+1$
  * O(log_2(log_2(n)))
  * Solve by substitution


2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?
    A - O(n ^ (log base2 (5)))
    B - O(2^n)
    C - O(n^2)
    Given these runtimes, algorithm C is the most efficent runtime, so I would chose that one. 


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs in `test_main.py` to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


