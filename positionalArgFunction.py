def intr(amt,rate, /):
    val = amt*rate/100
    return val
print(intr(2,3))
#print(intr(amt=2,rate=3)) # intr() got some positional-only arguments passed as keyword arguments: 'amt, rate'
def intr(amt,rate, /, ab, xy):
    val = amt*rate/100
    return val
print(intr(2,3, ab=2, xy=3))