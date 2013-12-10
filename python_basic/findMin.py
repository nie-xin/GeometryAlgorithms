# O(n^2)
def findMin2(L):
    for i in L[0:]:
        for j in L[0:]:
#            print("i: " + str(i))
            #print("j: " + str(j))
            if j < i:
                break
            elif j == L[-1]:
                return i
# O(n)
def findMin(L):
    min = L[0]
    for item in L[1:]:
        if item < min:
            min = item
    return min

#test drive
print(findMin2([12, 23, 45, 4, 7]))
#print(findMin([12, 23, 45, 4, 7]))
