a = []
for i in xrange(2,101):
    for j in xrange(2,101):
        val = i**j
        if val not in a: a.append(val)
print(len(a))