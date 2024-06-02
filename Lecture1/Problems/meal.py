def main():
    x = input("What time is it? ")
    if 7 <= convert(x) <= 8:
        print("breakfast time")
    elif 12 <= convert(x) <= 13:
        print("lunch time")
    elif 18 <= convert(x) <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    return int(h)+round(int(m)/60, 1)

main()