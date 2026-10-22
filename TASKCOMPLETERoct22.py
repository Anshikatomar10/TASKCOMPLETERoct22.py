#CHALLANGE:The task completer (task manager upgrade)
#GOAL:Modify the task manager to print task with a numbered task index.Allow the user to add a task by typing
#text,complete/remove a task by typing its number , or type "stop" to exit .
to_do = ["learn python","clean room "]#step 1 write the to do things as a list.
#step 2 setup a while loop to keep the programing repeating until the user enters 'exit' to stop the loop .
while True:
    print("="*40)
    #step 3 using for loop and enumerate add the numbers infront of each task 
    for index ,task in enumerate(to_do,start=1):
      print(f"{index}.{task}")
    print("="*40)
    # step 4 ask the user if they want to enter any new task in the list or give them the option to exit the loop.
    new_task = str(input("enter any new task you want to add to the list(or enter 'stop' to exit ) \n you can also tyoe'none' to proceed furter without adding any new task ")).lower().strip()
    if new_task == "stop":
         break#if the user choose to exit break the loop right there .
    elif new_task == "none":# as per the instructions if the user enters 'none' then proceed without adding anything new to the list .
         to_do = to_do
    else:# if the user do enter a task then append it to the existing list and print the updated version .
         to_do.append(new_task)
         print("="*40)
         print("your updated list is :",to_do)
         print("^"*40)
    # step 5 ask the user to enter the number of the task they have completed to remove that task from the to do list .     
    completed = int(input("Enter the number of task you have completed to remove that from the list :")) 
    python_index = completed - 1 #adjust the int with the with the python indexing to keep it correct and easy to use .
    to_do.pop(python_index) # remove the task listed on the entered number from the list using .pop
     # print the updated list to let the user know about the changes .
    print("your updated list is :",to_do) 
# step 6 print the final list as the final output .
print("="*40)
print("your final list is :", to_do)
print("="*40)    
    
