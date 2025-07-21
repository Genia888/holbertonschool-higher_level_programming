# Python3: Mutable, Immutable… Everything is Object!

![Python image](https://raw.githubusercontent.com/Genia888/holbertonschool-higher_level_programming/main/python-everything_is_object/python.jpg)

## Introduction
In Python, every value is an object — from numbers to lists, even functions. Understanding what this means is key to avoiding unexpected bugs and writing clear code.

## ````id```` and ````type````
Every value in Python is an object. Each object has three essential properties:

- Type: What kind of object it is (e.g., ````int````, ````list````, ````str````)

- Value: The data stored inside (e.g., ````42````, ````[1, 2, 3]````)

- Identity: Its unique location in memory (at least in CPython).

You can examine an object’s type and identity using the built-in ````type()```` and ````id()```` functions:
````python
a = [1, 2, 3]
print(type(a))  # <class 'list'>
print(id(a))    # 140582645400512
````
The ````id```` function returns a unique integer (often the memory address in CPython) for the object during its lifetime. If two variables have the same ````id````, they reference the same object.

## Mutable objects
A mutable object is one whose contents can be changed after it is created. Classic examples in Python include lists, dictionaries, and sets:
````python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
````
With mutables, if you assign one variable to another, both names point to the same object:
````python
a = [1, 2, 3]
b = a
a.append(99)
print(b)  # [1, 2, 3, 99]
print(a is b)  # True
````
Be careful with this — changes via one alias affect all others referencing the object!

## Immutable Objects
An immutable object cannot be changed after it is created. Common examples are integers, floats, strings, and tuples:
````python
a = 5
b = a
a = 7
print(b)  # 5
print(a is b)  # False
````
If you “change” an immutable object (like adding 1 to an integer or concatenating a string), Python actually creates a new object and reassigns the variable name:
````python
text = "Hello"
print(id(text))
text += " World"
print(id(text))  # id has changed
`````

## Why Does It Matter?
Knowing the difference between mutable and immutable objects is crucial because Python handles assignment and function arguments by object reference. If you aren’t careful, you might change a variable “by accident” through an alias — a very common bug for new Python programmers.

For example, concatenating lists with ````+```` creates a new list (immutable-style behavior), while using ````append()```` or ````+=```` modifies the list in place (mutable behavior):
````python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]  # Creates a new list; l2 is unchanged
print(l2)  # [1, 2, 3]

l1 = [1, 2, 3]
l2 = l1
l1 += [4]  # Modifies in place; l2 also changes
print(l2)  # [1, 2, 3, 4]
````
## How Arguments Are Passed to Functions
When you pass a variable to a function, Python passes a reference to the object, not the actual variable name. This means that mutables can be changed inside functions, while immutables cannot:
````python
def add_one(n):
    n += 1

a = 5
add_one(a)
print(a)  # Still 5 (immutable, no effect)

def append_four(lst):
    lst.append(4)

mylist = [1, 2, 3]
append_four(mylist)
print(mylist)  # [1, 2, 3, 4] (mutable, changed in place)
````
If you want to avoid mutating objects inside functions, always pass a copy (e.g., ````list[:]````)

## Advanced Takeaways
Working on more advanced tasks, I discovered the importance of:

- Aliasing vs. Cloning: ````b = a```` makes an alias; ````b = a[:]```` makes a copy.

- Tuple single-element syntax: ````(1,)```` is a tuple; ````(1)```` is just an integer.

- Interning: Python sometimes reuses small objects for efficiency, like small integers or some strings — but not always with tuples or longer objects!

- ````id()```` and memory model: The identity (````id````) helps debug when objects are the same or not, especially with in-place and out-of-place operations.

## Conclusion
Knowing what’s mutable and what’s not explains most “weird” bugs in Python. Use ````id()```` to debug object identities and be careful with assignments and function arguments, especially with mutable types like lists and dictionaries.