import random
try:
    dict = {"snake": 1 ,"water":2,"gun": 3 }


    reverse_dict = { 1:"s",2: "w",3: "g"}


    computer_choice = random.randint(1,3)

    

    your_choice = int(input("Enter your choice(snake = 1,water = 2,gun = 3): "))


    if(computer_choice == your_choice):
        print("It's a Draw")
    else:
        if(computer_choice == 1 and your_choice == 2):
            print("computer wins") 
        elif(computer_choice == 2 and your_choice == 1):
            print("you wins") 
            print(f"your choice {reverse_dict[your_choice]} and computer choice {computer_choice[reverse_dict]}")
        elif(computer_choice == 1 and your_choice == 3):
            print("you wins") 
            print(f"your choice {reverse_dict[your_choice]} and computer choice {computer_choice[reverse_dict]}")
        elif(computer_choice == 3 and your_choice == 1):
            print(f"your choice {reverse_dict[your_choice]} and computer choice {computer_choice[reverse_dict]}")
            print("computer wins") 
            print(f"your choice {reverse_dict[your_choice]} and computer choice {computer_choice[reverse_dict]}")
        elif(computer_choice == 2 and your_choice == 3):
            print("computer wins") 
            print(f"your choice {reverse_dict[your_choice]} and computer choice {computer_choice[reverse_dict]}")
        elif(computer_choice == 3 and reverse_dict == 2):
            print("you wins") 
            print(f"your choice {reverse_dict[your_choice]} and computer choice {computer_choice[reverse_dict]}")
        else:
            print("Something went wrong")

except ValueError:
    print("Invalid value,please enter input in integer and from 1,2 or 3")
