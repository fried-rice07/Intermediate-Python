# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "Marcel"
my_counter = Counter(a)
print(my_counter.keys()) #getting the key of variable a
print(my_counter.values()) # values of variable a
print(my_counter) # print how many string they have in variable a
print(list(my_counter.elements())) # see it to the list

from collections import namedtuple
Point = namedtuple("Point",'x, y')
pt = Point(1,-4)
print(pt.x, pt.y)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

from collections import defaultdict
d = defaultdict(float)
d['a'] = 1.121212
d['b'] = 2
print(d)
print(d['a'])
print(d['b'])

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
