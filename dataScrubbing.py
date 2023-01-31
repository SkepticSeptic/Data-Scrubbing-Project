# Some of these comments are sorta lengthy, but they explain what 
# this does effectively. Read them before changing anything.

list_named = [1, 2, 1, 2, 3, 1, 4, 5, 6, 7, 2, 8, 2, 9, 10, 2] #first test list, checking if variables as lists work
def clean_up_data(data_list, value):
    fstlstitm = 0 #first list item, increments each time the first list item is found
    iterations = 0 #iterations of the while loop, making sure it doesnt scan data_list[10] when it only goes to 9
    
    #1. print the text label: “Before cleaning size: ” and the number of elements in the list before cleaning
    print("Before cleaning size: " + str(len(data_list)))
    
    #2. print the original list
    print(data_list)
    
    #3. using selection and iteration, remove the provided value from the list every time it is found
    while value in data_list: #While said value exists, remove it.
        data_list.remove(value) #Keeps looping till said value isn't detected
    
    #4. print the cleaned list
    print(data_list)
    
    #5. print the text label: “After cleaning: ” and the number of elements in the list after cleaning
    print("After cleaning: " + str(len(data_list))) 
    
     #6. print the first element in the list and a count of the number of times the first list element occurs in the list overall (including the first time)
    while (iterations < len(data_list)): #While iterations arent bigger than how long the list is, 
        if data_list[0] == data_list[iterations]: #check if first item is in "iterations," which increments each time the loop runs
            fstlstitm +=1 #increments each time the first list item is found
        iterations +=1  #increment the iterations to ensure it doesnt search for list items higher than the # of items in the list
    print("first item is " + str(data_list[0]) + ", appears " + str(fstlstitm) + " times") #call for first list item variable
