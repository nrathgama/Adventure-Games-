while True: 

    answer = input("What do you like to play? (yes/no) ")

    #checks what would be the answer is. The strip() clears any white space allowing any variation of "yes" to be accepted

    if answer.lower().strip() == "yes":

        answer = input("You have reached a crossroads, would you like to go left or right?").lower().strip()
        if answer == "left":
            answer = input("You encounter a monster, would you like to run or attack?")
        
            if answer == "attack":
                print("That was not the greatest idea, you lost!")
            else:
                print("Good job! you made it away safely.")
            
                answer = input("You see a car and a plane. Which would you like to take? (car/plane)")
            
                if answer == "plane":
                    print("Unfortunately, you do not know how to fly.. Game Over!")
                else:
                    print("You won!")
                
        elif answer == "right":
            print("You walk aimlessly to the right and fall on a patch of ice. You injured your leg and now you cannot continue. Game Over!")
        else:
            print("Invalid choice, you lost!")
    else:
        print("That's too bad!")
        break
