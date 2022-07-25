# to understand the flow and work of each line use "https://pythontutor.com/visualize.html#mode=edit" and get handy

from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bid = {}
biding_finished = False

def find_highest_bidder(bidding_record):
  highest_bidder = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bidder:
      highest_bidder = bid_amount
      winner = bidder
  print(f"The Winner is {winner} with biding amount ${highest_bidder}")
  
  

while not biding_finished:
  name = input("Enter your name: ")
  price = int(input("What is your bid?: $"))
  bid[name] = price
  should_continue = input("Are there any other bidders? Types 'yes' or 'no'.\n")
  if should_continue == 'no':
    biding_finished = True
    find_highest_bidder(bid)
  elif should_continue == 'yes':
    clear()


  
## her import from replit and art will not work as this is local thing need to work accordingly
