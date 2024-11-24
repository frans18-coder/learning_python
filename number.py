number = 23
guess = int(input("enter an integer (between) = "))

if guess == number:
    print("Congratulations!, yous guessed it.\nbut you do not win any prizes!")
    
elif guess < number:
    print("No, it is a little higher than that.")
    
else:
    print("No, it is a little lower than that.")