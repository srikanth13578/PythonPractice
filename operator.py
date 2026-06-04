###
# [10,20,30,40,50]
# [50,10,20,30,40] | n = 1
# [40,50,10,20,30] | n = 2
# [50,10,20,30,40] | n = 156
# n = n % 5

data = [10,20,30,40,50]
len=len(data)
n = 143
n = n % len

# 1 shift
last = data[-1]
for i in range(len - 1,-1,-1):
    data[i] = data[i - 1]
data[0] = last

print(data)

