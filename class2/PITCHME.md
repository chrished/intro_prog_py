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
### Functions Exercise

1. Write a function that takes as input three numbers: Initial wealth *a*, interest rate *r* and number of periods *t*. Suppose end of period wealth is calculated as $$a_{t+1} = a_t(1+r)$$. Now your function is supposed to return   wealth t periods into the future!

2. Write a function that takes a string and returns it stripped of all ";", "_" and whitespaces " ".  (There is a python function that basically does the job for you, if you want you can use it or write everything yourself)

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
Ndimensional - Array
mean, sum, min, max

---
### Numpy OLS


---
### Pandas OLS
