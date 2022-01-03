a = 0
b = 1
c = a + b
print("Result: "+str(a))
print("Result: "+str(b))

for x in range (0,7):
    print("Result: "+str(c))
    a = b
    b = c
    c = a + b