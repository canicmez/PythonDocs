expression = input("Expression: ")

x, y, z =expression.split(" ")
match y:
    case "+":
        print(round(float(int(x)+int(z)), 1))
    case "-":
        print(round(float(int(x)-int(z)), 1))
    case "/":
        print(round(float(int(x)/int(z)), 1))
    case "*":
        print(round(float(int(x)*int(z)), 1))