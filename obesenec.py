slovo = ["s", "a", "m", "o", "t", "a"]
s_hadanie = ["", "", "", "", "", ""]
s_copy = slovo.copy()
pokus = 0


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

if s_copy == s_hadanie:
    print("GG")
else:
    print(":(")
