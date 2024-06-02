def main():
    x = int(input("whats x? "))
    if is_even2(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def is_even2(n):
     if n % 2 == 0: return True 
     else: return False

def is_even3(n):
    return n % 2 == 0 


main()    