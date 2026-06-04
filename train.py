# n = 6
# Arr : {900,940,950,1100,1500,1800}
# Dep : {910,1200,1120,1130,1900,2000}
# Max Platform Required ?

n = 6
arr = [900,940,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]

i = 0
j = 0
platform = 0
maxPlatform = 0

while i < n and j < n:
    if arr[i] < dep[j]:
        platform+= 1
        if platform > maxPlatform:
            maxPlatform = platform
        i+= 1
    else:
        platform = 1
        j+= 1

print(f" Max Platform : {maxPlatform} ")
