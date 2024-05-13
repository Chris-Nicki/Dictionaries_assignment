# Assignments | Dictionaries

#1. Real-World Python Dictionary Applications
"""Objective:
The aim of this assignment is to reinforce your understanding and
application of Python dictionaries, nested collections, and dictionary
methods in real-world scenarios. You will apply these concepts to solve
practical problems, demonstrating your ability to manipulate and manage 
complex data structures.
"""
#  Task 1: Restaurant Menu Update
"""You are given an initial structure of a restaurant menu stored in a 
nested dictionary. Your task is to update this menu based on given 
instructions. This exercise tests your ability to manipulate nested 
dictionaries and manage data effectively.
"""
# Problem Statement:
# # Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
print(restaurant_menu)
print()

# Add a new category called "Beverages" with at least two items.
print("Beverages Added")
restaurant_menu["Beverages"] = {"Coke": 2.50, "Dr. Pepper": 2.50, "Sprite": 2.50}
print(restaurant_menu["Beverages"])
print(restaurant_menu)
print()
# Update the price of "Steak" to 17.99.
print("Steak price change")
restaurant_menu["Main Course"]["Steak"] = 17.99
new_price = restaurant_menu["Main Course"]["Steak"] = 17.99
item = "Steak"
print(f"Price of {item} changed to {new_price}")
print()
# Remove "Bruschetta" from "Starters"
print("Bruschetta Removed")
removed_item = restaurant_menu["Starters"].pop("Bruschetta") 
print(restaurant_menu)


# 2. Python Programming Challenges for Customer Service Data Handling
"""Objective: This assignment is designed to test and enhance your Python programming skills, 
focusing on real-world applications in customer service data management. You will practice correcting
code, organizing customer data, and implementing a feedback system using Python dictionaries.
"""
# Task 1: Customer Service Ticket Tracker
"""Demonstrate your ability to use nested collections and loops by creating a system to track customer 
service tickets.

Problem Statement: Develop a program that:
- Tracks customer service tickets, each with a unique ID, customer name, issue description, and status 
(open/closed).
Implement functions to:
    - Open a new service ticket.
    - Update the status of an existing ticket.
    - Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
"""
"""Example ticket structure:
    service_tickets = {
        "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
        "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
# """
Ticket_Database = {}
Ticket_Database["open_tickets"] = {}
Ticket_Database["closed_tickets"] = {}
def create_new_ticket():
    print("Lets get your service ticket started, we will just need a little information.")
    import random
    ticket_number =  random.randint(1000,2000)
    ticket_number = str(ticket_number)
    if ticket_number not in Ticket_Database: 
        Ticket_Database[ticket_number]= {}
    else:
        print("Number in use, please get a new one.")

    print("We will need your name.")
    first_name = input("What is your first name")
    last_name = input("What is your last name? ")
    print("What is the reason for service? ")
    model = input("What model is the duck? ")
    problem = input("What is wrong with it? ")
    print("What is the status of the ticket")
    open = input("Would you like to mark the ticket open or closed? ")
    while True:
        if open == "open" or open == "closed":
            if open == "open":
                Ticket_Database["open_tickets"][ticket_number] = {"Customer": [first_name, last_name], "Issue": [model, problem], "Status": [open]} 
            else:
                Ticket_Database["closed_tickets"][ticket_number] = {"Customer": [first_name, last_name], "Issue": [model, problem], "Status": [open]}  
            break  
        else:
            open = input("Would you like to mark the ticket open or closed? ")
    Ticket_Database[ticket_number] = {"Customer": [first_name, last_name], "Issue": [model, problem], "Status": [open]} 
def locate_a_ticket():
    print("Lets find that service ticket!")
    while True:
        ticket_number = input("What is your ticket number? ") 
        if ticket_number in Ticket_Database:
            print(Ticket_Database[ticket_number])
            return ticket_number
        else:
            print("Please enter a valid ticket number")
        break
def update_ticket():
    while True:   
        ticket_number =locate_a_ticket() 
        print(ticket_number)    
        update = input("""What would you like to do to the ticket?
1. Change name
2. Update issue
3. Change status
4. Delete ticket
""")
        if update == "1":
            print("Please update your name")
            update_first_name = input("What is your first name")
            update_last_name = input("What is your last name? ")
            Ticket_Database["open_tickets"][ticket_number]["Customer"] = [update_first_name, update_last_name]  
                    # only works if the ticket is open, closed is not recognized
        elif update == "2":
            print("Please update the service needs. ")
            n_model = input("What is the model number? ")
            n_issue = input("What is the issue?")
            Ticket_Database["open_tickets"][ticket_number]["Issue"]= [n_model, n_issue]
            break
        elif update == "3":
            print("Please update the status of the ticket")
            open = input("Would you like to mark the ticket open or closed? ")
            while True:
                if open == "open" or open == "closed":
                    if open == "open":
                        Ticket_Database["open_tickets"][ticket_number] = {"Status": [open]} 
                    else:
                        Ticket_Database["closed_tickets"][ticket_number] = {"Status": [open]}  
                    break
                else:
                    open = input("Would you like to mark the ticket open or closed? ")  
            break
        # works but does not pop out of the old dictionary if moved to the new?
        elif update == "4":
            deleted_ticket = input("What ticket number would you like to delete? ")
            if deleted_ticket in Ticket_Database:
                deleted = Ticket_Database.pop,Ticket_Database["Open Tickets"].pop, Ticket_Database["closed_tickets"].pop(deleted_ticket)
                print(f"{deleted} with {deleted_ticket} ticket has been deleted from database.")
                break
            else:
                print("Please enter a valid entry.")
        # works, but doesnt delete the ticket from every dictionary, can we do a mass wipe?

def view_tickets():
    while True:
        view = input("""What tickets would you like to view?
1. Open Tickets
2. Closed Tickets
3. All Tickets
4. Return to Menu             
""")
        if view == "1":
            print(Ticket_Database["open_tickets"])
        elif view == "2":
            print(Ticket_Database["closed_tickets"])
        elif view == "3":
            print(Ticket_Database)
        elif view == "4":
            break
        else:
            print("Please enter a valid response.")
               
def service_ticket_app():
    print()
    print("Welcome to Fred's Rubber Duck Repair Shop Service Ticket Application")
    print("Remember, their is no I in team, but their is in WIN, so fix those ducks!")
    print()
    while True:
        option = input("""What do you need to do?
1. Open a new service ticket
2. Locate a ticket
3. Update a current ticket
4. View tickets  
5. Quit              
""")
        if option =="1":
            create_new_ticket()
            print(Ticket_Database)
        elif option == "2":
            locate_a_ticket()
            print(Ticket_Database)
        elif option == "3":
            update_ticket()
            print(Ticket_Database)
        elif option == "4":
            view_tickets()
            print(Ticket_Database)
        elif option == "5":
            print("Thank you for using the Rubber Ducker Service Ticket Repair App! Have a great day")
            break
        else:
            print("Please enter a valid entry or the ducks will sink!")
service_ticket_app()
