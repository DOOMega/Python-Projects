values = []
values2 = [1,2,3,4,5,6] 
values = [ x for x in range(10) if x % 2 == 0]


values.extend("5")

#print([x for x in range(2,100) if not any(x%i==0 for i in range(2,x))])

class Foo:
    def __init__(self, x):
        self.x = x

    def test(self):
        return "Foo: {}".format(self.x)

    def __add__(self, other):
        return self.val * 2 + other.val

    def add(self, other):
        return self.val * 2 + other.val

class Bar:
    def __init__(self, x):
        self.x = x

    def test(self):
        return "Bar: {}".format(self.x)


class Foobar(Foo, Bar):
    pass


obj = Foo(10)
print(obj.add(), obj.__add__())

def test(n, x=[]):
    x.extend(range(n))
    return x

a = test(2)
b = test(3)
print(b)

