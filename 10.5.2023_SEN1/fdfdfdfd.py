p = [[1,2,3], [4,5,6], [7,8,9]]


def moznost_1():
    for i in p:
        for y in i:
            print(y)

def moznost_2():
    for i in range(len(p)):
        for y in range(len(p)):
            print(p[i][y])

def moznost_3():
    r = []
    for j in range(list(p)):
        print(j)

moznost_1()
print("#########################")
moznost_2()
print("#########################")
moznost_3()