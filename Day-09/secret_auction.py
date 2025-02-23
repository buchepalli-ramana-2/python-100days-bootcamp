import art
final_bid = {}
other_bidder_exists = True
bidder = ""

while other_bidder_exists:
    name = input("Enter name of bidder: ")
    value = int(input("Enter amount of bid value: $"))
    final_bid[name] = value
    is_there_other_bidder = input("Is there any other bidder? Type 'yes' or 'no' \n").lower()

    if is_there_other_bidder == 'no':
        other_bidder_exists = False        
        bid_values = []
        for key, value in final_bid.items():
            bid_values.append(value)
        if value == max(bid_values):
            bidder = key
        print(f"Bid winner is: {bidder}")


        