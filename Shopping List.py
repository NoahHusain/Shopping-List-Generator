# Generates shopping list that exports to file
def ShoppingListGenerator():
    shoppingList = []
    NeededItems  = input("\nPlease input items for your shopping list: ")  #outputs "Banana, apple, booze, Booze, BOOZE"     
    itemList = NeededItems.split (", ") #takes the output ^ and converts it into ["Banana", "apple","booze", "Booze", "BOOZE"]
    print("Your current shopping list is:") #prints to console the current string
    for i in range(len(itemList)): #counts how many strings were in the set and makes a list starting from 0 and counting to how many strings there are (0-4)
        itemList[i] = itemList[i].lower() #makes everything is the set lowercase

        # Make new list, add items to list using append, if item exists in list discard.
    grcy = [] 
    f = open("demofile2.txt", "w") #opens a txt document and discards the current text on it. if file under that name does not exist, creates it.
    f.write("Your current shopping list is:") #writes the sentence 
    
    for item in itemList: #creates new local variable item
        if item not in grcy: #plain english
            grcy.append(item) #if item does not exist in the list, add it to the end
            if itemList.count(item) > 1: #if the item appear in the list more than once, print the item name, number of times seen, and put () around the integer in console/file
                print("\n-" + item+ " (" + str(itemList.count(item))+ ")") #prints to console
                f.write("\n-" + item + " (" + str(itemList.count(item))+ ")") #prints to file
            else: #if the number of items is not more than 1 them just print the item with no attached integer
                print("\n-" + item) #prints to console
                f.write("\n-" + item) #prints to file
    
    f.close()# close the file          
    

    

ShoppingListGenerator()
