## Introduction to Python

---

### Last Time
1. Variables, Math Operators, Strings
2. Lists/Dictionaries
3. Booleans
4. if-elif-else
5. for/while loops

---

### Class 2
Today:
1. functions
2. package import (example with numpy)
3. Projects!

---

### Functions/Methods
Define a function like this
```python
def myfun(arg1, arg2):
    print("I print out my arguments:")
    print(arg1, arg2)
    # return its second argument
    return arg2
```

---
### Functions/Methods - 2
There are many methods defined to operate only on certain types of objects, for example `list.append`
```python
x = [3, 4]
print("x has two elements: ", x)
x.append(5)
print("now x has three elements: ", x)

# we can also drop the last element
lastelement = x.pop()
print("now x has two elements again: ", x)
print("we dropped: ", lastelement)

```

---
### Functions/Methods - 3

We will focus on writing functions, but you will encounter the "obj.method()" syntax a lot!

* Methods operate on objects of a specific class (like `listobject.append()` )
* methods often change the object they operate on
* the key difference of a class specific method to a general function is that they take the class instance as the first argument for the function call

---
### Functions Exercise 1

1. Write a function that takes as input three numbers: Initial wealth *a*, interest rate *r* and number of periods *t*. Suppose end of period wealth is calculated as $$a_{t+1} = a_t(1+r)$$. Now your function is supposed to return   wealth t periods into the future! Suppose initial wealth is 1321€ and the interest rate is 5\%, what's your wealth 5 periods in the future?

---
### Functions Exercise 2
2. Write a function that takes a string and returns it stripped of all ";", "\_" and whitespaces " ".  (There is a python function  that basically does the job for you, if you want you can use it or write everything yourself). Then apply your function to: "Lady; Alice_McAllister  ".

---

### Working with packages

```python
import numpy as np

a = np.arange(10)
b = a.reshape(2,5)
b.ndim
b.dtype.name
b.size
type(b)
```
---

### Numpy example
Let's create 1D and 2D Array

```python
import numpy as np
a = np.array([1.5,2,3])
b = np.array([(1.5,2,3), (4,5,6)])

a.mean() # alternatively write np.mean(a)
b.mean()

# mean of each row
b.mean(1)
# mean of each column
b.mean(0)

# there are many more methods available in numpy
# try e.g. min(), max(), abs()
```
---

### Matplotlib example
```python
import numpy as np
import matplotlib.pyplot as plt
# see  https://matplotlib.org/1.2.1/examples/pylab_examples/

x = np.linspace(0.,2*np.pi,100)

plt.plot(x, np.sin(x))
plt.ylabel('sin(x)')
plt.title("A wave")
plt.show()
```

---
### Numpy OLS
see https://docs.scipy.org/doc/numpy/reference/index.html
```python
import numpy as np
# Fake dataset
x = np.random.randn(1000)
constant = np.ones(1000)
X = np.stack([constant, x], axis=1)
# X[0, 0] = 1
# X[0, 1] = some random number
# and so on for all rows
b = np.array([1., 5.])
y = np.dot(X,b) + np.random.randn(1000) * 0.5
```
---
### Numpy OLS - 2
see https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

```python
# (X'X)^-1 (X'y)
# writing out the formula
bhat = np.dot(np.linalg.inv(np.dot(X.transpose(), X)), np.dot(X.transpose(), y))
# using built-in numpy linear solver for lstsq problems (returns additional output)
bhat2, SSR, rank, s = np.linalg.lstsq(X,y)
```
Calculate the standard errors for bhat and do a simulation where you estimate bhat S times on a randomly drawn dataset each time. What does the distribution of bhat look like?

---
### Pandas +  Statsmodels
* Pandas gives you DataFrames like in R, see https://pandas.pydata.org/pandas-docs/stable/
* Statsmodels gives you a similar syntax for things like regressions, see http://www.statsmodels.org/stable/index.html
```python
import pandas as pd
import statsmodels.formula.api as sm
df = pd.DataFrame({"y": y, "x": x})
result = sm.ols(formula="y ~ x", data=df).fit()
print(result.summary())
```
