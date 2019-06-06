Y = "2"
Z = "3"
X = ""
while True:
    X = input(">    ").upper()
    if (X) == (Y):
        print ("Y")
    elif (X) == (Z):
        print ("Z")
    elif (X) == ("QUIT"):
        break
    else:
        print ("I didn't get that!")
    X = ""