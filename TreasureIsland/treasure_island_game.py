from turtle import right
import my_module


print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

select1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if select1 == "left":
    select2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if select2 == "wait":
        select3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if select3 == "red":
            print("You entred into a room on fire and lost the treasure. Game over!")
        elif select3 == "yellow":
            print("You found the treasure. Congratulations! You won!! ")
            print('''
                888                                                          
                888                                                          
                888                                                          
                888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
                888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
                888   888    88888888.d888888"Y8888b.888  888888    88888888 
                Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
                "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 
            ''')
            print("And you get $",my_module.pi)
        elif select3 == "blue":
            print("You entered a room full of smoke and you can't see anything. Game over!")
        else: 
            print("Your selection is not available. Game over!")
    else:
        print("You just drown. Game over!")
else:
    print("You made the wrong choice and fell in a hole. Game over!")
