import random 

computer_val = random.choice(["sten", "sax", "påse"])
computer_valtvå = random.choice(["sten", "sax", "påse"])
computer_valtre = random.choice(["sten", "sax", "påse"])



namn = input("Vad heter du? ")
print("jag heter stensaxpåsemästaren, nu ska det spelas! ")

omgångar = int(input("Hur många omgångar vill du spela? "))


print(f"Vi ska spela {omgångar} omgångar, lycka till {namn}!")
val = input("Välj mellan sten, sax eller påse: ")
print(f"du valde {val}")

score = 0
if val == computer_val:
    print("Det blev oavgjort!")
elif val == "sten" and computer_val == "sax":
     score = score + 1
elif val == "sax" and computer_val == "påse":
     score = score + 1
elif val == "påse" and computer_val == "sten":
        score = score + 1
else:
    print(f"Du förlorade! Datorn valde {computer_val}")




    