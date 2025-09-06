
#---Imports---

from datetime import datetime

#----------------Database Equivalent- FOR TESTING--------------------------------

record_of_sale = []

snack_inventory = [
    {"id" : 101 , "name" : "Chips" , "price" : 20.00 , "is_available" : True},
    {"id" : 102 , "name" : "Samosa" , "price" : 25.00 , "is_available" : True},
    {"id" : 103 , "name" : "Yogurt" , "price" : 22.50 , "is_available" : True}
]


#--------------------------Main Menu-----------------------------------------------

def main_menu() :
    print("\nPlease choose from the following menu options : \n")
    print("1. Add Snack\n2. Remove Snack\n3. Update Avaliability\n4. Record Sale\n5. View Inventory\n6. View Sales\n7. Exit")
    choice = int(input("User Selection : "))
    if choice == 1:
        add_snack()
    elif choice == 2 :
        remove_snack()
    elif choice == 3 : 
        update_availability()
    elif choice == 4:
        record_sale()
    elif choice == 5 :
        print("🛒 INVENTORY:\n") 
        for each in snack_inventory :
            print(f"id:{each["id"]} | name:{each["name"]} | price:₹{each["price"]} | In_stock:{each["is_available"]}")
        main_menu()
    elif choice == 6:
        if record_of_sale == [] :
            print("No sales yet!\n")
            main_menu()
        else:
            print("📊 SALES HISTORY:\n")
            for each in record_of_sale :
                print(f"{each["sale_id"]}. name:{each["name"]} | price:{each["price"]} | date sold : {each["date_sold"]}")
            main_menu()
    elif choice == 7 :
        print("Goodbye!")
        return
    else : 
        return # using this like break, to exit this app

# -------------------User Updates to the Data -------------------------------------

#----To Check if Snack is in Inventory----
#---Will be used in add_snack & remove_snack---
def snack_in_inventory(specified_snack) :
    snack_in_inventory = False
    index = 0
    for each_snack in snack_inventory:
        if specified_snack == each_snack["id"]:
            snack_in_inventory = True
            break
        index += 1
    return snack_in_inventory , index

#----Kinda self explanatory----
def add_snack() :
    for snack in snack_inventory :
        print(f"id : {snack["id"]} | item : {snack["name"]}")
    id = int(input("Please enter the new item id : "))
    already_in_inventory, index = snack_in_inventory(id)
    if already_in_inventory == True :
        print("This entry is invalid : Already in Inventory")
        add_snack()
    else:
        name = input("Please enter the new item name : ")
        price = float(input("Please enter the new item price : "))
        is_available = True
        snack_inventory.append({"id":id,"name" : name,"price":price,"is_available" : is_available})
        print("\nHere is the updated inventory below! : \n")
        for each in snack_inventory :
            print(f"id:{each["id"]} | name:{each["name"]} | price:₹{each["price"]} | In_stock:{each["is_available"]}")
        main_menu()

        


# ----Again this is pretty self explanatory----
def remove_snack() :
    for snack in snack_inventory :
        print(f"id : {snack["id"]} | item : {snack["name"]}")
   
    snack_to_remove = int(input("Please enter the snack id you would like to remove : "))
    
    in_inventory , index = snack_in_inventory(snack_to_remove)
    
    if in_inventory == True : # this is checking if that return value boolean is true or not
        
        certainty = input(f"Enter YES if you are certain you would like to delete {snack_inventory[index]["name"]} : ")
        
        if certainty.upper() == "YES" :
            del snack_inventory[index] # this is using the referrenced index returned from the function
            print("Here is the updated inventory below : ")
            print("")
            for each in snack_inventory :
                print(f"id: {each["id"]} | name : {each["name"]}")
            main_menu()
        else : 
            "Let's go back to the list of snacks so you may choose which to remove : "
            remove_snack()
    else : 
        print("Snack not found, please try again.")
        remove_snack()

#--------Update that AvAiLaBiLiTy-------------
def update_availability() : 
    for each in snack_inventory :
        print(f"id:{each["id"]} | name:{each["name"]} | In_Stock:{each["is_available"]}")
    to_update = int(input("Enter the id of the item you would like to update : "))
    is_in_inventory, index = snack_in_inventory(to_update) 
    if is_in_inventory == False :
        print("Sorry, that selection does not exist!")
        main_menu()
    else:
        print(f"Current Availability of {snack_inventory[index]["name"]} | id: {snack_inventory[index]["id"]} is : {snack_inventory[index]["is_available"]}")
        print("Choose from below to update :\n1. Available\n2. Not Available")
        choice_to_update = int(input("User Choice : "))
        if choice_to_update == 1 :
            snack_inventory[index]["is_available"] = True
            print(f"{snack_inventory[index]["name"]} | id: {snack_inventory[index]["id"]} has been updated as In_Stock : {snack_inventory[index]["is_available"]}")
            main_menu()
        elif choice_to_update == 2 : 
            snack_inventory[index]["is_available"] = False
            print(f"{snack_inventory[index]["name"]} | id: {snack_inventory[index]["id"]} has been updated as In_Stock : {snack_inventory[index]["is_available"]}")
            main_menu()
        else : 
            print("Sorry, that was an invalid choice!")
            main_menu()


#--------------We sold an item!!!-------------------------------



def record_sale() :
    for each in snack_inventory :
        print(f"id : {each["id"]} | name : {each["name"]}")
    item_sold = int(input("What is the item id of the item sold? : "))
    in_inventory, tempIndex = snack_in_inventory(item_sold)
    if in_inventory == True :
        tempCounter = len(record_of_sale) +1
        snack_name,snack_price = snack_inventory[tempIndex]["name"],snack_inventory[tempIndex]["price"]
        date_sold = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Appending sale #{tempCounter}: name={snack_name}, price={snack_price}") # for temp debug
        record_of_sale.append({"sale_id":tempCounter,"name":snack_name,"price":snack_price,"date_sold":date_sold})
        print(f"Sale recorded for {snack_inventory[tempIndex]["id"]}|{snack_inventory[tempIndex]["name"]}!")
        main_menu()
    else :
        print("Sorry, that's an invalid entry!")
        main_menu()

main_menu()
