# Tasks
For this topic, there is one big task. Ignore the folder `tests` which will be used to run a series of tests for the subroutine(s) you are asked to write.

## Maths Library
Our mini-project will be a library of mathematical utilities and functions. We will assume that you do not have access to any pre-written libraries so that you have to use all but the most basic mathematical operations yourself. 

We will use a mathematical technique called MacLaurin Series to produce good approximations for functions that cannot be computed exactly. Don't worry; you will never need to *understand* the maths I am asking you to program, you only need to be able to translate it into a program.

### Basics
We will need a few basics, which we shall collect in the file `maths/util.py`. 

The first function among these is the factorial function. It works on *integers*, i.e. whole numbers. If $n$ is a non-negative whole number, the factorial of $n$ is written as $n!$, and it is computed as $n! = 1 \times 2 \times ... \times (n-1) \times n$, unless $n$ is $0$; $0! = 1$ by definition. 

**In the file `maths/util.py`, write a function `factorial(n)` which returns the value $n!$.**

*The file `util.py` contains a value `NaN` which represents undefined values ("N.a.N." == "Not a Number"). `factorial` should return this value when given a negative number.*


### Exponents 1
Exponentiation is, in principle, simple. Writing $a^b$ is shorthand for multiplying $b$ copies of the number $a$ together. 

But what about the following expression? $$4^{2.325}$$

We can't have $2.325$ copies of the number $4$! It makes not one shred of sense! That is why we need to use MacLaurin series. We'll start with a very special number, $e$. $e$, Euler's constant, is approximately $2.718$ and is **the most important real number there is**. When $x$ is between -1 and 1, that is, when $-1 < x < 1$, we can use the following approximation:

$$e^x \approx \sum_{i=0}^{i=N} \frac{x^i}{i!}$$

When $x$ is not within that interval, we can either multiply or divide the value of $x$ by the value of $e$ until it is, as long as we keep track of how often we do this. This leads us to the following algorithm:

1. set a variable `p` = 1
2. if $\mathtt{x} \leq -1$:
    1. while $\mathtt{x} \leq -1$:
        1. divide `p` by $e$
        2. increment `x` by 1
3. else, if $\mathtt{x} \geq -1$:
    1. while $\mathtt{x} \geq -1$:
        1. multiply `p` with $e$
        2. decrease `x` by 1
4. if $x = 0$, return `p`
5. else: 
    1. compute the following expression:
       $$\epsilon = \sum_{i=0}^{i=N} \frac{\mathtt x^i}{i!}$$
    2. return $\mathtt p \times \epsilon$.

**In the file `maths/exponents.py`, write a function `exp(x)` which computes the function given by $\exp(x) = e^x$.**

### Logarithms

In case you have not met the so-called logarithm function yet, here is a very brief explanation/recap/introduction. It boils down to being the inverse of exponentiation. 

If $a, b, c$ are real numbers and $c$ is such that $a^b = c$, then *$b$ is the logarithm of $c$ with base $a$*. We write this as $b = \log_a(c)$. For instance, since $5^2 = 25$, we have $2 = \log_5(25)$. 

The most important logarithm function is the *natural logarithm* $\ln(x)$. It is the logarithm function with base $e$ (where $e \approx 2.718$ is Euler's constant from above). To recap, $\ln(x) = y$ implies that $e^y = x$. 

We can closely-approximately compute the logarithm of a *positive* real number $x$ using the following algorithm:

1. set a variable $l = 0$. 
2. if the number $x$ is greater than 1:
    1. while $x > 1$:
        1. divide the value of $x$ by $e$
        2. increment $l$ by 1.
3. if $x = 1$, return $l$. 
4. else: 
    1. compute the following expression:
       $$\Delta = \sum_{i=1}^{i=N} (-1)^{(i+1)} \frac{(x-1)^i}{i}$$
    2. return $l + \Delta$

Here, $N$ is some sufficiently large number, 20 should be enough. The file contains a variable (that you should absolutely not change) called `EULER` which gives you a sufficiently good value of $e$, Euler's constant.

**In the file `maths/logarithms.py` write a function `ln(x)` which implements the above algorithm.**

We should be able to use a more general logarithm function, though. That's OK, we can generalise the above function quite easily, using the below equivalence:
$$\log_a(b) = \frac{\ln(b)}{\ln(a)}$$

**In the file `maths/logarithms.py` write a function `log(x, base)` which computes the logarithm of `x` with base `base` using the above equivalence`**

### Exponents 2

We have written a function that exponentiates Euler's constant with any real number $x$ and we have written a function that computes the natural logarithm of any positive number $a$. We can use these together to write a function that exponentiates any *nonnegative* number $a$ with any real number $b$, by exploiting the equivalence

$$a^b = \left(e^{ln(a)}\right)^b = e^{\ln(a) \times b}$$

with the exception that $0^x$ is $0$ for all $x$ except when  $x = 0$. Remember that $a^0 = 1$ for any $a$.

**In `maths/exponents.py`, write a function `exponentiate(x, y)` that computes $x^y$ for any $x \geq 0$ and any $y$.**

We can also use this to write root functions such as the square root and $\sqrt[n]{x}$ for any $n$. Recall that 
$$\sqrt[n]{x} = x^{1/n}$$ 
so that root functions become easy to compute with what we have so far. 

**In `maths/exponents.py`, write functions `sqrt(x)` and `root(x, n)` that compute $\sqrt{x}$ and $\sqrt[n]{x}$, respectively.** 

*`root(x, n)` should only accept integers for its parameter `n`; printing `Use exponentiate to compute non-integer roots, n must be integer type!` if it is given floating-point values for `n` and not return anything. `root` should also be able to deal with negative values of `x` when `n` is odd. When `n` is even or `sqrt` is called, the functions should return `NaN` for negative `x`.* 

### Trigonometry

We want to be able to use trigonometric functions such as the sine, cosine and tangent. These can also eaily be computed with MacLaurin series. 

To start with, these functions are *periodic* with period $2\pi$, meaning that adding multiples of the constant $2\pi$ to the value $x$ does not change the value of $\sin(x)$ or $\cos(x)$ or $\tan(x)$. That means we can just focus on the interval $-\pi < x < \pi$ and modify all other inputs in order to be within it before computing an approximation of the respective functions.

To approximately compute the sine function, we can follow the algorithm below:
1. if $x < -\pi$:
    1. while $x < -\pi$:
        1. increase $x$ by $2\pi$
2. else if $x > \pi$:
    1. while $x > \pi$:
        1. reduce $x$ by $2\pi$
3. compute the value 
   $$\mathtt s = \sum_{i=0}^{i=N} (-1)^i \frac{x^{2\times i + 1}}{(2\times i + 1)!}$$
4. return the value `s`

To compute the cosine function, we can also merely exploit the equivalence $\cos(x) = \sin\left(x - \frac{\pi}{2}\right)$. Alternatively, you can follow the above algorithm for the sine curve and replace the mathematical expression for $s$ with the following:
$$c = \sum_{i=0}^{i=N} (-1)^i \frac{x^{2\times i}}{(2\times i)!}$$

The tangent function is defined as $\tan(x) = \frac{\sin(x)}{\cos(x)}$. However, the value of the tangent function is undefined whereever $\cos(x) = 0$. This needs to be signalled to the user by returning a NaN (not-a-number) value, which is given to you in `util.py`.

**In the file `maths/trigonometry.py`, write functions `sin(x)`, `cos(x)` and `tan(x)` that compute the sine, cosine and tangent functions respectively.**