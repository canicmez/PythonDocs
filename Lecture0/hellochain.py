

#Ask user for their name
name = input("What's your name? ").strip().title()

# Split users name into first and last name
first, last = name.split()

#say hello to user
print(f"hello, {name}")  


#say hello to user
print(f"hello, {last}")     