def find(a, b):
    if a%b==0:
        print(b)
        return
    return find(b, a%b)

find(64, 48)