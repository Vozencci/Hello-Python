def Binaire(n):
    b=str()
    while not(n//2==1):
        r=n%2
        b=str(r)+b
        n=n//2
    b='10'+b
    return b