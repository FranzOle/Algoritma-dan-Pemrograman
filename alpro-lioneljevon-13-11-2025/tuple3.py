listing = {'a': 10, 'b':8, 'c':20}

t = list(listing.items())
print(t)
t.sort()
print(t)

d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items() :
    l.append( (val, key) )
print(l)