from collections import Counter, namedtuple, deque


numbers = [1,2,2,2,3,3,6,6,6,9,9,9,9,1]

my_cnt = Counter(numbers)
print(my_cnt)
print(my_cnt.most_common(1))

Point = namedtuple("Point", "x y")
my_point = Point(2, 3)
print(my_point)

people_waiting = ["Dean", "Haidun", "laura", "avy"]
our_line = deque(people_waiting)
print(our_line)
our_line.rotate()
print(our_line)