arr = [1,2,2,3]
arrlen = len(arr)

sp = 0
for fp in range(1,arrlen):
    if arr[fp]!= arr[sp]:
        sp+= 1
        arr[sp] = arr[fp]

    print([arr[x] for x in range(sp+1)])