# Some of these comments are sorta lengthy, but they explain what 
# this does effectively. Read them before changing anything.

def clean_up_data(data_list, value):
    First_item_in_list_count = 0 #first list item, increments each time the first list item is found
    iterations = 0 #iterations of the while loop, making sure it doesnt scan data_list[10] when it only goes to 9
    Length_of_the_list = len(data_list)
    Length_of_list_as_string = str(len(data_list))
    #Is the list valid?
    if Length_of_the_list < 1:
        print("WARNING: Data list has less than one value. \nExiting...")
    else:
        #1. print the text label: “Before cleaning size: ” and the number of elements in the list before cleaning
        print("Before cleaning size: " + str(Length_of_the_list))
        
        #2. print the original list
        print(data_list)
        
        #3. using selection and iteration, remove the provided value from the list every time it is found
        while value in data_list: #While said value exists, remove it.
            data_list.remove(value) #Keeps looping till said value isn't detected
        
        #4. print the cleaned list
        print(data_list)
        
        #5. print the text label: “After cleaning: ” and the number of elements in the list after cleaning
        print("After cleaning the list: " + Length_of_list_as_string) 
        #"if" is call 1, rest of it is call 2
         #6. print the first element in the list and a count of the number of times the first list element occurs in the list overall (including the first time)
        while (iterations < len(data_list)): #While iterations arent bigger than how long the list is, 
            if data_list[0] == data_list[iterations]: #(SELECTION) check if first item is in "iterations," which increments each time the loop runs
                First_item_in_list_count +=1 #increments each time the first list item is found
            iterations +=1  #increment the iterations to ensure it doesnt search for list items higher than the # of items in the list
        print("First item in the list: " + str(data_list[0]) + "\nFirst item appears " + str(First_item_in_list_count) + " times") #call for first list item variable
        print("_____________________________________________________")

listname1 = [1, 4, 2, -4, 10, 0, 4, 2, 1, 4]
listname2 = ["Anita", "Arya", "Baz", "Evander", "Idris", "Kala", "Nia", "Smith", "Talia", "Zahara"]

clean_up_data(listname1, -4)
clean_up_data(listname2, "Smith")
