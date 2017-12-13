n=7
count = 0
while(n):
    count += n & 1
    n = n >> 1
print(count)