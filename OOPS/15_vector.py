class _2Dvector:
    def __init__(self, i, j):
        self.i=i
        self.j=j
    def showvector(self):
        print(f"The vector is: {self.i}i + {self.j}j")


class _3Dvector(_2Dvector):
    def __init__(self, i, j,k):
        super().__init__( i, j)
        self.k=k
    def showvector(self):
        print(f"The vector is: {self.i}i + {self.j}j + {self.k}k")

a=_2Dvector(1,2)
b=_3Dvector(3,4,5)
a.showvector()
b.showvector()