def highest_bidder(bid_dictionary):
  bid_winner = ''
  highest_bid = 0

  max(bid_dictionary)

  for bidder in bid_dictionary:
    bid_amount = bid_dictionary[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      bid_winner = bidder

  print(f'The winner is {bid_winner} with a bid of ${highest_bid}!')

bids = {}

continue_bid = True
while continue_bid:
  name = input("Enter you name: \n")
  pricing = input("Enter you price: \n")
  bids[name] = pricing
  other_bidders = input("If there are any more bidders, enter y, but if there isn't, enter n \n")
  if other_bidders == 'n'.lower():
    continue_bid = False
    highest_bidder(bids)
  elif other_bidders == 'y'.lower():
    print('\n' * 50)


