# Secret Auction Program
import art

print(art.logo)

bid_dict ={}

continue_bidding=True
while continue_bidding:
    
# TODO-1: Ask the user for input
    name=input("What is your name?")
    bid=float(input("What is your bid? £"))
    
    name=name.title().strip()
# TODO-2: Save data into dictionary {name: price}
    bid_dict[name]=bid
    
# TODO-3: Whether if new bids need to be added
    more_bids=input("Are there any more bids? Type 'yes' or 'no'.")
    if more_bids=="no":
        continue_bidding=False

# TODO-4: Compare bids in dictionary
highest_bid=0
highest_bidder=""
for key in bid_dict:
    if float(bid_dict[key])>highest_bid:
        highest_bid=float(bid_dict[key])
        highest_bidder=key
print(f"The highest bidder is {highest_bidder} with a bid of £{highest_bid}")