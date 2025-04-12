prices = [100,145,99,200,64,89,125,175]
discc_price = [price * 0.8 if price >100 else price for price in prices]
print(discc_price)