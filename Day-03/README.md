## If else
#### Description:
##### Condition check,
    Learn to use conditionals in python to check a conditions and tell the computer what to do in each case.
    
e.g. 

```python

if < this condition True >:
      < the execute this line of code>

elif < this condition True >:
        < execute this line of code>

else
      < execute this line of code >
```

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

e.g: 

    9 % 3 = 0, 8 % 3 = 2

It is very useful to find out the given number is EVEN, ODD, PRIME number.

## Logical Operators
- You can combine different conditions using logical operators.

- A ```and``` B #_Both conditions need to be ```True```_
- C ```or``` D #_Only one condition needs to be ```True```_
- ```not``` E #_THe condition must be ```False```_

## Project
- ```Title```:  __Treasure hunt__
- Refer the [flowchart](https://github.com/buchepalli-ramana-2/python-100days-bootcamp/blob/main/Day-03/TreasureIslandFlowchart.pdf) and write the code using logical operators and ask for the user input & return the results based on flowchart.
- Use your own [ASCII ART](https://ascii.co.uk/art#google_vignette) for your game