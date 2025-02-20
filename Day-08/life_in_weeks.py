# take current age as input and output the number of weeks left in life if lives till 90
def life_in_weeks(age):
    weeks = (90 - age)* 52
    print(f"You have {weeks} weeks left.")
    
    
life_in_weeks(38)