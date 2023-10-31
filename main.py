import sys

bid_limit = 10
bid_attempts = 0
ubid = '0'
correct_answer = 'Y'

print("Lets list an item.\n")
name = input("What is the name of the item you are trying to list?:\n")
price = input(f"How much would you like to list {name} for?: ")
answer = input(f"You listed {name} for {price} would you like to bid(Y/N): ")

if answer == correct_answer:
  ubid = input("How much would you like to bid?: ")
  if ubid > price:
    print("You won the item!")
else:
  print("Have a good day.")
  sys.exit()

while bid_attempts < bid_limit and int(ubid) < int(price):
  bid_attempts += 1
  if bid_attempts >= bid_limit:
    print("You lost the item, goodbye.")
    break
  print(f"Minimum bid is {price} Would you like to bid?")
  answer = input()
  if answer == correct_answer:
    ubid = input("How much would you like to bid?: ")
  else:
    print("Have a good day.")
    break
  if int(ubid) > int(price):
    print("You won the item.")
    sys.exit()
