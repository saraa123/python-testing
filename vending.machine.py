from byotest import *

usd_coins = [100, 50, 25, 10, 5, 2, 1]
euro_coins = {100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}

def get_change(amount, coins=euro_coins):
    if amount == 0:
        return []
        
    if amount in coins:
        return[amount]
        
    change = [ ]
    for coin in coins:
        while coin <= amount:
            change.append(coin)
            amount -= coin
    
    return change 

test_are_equal(get_change(6), [3, 3])

print("passed")