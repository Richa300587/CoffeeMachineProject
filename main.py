def coinvalue():
    a = int(input("No of Penny coins"))
    b = int(input("No f Nickel coins"))
    c = int(input("No of Dime coins"))
    d = int(input("No of Quarter coins"))
    return (.01 * a + .05 * b + .01 * c + .25 * d)


def espresso(Max):
    if Max[0] >= 50 and Max[2] >= 18:
        t = coinvalue()
        while t > 0:
            if t >= 1.5:
                print(f"Left balance is {t - 1.5}")
                Max = [Max[0] - 50, Max[1] - 0, Max[2] - 18]
                return Max
            else:
                print("insufficient amount")
                t = coinvalue()
    elif Max[1] < 50:
        print("Short of Water Please add")
        q = input("do you want to refill press 'Y' for yess 'N' for no")
        if q == 'Y':
            Max = [300, 200, 100]
            return Max
        elif q == 'N':
            return Max
        else:
            print("wrong input")
            q = input("do you want to refill press 'Y' for yess 'N' for no")
    elif Max[2] < 18:
        print("Short of Coffee")
        q = input("do you want to refill press 'Y' for yess 'N' for no")
        if q == 'Y':
            Max = [300, 200, 100]
            return Max
        elif q == 'N':
            return Max
        else:
            print("wrong input")
            q = input("do you want to refill press 'Y' for yess 'N' for no")
            return Max


def latte(Max):
    if Max[0] >= 200 and Max[1] >= 150 and Max[2] >= 24:
        t = coinvalue()
        while t > 0:
            if t >= 2.5:
                print(f"Left balance is {t - 1.5}")
                Max = [Max[0] - 200, Max[1] - 150, Max[2] - 24]
                return Max
            else:
                print("insufficient amount")
                t = coinvalue()
    elif Max[0] < 200:
        print("Short of Water Please add")
        q = input("do you want to refill press 'Y' for yess 'N' for no")
        if q == 'Y':
            Max = [300, 200, 100]
            return Max
        elif q == 'N':
            return Max
        else:
            print("wrong input")
            q = input("do you want to refill press 'Y' for yess 'N' for no")
            return Max
    elif Max[1] < 150:
        print("Short of Milk Please add")
        q = input("do you want to refill press 'Y' for yess 'N' for no")
        if q == 'Y':
            Max = [300, 200, 100]
            return Max
        elif q == 'N':
            return Max
        else:
            print("wrong input")
            q = input("do you want to refill press 'Y' for yess 'N' for no")
            return Max
    elif Max[2] < 18:
        print("Short of Coffee Please add")
        q = input("do you want to refill press 'Y' for yess 'N' for no")
        if q == 'Y':
            Max = [300, 200, 100]
            return Max
        elif q == 'N':
            return Max
        else:
            print("wrong input")
            q = input("do you want to refill press 'Y' for yess 'N' for no")
            return Max


def cappuccino(Max):
    if Max[0] >= 200 and Max[1] >= 150 and Max[2] >= 24:
        t = coinvalue()
        while t > 0:
            if t >= 3.0:
                print(f"Left balance is {t - 1.5}")
                Max = [Max[0] - 200, Max[1] - 150, Max[2] - 24]
                return Max
            else:
                print("insufficient amount")
                t = coinvalue()
    elif Max[0] < 200:
        print("Short of Water Please add")
        q = input("do you want to refill press 'Y' for yess 'N' for no")
        if q == 'Y':
            Max = [300, 200, 100]
            return Max
        elif q == 'N':
            return Max
        else:
            print("wrong input")
            q = input("do you want to refill press 'Y' for yess 'N' for no")
            return Max
    elif Max[1] < 150:
        print("Short of Milk Please add")
        q = input("do you want to refill press 'Y' for yess 'N' for no")
        if q == 'Y':
            Max = [300, 200, 100]
            return Max
        elif q == 'N':
            return Max
        else:
            print("wrong input")
            q = input("do you want to refill press 'Y' for yess 'N' for no")
            return Max
    elif Max[2] < 18:
        print("Short of Coffee Please add")
        q = input("do you want to refill press 'Y' for yess 'N' for no")
        if q == 'Y':
            Max = [300, 200, 100]
            return Max
        elif q == 'N':
            return Max
        else:
            print("wrong input")
            q = input("do you want to refill press 'Y' for yess 'N' for no")
            return Max


def coffeemachine():
    global p
    p = [300, 200, 100]
    while (p[0] >= 50 and p[2] >= 18) or (p[0] >= 200 and p[1] >= 150 and p[2] >= 24):

        r = input("Do you want report press 'Y' for yes and 'N' for no")
        while type(r) == str:
            if r == 'Y':
                print(p)
                break
            elif r == 'N':
                break
            else:
                print("wrong input")
                r = input("Do you want report press 'Y' for yes")

        t = input(" press 'E' for espresso, press 'L' for latte , press 'C' fpr cappuccino ")

        if t == 'E':
            p = espresso(p)

        elif t == 'L':
            p = latte(p)

        elif t == 'C':
            p = cappuccino(p)

        else:
            print("Wrong input")

    print("Please refill can not make single coffee")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    coffeemachine()
