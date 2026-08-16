#Take your roll number. Extract its individual digits, and multiply
#each digit by 10 to form your list L (10 numbers in list now)
n = 1024170406
L = []
while (n != 0):
    digit = int(n%10)
    n = int(n/10)
    L.append(digit)

L.reverse()

L.append(100) #insert 100 at last of list
L.insert(3, 200) #insert 200 at index 3

L.pop() #removes 100 from last index
L.remove(200) #removes 200 from list

L_increasing = sorted(L)
#print(L_increasing)
L_decreasing = sorted(L, reverse=True)
#print(L_decreasing)

#print(L[:3])
#print(L[-3:])

avg = sum(L)/len(L)
avgList = [x for x in L if x>avg]
#print(avgList)

print(L)