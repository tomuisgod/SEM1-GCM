import turtle

slovo = ["s", "a", "m", "o", "t", "a"]
s_hadanie = ["", "", "", "", "", ""]
s_copy = slovo.copy()
pokus = 0
t = turtle.Pen()


while pokus<10 and s_copy != s_hadanie:
    hadanie = input("Zadaj písmeno: ")

    if len(hadanie) > 1:
        if hadanie == "ch" or hadanie == "ia" or hadanie == "ie" or hadanie == "iu  ":
            while pokus<10 and s_copy != s_hadanie:
                hadanie = input("Zadaj písmeno: ")
                if hadanie in slovo:
                    print("ok")
                    while hadanie in slovo:
                        i = slovo.index(hadanie)
                        s_hadanie[i] = hadanie
                        slovo[i] = "."
                    print(s_hadanie)
                else:
                    pokus += 1
                    print("Nesprávne, tvoj pokus:", pokus)
        elif hadanie is int or len(hadanie) > 1:
            print("ERROR: Nezadal si písmeno")
            hadanie = ("Zadaj písmeno: ")

    else:
        if hadanie in slovo:
            print("ok")
            while hadanie in slovo:
                i = slovo.index(hadanie)
                s_hadanie[i] = hadanie
                slovo[i] = "."
            print(s_hadanie)
        else:
            pokus += 1
            print("Nesprávne, tvoj pokus:", pokus)
            
            # polkruh
            if pokus == 1:
                t.speed(100000)
                t.left(90)
                for x in range(180):
                    t.forward(1)
                    t.right(1)
            
            #ciara hore
            if pokus == 2:
                t = turtle.Pen()
                t.speed(100000)
                t.penup()
                t.right(180)
                for y in range(180):
                    t.forward(1)
                    t.left(1)
                t.pendown()
                t.forward(200)
            
            #ciara doprava
            if pokus == 3:
                t.right(90)
                t.forward(200)
            
            #ciara dole
            if pokus == 4:
                t.right(90)
                t.forward(100)
            
            #hlava
            if pokus == 5:
                for x in range(360):
                    t.forward(1)
                    t.right(1)

            #telo
            if pokus == 6:
                for x in range(180):
                    t.forward(1)
                    t.right(1)
                t.forward(50)
            
            #prava ruka
            if pokus == 7:
                t.right(180)
                t.forward(30)
                t.right(45)
                t.forward(30)

            #lava ruka
            if pokus == 7:
                t.left(90)
                t.forward(30)
                t.right(45)
                t.left(90) 
                t.forward(30)
            
            #prava noha
            if pokus == 8:
                t.left(180)
                t.forward(30)
                t.right(150)
                t.forward(25)
                t.right(45)
                t.forward(30)

            if pokus == 9:
                t.right(180)
                t.forward(30)
                t.left(135)
                t.forward(30)               




                
                


if s_copy == s_hadanie:
    print("GG")
else:
    print(":(")
