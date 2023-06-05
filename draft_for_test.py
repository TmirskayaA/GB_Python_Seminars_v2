a = [1, 2, 3, 4, 5]
min = 1
i = 4
l = 0
while i >= min:
    for j in a:
        if j == i: 
            l = i
            print(f"L = {l}")
        i -= 1

a = [5,4,3,1,2]
i = 1
max = 5
while i <= max:
    for j in a:
        if j == i: 
            l = i
            print(f"M = {l}")
    i += 1