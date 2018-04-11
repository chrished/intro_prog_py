## Introduction to Python


---

### Class 1
Today:
1. Variables, Math Operators, Strings
2. Lists/Dictionaries
3. Booleans
4. if-elif-else
5. for/while loops

---
### Variables
Define a variable like this
```python3
myvar = 3
```
The name of a variable has to start with a letter, no spaces allowed, no special symbols except underscore
```python3
_myvar2 = 3
```
Now try to find a variable name, that is NOT allowed!
---

### Basic Datatypes
* Numbers: Integer and Floating-Point

```python3
x = 3
type(x)
y = 3.5
type(y)
z = 3.0
type(z)
```

* Strings

```python3
name = 'chris'
type(name)
numstr = '2.5'
type(numstr)
```

---

### Math Operators
You should give a and b a value and try out Python as a calculator

```python3
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

### String Operators
The key operators for strings are concatenation and replication
```python3
name = 'chris'
greeting = 'hello'
print(greeting + ' ' + name)
```
While "+" works on strings, "-" does not.

You can also replicate strings by multiplying them with an integer

```python3
name = 'chris'
greeting = 'hello'
print(greeting*2 + ' ' + name)
```

---
### Conversion Operators
* str()
* int()
* float()

```python3
# convert a string to a number
numstr = '20'
int(numstr)
float(numstr)

# convert a string to a number
num = 20.5
str(num)

# covert an integer to float
float(20)

# covert a float to integer
int(20.8)
```
Make yourself familiar with the behavior of the conversion operators!
---

### Lists
We typically want to store many numbers and/or strings, for this we uses Lists and Dictionaries

```python3
countries = ['Spain', 'France']
capitals = ['Madrid', 'Paris']
```
We can access values of a list with square brackets, what does the following evaluate to?
```python3
countries[1]
```

---
### Lists 2
We typically want to store many numbers and/or strings, for this we uses Lists and Dictionaries

```python3
countries = ['Spain', 'France']
capitals = ['Madrid', 'Paris']
```
We can access values of a list with square brackets, what does the following evaluate to?
```python3
>>> countries[1]
'France'
```
Lists have zero based indexing: the first element has index "0"
---

### Dictionaries
Suppose we want to store the capital of each country in a more structured manner we can use dictionaries. Instead of indexing by numbers, a dictionary is accessed by key values
```python3
capitals = {'Spain':'Madrid', 'France':'Paris'}
capitals['Spain']
```
---


### Booleans
Booleans evaluate only to "True" or "False"

```python3
mybool = True
otherbool = False
```
---
