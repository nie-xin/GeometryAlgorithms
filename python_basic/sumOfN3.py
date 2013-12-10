import time

def sumOfN3(n):
    start = time.time()

    result = (n*(n+1))/2

    end = time.time()

    return result, end - start
#print(sumOfN3(10))

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN3(100000))

