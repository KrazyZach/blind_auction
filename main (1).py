from replit import clear
from art import logo

print(f'{logo}\nWelcome to the secret auction program!')

def check_highest_bid():
    highest_bid =0
    list_number = 0
    for number in range(0,len(auction_dictionary)):
        if highest_bid < auction_dictionary[number]['bid']:
            highest_bid = auction_dictionary[number]['bid']
            list_number = number
    print(f"The winner is {auction_dictionary[list_number]['name']}, and they paid ${highest_bid: .2f}.")

auction_dictionary = []
more_people = False
while more_people == False:
    name = input("What is your name? ")
    bid = float(input("What is you bid? $"))
    num_of_people = input("Are there any other bidders? Type 'yes' or 'no'. ")
    auction_dictionary.append({'name':name, 'bid':bid})
    if num_of_people.lower() == 'no':
        more_people = True 
    clear()
    
check_highest_bid()