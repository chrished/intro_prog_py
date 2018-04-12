## Introduction to Python

---

### Python

For some background see
* its [Wikipedia Page](https://en.wikipedia.org/wiki/Python_(programming_language))
* and its creator [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)


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

### String Operators
The key operators for strings are concatenation and replication
```python
name = 'chris'
greeting = 'hello'
print(greeting + ' ' + name)
```
While "+" works on strings, "-" does not.

You can also replicate strings by multiplying them with an integer

```python
name = 'chris'
greeting = 'hello'
print(greeting*2 + ' ' + name)
```

---
### Conversion Operators
* str()
* int()
* float()

```python
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

```python
countries = ['Spain', 'France']
capitals = ['Madrid', 'Paris']
```
We can access values of a list with square brackets, what does the following evaluate to?
```python
countries[1]
```

---
### Lists 2
We typically want to store many numbers and/or strings, for this we uses Lists and Dictionaries

```python
countries = ['Spain', 'France']
capitals = ['Madrid', 'Paris']
```
We can access values of a list with square brackets, what does the following evaluate to?
```python
>>> countries[1]
'France'
```
Lists have zero based indexing: the first element has index "0"
---

### Dictionaries
Suppose we want to store the capital of each country in a more structured manner we can use dictionaries. Instead of indexing by numbers, a dictionary is accessed by key values
```python
capitals = {'Spain':'Madrid', 'France':'Paris'}
capitals['Spain']
```
---


### Booleans
Booleans evaluate only to "True" or "False". We need those so that we can decide what to do in a program.

```python
mybool = True
otherbool = False
```

Comparison Operators
```python
x = 1.5
y = 2.
# equal to
x == y
# not equal to
x != y
# smaller than
x < y
# greater than
x > y
# smaller than
x <= y
# greater than
x >= y
```

---
### Booleans 2
Booleans evaluate only to "True" or "False". We need those so that we can decide what to do in a program.

Now consider logical "and" and "or"
```python
z = 3.
# the logical and/or 
x < y and x < z
x < y and x > z
x < y or x > z
```

---

### If-elif-else
Suppose we want to execute a part of a program only under some condition
```python
rain = True
sun = False
if rain:
    print("Oh no it rains!")
elif sun:
    print("Yeah sun")
else:
    print("At least it does not rain")
```
* "if condition:", the ":" tells python to find starting on the next line the relevant code that should be executed if "condition" is met.
* codeblock to be executed is indented by 4 spaces (and ends 4 spaces to the left)
* "elif" is only called if the first condition was "false"
*  "else" is only called if neither the first nor the second condition was "true"

---

### for loops
In cases where you want to do a certain task a number of times a loop is what you are looking for
```python

for i in range(5):
    print(i)

for name in ["anna", "bob"]:
    print(name)

res = 0
for k in range(1, 10):
    res += k
    print(res)
    if res == 6:
        break
```

---

### while loops
in case you want to repeat a task until a certain condition is met, a while loop comes in handy
```python
x = 0
while x < 5:
    x += 1
    print(x)

# this loop will never end. so maybe do not execute it without adding a termination clause
while True:
    x+=1
    print("We are going to infinity, currently at ", x)
```



---

### Exercises

Go to [Automate the Boring Stuff](https://automatetheboringstuff.com) and try the exercises in Chapter 1-5

we did not talk about functions yet, so feel free to skip them
