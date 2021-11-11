class concatenate:
    def __init__(self, data1, l=[]):
        self.data1 = data1
        self.l = l

    def __add__(self, other):
        s = concatenate(self.data1 + other.data1)
        return s

    def __sub__(self, other):
        s = concatenate(self.data1 - other.data1)
        return s

    def __mul__(self, other):
        s = concatenate(self.data1 * other.data1)
        return s

    def __truediv__(self, other):
        s = concatenate(self.data1 / other.data1)
        return s

    def __iadd__(self, other):
        self.data1 += other.data1
        return self

    def __lt__(self, other):
        if self.data1 < other.data1:
            return True
        return False
    
    def __gt__(self, other):
        if self.data1 > other.data1:
            return True
        return False

    def __len__(self):
        if len(self.l) != 0:
            return self.l[0]
        return False


l = [2, 1, 3]
x = concatenate(1, l)
y = concatenate(2, l)
z = x + y
print(z.data1)

z = x - y
print(z.data1)

z = x / y
print(z.data1)

z = x * y
print(z.data1)

x += y # x = x + y
print(x.data1)

print(x < y)
print(x > y)
print(len(x), len(y))