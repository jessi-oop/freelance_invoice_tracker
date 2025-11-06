import csv
import os


def addCustomer():
    customerName = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phoneNum = int(input("Enter customer phone number: "))

    if not os.path.exists('CustomerRecords.csv'):
        with open('CustomerRecords.csv', 'w', newLine='') as file:
            fieldNames = ['Name', 'Email', 'PhoneNum']
            writer = csv.DictWriter(file, fieldnames=fieldNames)
            writer.writeheader()
        print("CSV file created with headers")

    with open('CustomerRecords.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Email', 'PhoneNum'])
        writer.writerow({'Name': customerName, 'Email': email, 'PhoneNum': phoneNum})

    print(f"Successfuly added: {customerName}")