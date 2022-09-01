items = [["rotten banana", 1],
         ["table",92],
         ["chair", 29],
         ["school bus", 100000],
         ["xbox x", 700],
         ["f92 lamborgini", 1000000],
         ["moon", 1],
         ["giant paper airplane", 10000],
         ["infected chicken", 1],
         ["large chainsaw", 92]
]

product = ["rotten banana",
           "table","chair",
           "school bus",
           "xbox x",
           "f92 lamborgini",
           "moon",
           "giant paper airplane",
           "infected chicken",
           "large chainsaw"]

product_cost = [1,92,29,100000,700,1000000,1,10000,1,92]

cart = []

for item in items:
  want_to_buy = input(f"would you like to buy a {item[0]} for ${item[1]}, yes or no? ")
  if want_to_buy == 'yes':
    cart.append(item)

print(f"here is your shopping cart:")

total_cost = 0
remove_item = "yes"

for item in cart:
  print(f"{item[0]} for ${item[1]}")
  total_cost += item[1]
print(f"Total cost: ${total_cost}")

while remove_item == 'yes':
  remove_item = input("would you like to get rid of anyhting, yes or no? ")

  if remove_item == 'yes':
    what_to_remove = input("which item  would you like to remove? ")
    cart.remove([what_to_remove,product_cost[product.index(what_to_remove)]])
  
    total_cost -= product_cost[product.index(what_to_remove)]
    print("here is you shopping cart:")
  
    for item in cart:
      print(f"{item[0]} for ${item[1]}")
    
    print(f"total cost: ${total_cost}") 
else: print("thank you for your order!")
 

  

