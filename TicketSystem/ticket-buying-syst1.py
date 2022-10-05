# # Welcome message
height = int(input("What is your height in ft? "))

if height > 5:
    print("You can ride the rollercoster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. Have free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_pic = input("Do you want a photo? Y or N. ")
    if wants_pic == "Y":
        # Add $3 to the bill
        bill += 3
    print(f"Your final bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you ride.")
