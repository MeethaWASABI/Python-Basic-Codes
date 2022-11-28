
for j in range (2,100):
    isPrimeNumber = True
    for i in range(2,j):
        if j%i == 0 :
            isPrimeNumber = False
            break
    if isPrimeNumber == True:
         print(j,"is Prime")
