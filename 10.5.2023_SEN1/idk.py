def blbost(a: int, b: int):
    while a != b:
        if a < b:
            a,b = b,a
        a = a - b
    return b

print(blbost(173, 53))



