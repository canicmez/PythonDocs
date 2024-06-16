def main():
    name = str(input("input: "))
    twit(name)

def twit(n):
    i=0
    print("output: ", end="")
    while i<len(n):
        if n[i].lower() == "a" or n[i].lower() == "e" or n[i].lower() == "i" or n[i].lower() == "o" or n[i].lower() == "u":
            print("", end="")
        else:
            print(n[i], end="")
            
        i= i+1

main()
