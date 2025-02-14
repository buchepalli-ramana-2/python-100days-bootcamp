'''
Title: Treasure hunt
Description:
    Follow the flowchart to create your adventrues game using things you learnt today.

    use the ASCII(https://ascii.co.uk/art#google_vignette) art

'''

print(f'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 
''')
print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')

direction = input("Enter the direction you want go? ")

if direction == "Left":
    
    action = input("Do you want to swim or wait? ")
    if action == "Wait":
        doors = input('''You're infront of three doors. 
               select one door\n''')
        
        if doors == "Red":
            print('''Burn by fire.Game Over!!!''')
                  
        elif doors == "Blue":
            print("Eaten by beasts.Game Over!!!")
            
        elif doors == "Yellow":
            print("You Win!!")
            
        else:
            print("Game Over!")        
    else:
            print('''Attacked by trout
          Game Over!!!''')
else:
    print('''Fall into a whole.Game Over.!!''')


