# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __hash__(self):
#         return self.x
#     def __repr__(self):         # 可视化
#         return 'Point:({},{})'.format(self.x,self.y)
#
#     def __add__(self, other):
#         return Point((self.x + other.x),(self.y + other.y))
#
#     def __sub__(self, other):
#         return Point((self.x - other.x),(self.y - other.y))
#
#     def __lt__(self, other):
#         self_mag = (self.x ** 2) + (self.y ** 2)
#         other_mag = (other.x ** 2) + (other.y ** 2)
#         return self_mag < other_mag
#
#     def __eq__(self, other):
#         return (self.x == other.x) and (self.y == other.y)
#
#     def __gt__(self, other):
#         self_mag = (self.x ** 2) + (self.y ** 2)
#         other_mag = (other.x ** 2) + (other.y ** 2)
#         return self_mag > other_mag
#
#
# p1 = Point(4,5)
# p2 = Point(2,5)
# print(hash(p2))
# print(p1 == p2)
# print(p1 + p2)
# print(p1 - p2)
# print(p1 > p2)
# print(p1 < p2)

class Feb:
    def __init__(self):
        self.item = [1, 1]

    def __call__(self, n):
        if n <= len(self.item):
            return self.item[n - 1]
        for i in range(len(self.item),n):
            sum = self.item[i - 1] + self.item[i - 2]
            self.item.append(sum)
        return self.item[n-1]


fibo = Feb()
print(fibo(7))

