class A:
    def __init__(self,number):
        self.n=number

    def __add__(self,other):
        return self.n+other.n

x=A(-20)
y=A(10)
z=A(2222)
print(y+z)
