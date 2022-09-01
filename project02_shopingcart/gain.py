what_to_remove = "harp"
cart = [["sharp", 390],["harp", 8493]]

for item in cart: 
    if item.index(what_to_remove) == 0:
      cart.remove(item)
    else: print("prcess")