from replit import clear
import art
print(art.logo)
print("Welcome to the secret aution program.")

end_auction = False
bid_dictionary = {}

def add_bid(new_name, new_bid):
  bid_dictionary[new_name] = new_bid


def find_highest_bidder(bid_dictionary):
  highest_bid = 0
  winner = ""
  for bidder in bid_dictionary:
    bid_amount = bid_dictionary[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not end_auction:
  name = input("What is your name? ")
  bid = int(input("Whats your bid? $"))
  add_bid(new_name = name, new_bid = bid)
  end = input("Are there any other users who want to bid? Type yes or no. ").lower()
  clear()
  if end == 'no':
    end_auction = True

find_highest_bidder(bid_dictionary)




  
  
  
  


  