def prost(broj):
    if broj==1:
        return False
    for i in range(2,broj):
        if broj%i==0:
            return False
    return True

def prost_raspon(a, b):
    for i in range(a,b+1):
        if prost(i):
            print(i)

def prost_prebroji(a, b):
    ukupno = 0
    for i in range(a, b+1):
        if prost(i):
            ukupno+=1
    return ukupno

def prost_n(n):
    if 0 < n < 21:
        br, i = 0,1
        while True:
            i+=1
            if prost(i):
                br+=1
                if br==n:
                    return i
    else:
        return -1


def main(a, b):
    prost_raspon(a, b)
    prost_prebroji(a, b)
    prost_n(a)

if __name__ == "__main__":
    main()