import csv
import os


def addCustomer():
    customerName = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phoneNum = input("Enter customer phone number: ")

    filePath = 'CustomerRecords.csv'
    fieldNames = ['ID','Name', 'Email', 'PhoneNum']

    nextID = 1
    if os.path.exists(filePath): #For assigning id to customers
        with open(filePath, 'r') as file:
            reader = csv.DictReader(file, delimiter='|')
            ids = [int(row['ID']) for row in reader if row['ID'].isdigit()] #Get the ID from the ID row in the list, check if digit, then casts it from string to int
            if ids: #Check if ids has values
                nextID = max(ids) + 1 #Increment the highest value in ids with 1

    customerID = f"{nextID:03d}"

    if not os.path.exists(filePath):
        with open(filePath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldNames, delimiter='|')
            writer.writeheader()
        print("File created with headers!")

    with open(filePath, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldNames, delimiter='|')
        writer.writerow({'ID': customerID, 'Name': customerName, 'Email': email, 'PhoneNum': phoneNum})

    print(f"Successfuly added: {customerName}")

def viewCustomerRecords():
    with open('CustomerRecords.csv', 'r') as file:
        for row in file:
            print(row.split())

def deleteCustomer():
    filePath = 'CustomerRecords.csv' #Create file path again for the rewriting later

    if not os.path.exists(filePath): #Check if the file exists or not
        print("File does not exist!")
        return
    
    targetID = input("Enter customer ID for deletion: ")

    rows = [] #Initialize a list that will be used to store the content of the file
    with open(filePath, 'r') as file:
        reader = csv.DictReader(file, delimiter='|') #Reads the file
        rows = list(reader) #Stores the content of the file in to the rows list

    originalCount = len(rows) #Will be used as reference if there is a row deleted from the content
    rows = [row for row in rows  #Iterates through each customer record in the list
            if row['ID'] != targetID] #Gets the user input and match if the target customer to delete match any of the rows. Keeps only the rows that does not match the target ID
    
    if len(rows) == originalCount: #Verifies if the rows equals to original count. If yes, meaning customer does not exist in the records
        print(f"Unable to delete. Customer {targetID} does not exist.")
        return
    
    with open(filePath, 'w', newline='') as file: #If there is a deleted row, rewrites the new file with the remaining content within the rows list
        fieldNames = ['ID','Name', 'Email', 'PhoneNum']
        writer = csv.DictWriter(file, fieldnames=fieldNames, delimiter='|')
        writer.writeheader()
        writer.writerows(rows)

    print(f"Customer with ID {targetID} is successfully deleted!")

def editCustomerDetails():
    filePath = 'CustomerRecords.csv'

    if not os.path.exists(filePath):
        print("File does not exist!")
        return

    rows = []
    with open(filePath, 'r') as file:
        reader = csv.DictReader(file, delimiter='|')
        rows = list(reader)

    originalCount = len(rows)

    print("---Current Records---")
    for content in rows:
        print(content.split())

    print("---Enter ")

    


while True:
    print("===Choose an action===")
    print("[1] Add customer")
    print("[2] View Customer Records")
    print("[3] Edit customer details")
    print("[4] Delete customer")
    print("[5] Exit")
    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            addCustomer()
        case 2:
            viewCustomerRecords()
        case 5:
            print("Actions done!")
            break