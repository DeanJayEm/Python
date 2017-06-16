print "Hello World"

total = 0
j, m = 0, 1
while m < 4000000:
    j, m = m, j + m
    if j % 2:
        continue
    total += j

print total