#### Functions and Outputs
- A return statement is used to end the execution of the function call and it “returns” the value of the expression following the return keyword to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned. A return statement is overall used to invoke a function so that the passed statements can be executed

```python
def add(a, b):
    # returning sum of a and b
    return a + b
def is_true(a):
    # returning boolean of a
    return bool(a)
# calling function
res = add(2, 3)
print(res)
res = is_true(2<5)
print(res)

```