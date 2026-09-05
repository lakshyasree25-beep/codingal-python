#Step 1: Set total_chores to 4, store it as original_count, and print how many chores are on today's list.
total_chores = 4
original_count = total_chores
print("total number of chores to be done", total_chores)
#Step 2: Set up a completed_count counter starting at 0 and a chore_num counter starting at 1.
completed_count=0
chore_num=1
#Step 3: Start a while loop that keeps running as long as chore_num is less than or equal to total_chores.
while chore_num <= total_chores:
#Step 4: Inside the loop, work out the current chore's name from chore_num, then ask if it has been finished.
    if chore_num==1:
        print("clearing the table is your chore.")
        answer=input("have you cleared the table?")       
#Step 5: If the answer is yes, increase completed_count and chore_num by 1; otherwise, print a message and let the loop ask about the same chore again.
        if answer=="yes":
            completed_count+=1
            chore_num+=1
        else:
            print("clearing the table is your chore.")
    if chore_num==2:
            print("wasing the dishes is you chore")
            answer=input("have you cleaned the dishes?")       
    #Step 5: If the answer is yes, increase completed_count and chore_num by 1; otherwise, print a message and let the loop ask about the same chore again.
            if answer=="yes":
                completed_count+=1
                chore_num+=1
            else:
                print("wasing the dishes is you chore?")
    if chore_num==3:
                print("mowing the lawn is your chore")
                answer=input("have you mowed the lawn")       
        #Step 5: If the answer is yes, increase completed_count and chore_num by 1; otherwise, print a message and let the loop ask about the same chore again.
                if answer=="yes":
                    completed_count+=1
                    chore_num+=1
                else:
                    print("mowing the lawn is your chore")
    if chore_num==4:
                print("mopping the floor is your chore")
                answer=input("have you mopping the floor")       
        #Step 5: If the answer is yes, increase completed_count and chore_num by 1; otherwise, print a message and let the loop ask about the same chore again.
                if answer=="yes":
                    completed_count+=1
                    chore_num+=1
                else:
                    print("mopping the floor is your chore")    
#Step 6: Once the while loop ends, print the completion message, then safely demonstrate an infinite loop's condition, using a break to stop it after 3 rounds.
print("=========good job you commpleted all the chores!!!!!!!!!======")
happy=5
while happy<=8:
    print ("=========good job you commpleted all the chores!!!!!!!!!======") 
    happy+=1
    if happy==7:
        break
#Step 7: Print the final chore checklist summary showing chores assigned, completed, and remaining.
print ("""clearing the table is done.
wasing the dishes is done.
mowing the lawn is done.
mopping the floor is done""",end=".") 