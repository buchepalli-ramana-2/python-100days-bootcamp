#### Functions with Inputs
- _Parameters_  : A parameter is the variable defined within the parentheses when we declare a function.
```Python
    # Here a,b are the parameters
    def sum(a,b):
    print(a+b)
    
    sum(1,2)

```
- _Arguments_ : An argument is a value that is passed to a function when it is called. It might be a variable, value or object passed to a function or method as input.
```python
    def sum(a,b):
        print(a+b)
  
    # Here the values 1,2 are arguments
    sum(1,2)

```
- There are two types of arguments:
   - Positional argument
   - keyword argument
- _Positional arguments_ : Positional Arguments are needed to be included in proper order i.e the first argument is always listed first when the function is called, second argument needs to be called second and so on.
```python
    def fun(s1,s2):
        print(s1+s2)
  
    fun("Geeks","forGeeks")
```
- _Keyword arguments_ : Keyword Arguments is an argument passed to a function or method which is preceded by a keyword and equal to sign (=). The order of keyword argument with respect to another keyword argument does not matter because the values are being explicitly assigned.
```python
    def fun(s1, s2):
        print(s1 + s2)

# Here we are explicitly assigning the values
    fun(s1="Geeks", s2="forGeeks")
```