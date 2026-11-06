import random 




namn = input("Vad heter du? ")
print("jag heter stensaxpåsemästaren, nu ska det spelas! ")

omgångar = int(input("Hur många omgångar vill du spela? "))


print(f"Vi ska spela {omgångar} omgångar, lycka till {namn}!")

score = 0

for i in range(omgångar):

    computer_val = random.choice(["sten", "sax", "påse"])

    val = input("Välj mellan sten, sax eller påse: ")
    print(f"du valde {val}")
    print(f"omgång {i + 1} av {omgångar}")
    if val == computer_val:
        print("Det blev oavgjort!")
    elif val == "sten" and computer_val == "sax":
        score = score + 1 
        (print(f"Du vann! Datorn valde {computer_val}"))
    elif val == "sax" and computer_val == "påse":
        score = score + 1 
        print(f"Du vann! Datorn valde {computer_val}")
    elif val == "påse" and computer_val == "sten":
            score = score + 1
            print(f"Du vann! Datorn valde {computer_val}")
    else:
        print(f"Du förlorade! Datorn valde {computer_val}")

    print(f"Poäng: {score}")

