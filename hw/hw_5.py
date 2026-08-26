print("Holiday Planner")
print("A, Beach holiday")
print("B, Mountain holiday")

answer_1 = input("Pick a place to go (A or B): ")

if answer_1 == "A":
    print("C, Swimming")
    print("D, Make a sandcastle")
    answer_2 = input("Pick an activity (C or D): ")
    
    if answer_2 == "D":
        print("You picked a Beach Holiday")
        print("You picked to make a sandcastle")
        print("Remember to bring sunscreen and a hat.")
    elif answer_2 == "C":
        print("You picked a Beach Holiday")
        print("You picked to go swimming")
        print("Watch out for sharks!")
    else:
        print("error")

elif answer_1 == "B":
    print("E, Hiking")
    print("F, Camping")
    answer_2 = input("Pick an activity (E or F): ")
    
    if answer_2 == "E":
        print("You picked a Mountain Holiday")
        print("You picked hiking")
        print("Bring good gear.")
    elif answer_2 == "F":
        print("You picked a Mountain Holiday")
        print("You picked camping")
        print("Watch out for bears.")
    else:
        print("error.")
        
else:
    print("error")