items = [1,2,3]

import itertools
print( [x for x in itertools.permutations(items)] )
#[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

print( [x for x in itertools.combinations(items,2)] )
#[(1, 2), (1, 3), (2, 3)]
