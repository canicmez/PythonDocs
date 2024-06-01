
def main():
    #Ask user for their name
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello, ", to)

main()
