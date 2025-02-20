'''Love Calculator
💪 This is a difficult challenge! 💪 

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

2. Then check for the number of times the letters in the word LOVE occurs.   

3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times ,R occurs 1 time,U occurs 2 times,E occurs 2 times Total = 5 

L occurs 1 time O occurs 0 times V occurs 0 times E occurs 2 times Total = 3 
Love Score = 53

Example Input 

calculate_love_score("Kanye WesT", "Kim Kardashian")'''

def calculate_love_score(name1,name2):
    name = name1+name2
    true = "TRUE"
    love = "LOVE" 
    love_score1  = 0
    love_score2  = 0
    for i in name:
        if i in true.lower() or i in true:
            love_score1 += 1
            # print(i)
    

    for i in name:
        if i in love.lower() or i in love:
            love_score2 += 1
    
    print(str(love_score1)+str(love_score2))
    
 
    
#Call your function with hardcoded values
calculate_love_score("kanye West", "Kim kardashian")