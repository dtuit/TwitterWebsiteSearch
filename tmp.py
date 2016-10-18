x = {'a':'abcc', 'b': 'asdfs'}

y = {'a':'asdf', 'c': 'asdfassd'}

z = x.copy()
z.update(y)

print(x,y,z)