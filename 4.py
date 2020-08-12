def scip_zeros(ar, count):
    for i in ar[count:]:
        if i == 1:
            break
        count+=1
    return count
        


X = int(input())
N = int(input())
ar = []
for i in range(N):
   ar.append(int(input()))
   
num_of_brigade = 0
count = scip_zeros(ar, 0)
while count < len(ar):
    count += X
    count = scip_zeros(ar, count)
    num_of_brigade += 1

print(num_of_brigade)


