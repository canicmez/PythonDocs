def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    


def is_valid(s):
   
    if s[0:2].isalpha() == False:
        return False
    elif len(s) < 2 or len(s) > 6:
        return False
    elif not check_0(s):
        return False

    else: return True
    
def check_0(n):
    i=0

    while i < len(n):
        if not n[i].isalpha():
            if n[i]=="0":
                return False
            else: return True
        i += 1

main()