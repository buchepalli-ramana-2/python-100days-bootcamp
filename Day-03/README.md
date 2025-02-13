## If else
#### Description:
##### Condition check,
    Learn to use conditionals in python to check a conditions and tell the computer what to do in each case.
    
e.g.:

```if``` < this condition is true >:
      < the execute this line of code>
```elif``` < this condition is true >:
        < execute this line of code>
```else```
      < execute this line of code >

## Nested conditionals
- we can add ```if/else``` in another ```if/else``` statments

e.g:

```python
if math_score >=90:
  if english_score >= 90:
    print("You're good at everything")
  else:
    print("You're good at maths")
if english_score >=90:
   print("You're good at english")

```

## Modulo Operator (%)
- Modulo operator(%) between two numbers gives us the reminder.

e.g: 9 % 3 = 0, 8 % 3 = 2

It is very useful to find out the given number is EVEN,ODD,PRIME number.

## Logical Operators
- You can combine different conditions using logical operators.

- A ```and``` B #_Both conditions need to be ```True```_
- C ```or``` D #_Only one condition needs to be ```True```_
- ```not``` E #_THe condition must be ```False```_