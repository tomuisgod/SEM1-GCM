def sd(a: int, b: int):
    while a != b:
        if a < b:
            a,b = b,a
        a = a - b
    return b

print(sd(173, 53))



