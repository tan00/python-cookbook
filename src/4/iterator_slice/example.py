import itertools
def count(n):
    while True:
        yield n 
        n += 1 

it = count(0)
for x in itertools.islice(it,2,5):
     print(x)

for x in itertools.islice(it,2,5):
     print(x)
      
        



