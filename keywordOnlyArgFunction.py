def intr(amt, *, rate):
    val = amt*rate/100
    return val
#print(intr(100,200))  -> error
print(intr(100,rate = 200)) 