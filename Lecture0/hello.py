

#Ask user for their name
name = input("What's your name? ")

#say hello to user
print("hello, ", end='\n')
print(name)

#say hello to user
print("hello, ", end="")
print(name)

#f-string
print(f"hello, {name}")

#removes trailing characters str.rstrip([chars])
name = name.strip()
print(f"hello, {name}")


#capitalize first letter
name = name.capitalize()
print(f"hello, {name}")

#capitalize all first letters
name = name.title()
print(f"hello, {name}")

#chain functions
name = name.strip().title()
print(f"hello, {name}")       