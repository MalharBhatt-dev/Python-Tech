
stock_price = [5,1,7,8,9,6]

buy = 0
buy_index = 0
sell = 0
diff = 0

for i in stock_price:
    if i == 1:
        buy = i
        buy_index = stock_price.index(i)

    elif i == 6 and buy == 0:
        continue
    elif i == 6 and buy == 1:
        sell = i
        diff = stock_price.index(i) - buy_index

print(diff)


