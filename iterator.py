class yrange:
    def __init__(self, i, n):
        self.i = i
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1 
            return i
        else:
            raise StopIteration()
            
# for x in yrange(4, 6):
#    print(x)

y = yrange(55, 60)
y_iter = iter(y)
for x in range(3):
    print(next(y_iter))