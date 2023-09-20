v = [1,2,3,4,5]

n = 5
m = 3
min = 99999999999
max = 0
for i in range(n-(m-1)):
    if min > sum(v[i:i+m]) : min = sum(v[i:i+m])
    if max < sum(v[i:i+m]) : max = sum(v[i:i+m])

print(min, max)