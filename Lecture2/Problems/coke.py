
price = 50
while True:
    print(f"Amount Due: {price}")
    n = int(input("Insert Coin: "))
    if n == 25 or n == 10 or n == 5:
        price = price - n
        if price <= 0:
            price = price * -1
            print(f"change owed: {price}")
            break
        else: continue


    else: continue