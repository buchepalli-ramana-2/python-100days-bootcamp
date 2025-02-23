#### Dictionary

- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

__As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.__

Dictionaries are written with curly brackets, and have keys and values:
```Python
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

```

#### Nested loop syntax
```python

Outer_loop Expression:
    Inner_loop Expression:
        Statement inside inner_loop
    Statement inside Outer_loop
```
```python
# Running outer loop from 2 to 3
for i in range(2, 4):

    # Printing inside the outer loop
    # Running inner loop from 1 to 10
    for j in range(1, 11):

        # Printing inside the inner loop
        print(i, "*", j, "=", i*j)
    # Printing inside the outer loop
    print()

```
- __Note:__ To get the key of maximum of values in dictionary
```python
    fruits = {"orange": 12,"apple": 20,"watermelone": 10}
    max_value = max(fruits, key=fruits.get())
```