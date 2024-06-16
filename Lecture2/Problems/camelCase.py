def main():
    name = str(input("camelCase: "))
    snake(name)

def snake(n):
    i=0
    print("snake_case: ", end="")
    while i<len(n):
        if n[i].islower():
            print(n[i], end="")
        else:
            print(f"_{n[i].lower()}", end="")
        i= i+1

main()



