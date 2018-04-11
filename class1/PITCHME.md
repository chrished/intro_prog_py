## Introduction to Python


---

### Class 1
Today:
1. Variables, Math Operators, String
2. Lists
3. Dictionaries
4. if-elif-else
5. for/while loops

---
### Variables
Define a variable like this
```python
myvar = 3
```
The name of a variable has to start with a letter, no spaces allowed, no special symbols except underscore
```python
_myvar2 = 3
```
Now try to find a variable name, that is NOT allowed!
---

### Basic Datatypes
* Numbers: Integer and Floating-Point

```python
x = 3
type(x)
y = 3.5
type(y)
z = 3.0
type(z)
```

* Strings

```python
name = 'chris'
type(name)
numstr = '2.5'
type(numstr)
```

---

### Math Operators
You should give a and b a value and try out Python as a calculator

```python
# take a to the power of b
a**b
# modulus (remainder)
a%b
# Integer division (floored quotient)
a//b
# Division
a/b
# Multiplication
a*b
# Substraction
a-b
# Addition
a+b
```
Did you manage to produce an error somewhere?
---

---

### String Operators
The key operators for strings are concatenation and replication
```python
name = 'chris'
greeting = 'hello'
print(greeting + ' ' + name)
```
While "+" works on strings, "-" does not.
You can also replicate strings

```python
name = 'chris'
greeting = 'hello'
print(greeting + ' ' + name)
```

---
