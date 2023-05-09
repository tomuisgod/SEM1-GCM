import turtle

slovo = ["s", "a", "m", "o", "t", "a"]
s_hadanie = ["", "", "", "", "", ""]
s_copy = slovo.copy()
pokus = 0


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
        else:
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
            if pokus == 1:
                t = turtle.Pen()
                t.speed(100000)
                t.left(90)
                for x in range(180):
                    t.forward(1)
                    t.right(1)
            if pokus == 2:
                t = turtle.Pen()
                t.speed(100000)
                t.penup()
                for x in range(180):
                    t.forward(1)
                    t.left(90)
                t.pendown()
                t.right(90)
                
                


if s_copy == s_hadanie:
    print("GG")
else:
    print(":(")
