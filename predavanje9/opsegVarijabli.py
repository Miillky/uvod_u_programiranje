a = 5

def funckija1():
    print("Unutar:", a)

funckija1()

def funckija2():
    a = 4
    print("Unutar:", a)

funckija2()

def funckija3():
    global a
    a = 4
    print("Unutar:", a)

funckija3()

def funckija4():
    a = 4
    print("Unutar 1:", a)
    def funkcija5():
        nonlocal a
        a = 6
        print("Unutar 2:", a)
    funkcija5()
    print("Unutar 1:", a)

funckija4()

print("Izvan:", a)