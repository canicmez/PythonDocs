name = input("Whats your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Gözde":
        print("Ravenclaw")
    case _: # diğer durumlarda yapılacaklar için _ konuluyo. ifteki else gibi
        print("Who?")
        