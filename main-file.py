import math

def pascals(row):
    for i in range(row):
        for j in range(1, row - i):
            print(end=' ')

        for k in range(i + 1):
            iCk = math.factorial(i)// (math.factorial(k)*math.factorial(i-k))
            print(iCk,end=' ')
        
        print('')

row = int(input("Enter the number of rows: "))
pascals(row)
