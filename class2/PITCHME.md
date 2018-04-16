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
