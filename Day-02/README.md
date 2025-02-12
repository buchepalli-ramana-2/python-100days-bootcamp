## Data types
- String: "Hello" , "345906"(Anything within quotes referred as string)
- Integer: 143(Whole number), 1234_123(large integer)
- Float: 3.14, 145_246_.56
- Booleans: True, False

## Type Errors
- These type of errors when we are using wrong datatypes

    For example, ```len(123)``` will give the ```Type Error``` because len() is function of string 
#### Type checking:

    Using ```type()``` function we will get the data type.

     For example, 
     
    
     ```type(123)``` will get output as  ```<class 'int'>```

     ```type("123")``` will get output as ```<class 'str'>```

     ```type(3.145)``` will get output as ```<class 'float'>```

     ```type(True)``` will get output as ```<class 'bool'>```
      
    
#### Type Conversion:

We can change the data type to another data type using functions like ```int()``` , ```float()```, ```str()```, ```bool()```

we will get ```ValueError``` if we give different datatype that cannot convert using the above functions.

## Mathematical operations

- Basic mathematical operators are ```+, -, *, /,// and ** ```
- Preference of operators is __PEMDAS__ (_Paranthesis_,_Expoenents_,_Division_,_Addition_,_Substraction_)
    
## Number manipulation
- While printing multiple datatypes without datatype we will use f- strings

```print(f"  ")```

e.g: ```print(f"your height is {height} and your name is {name}")``` here _height_ is integer and _name_ is string