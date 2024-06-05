class Orange:
    def __init__(self,w,c,days,temp):
        self.weight=w
        self.color=c
        self.days=days
        self.temp=temp

#　インスタンス変数を使った関数、新たな引数は無い
    def mold(self):
        return self.days*self.temp

or1=Orange(200,"Red",10,37)
#　or1にメソッドmold()を適用し、プリント関数に渡す
print(or1.mold())



class Orange1:
    def __init__(self,w,c):
        self.weight=w
        self.color=c
        self.mold=0

#　rotというメソッドに新たな引数daysとtempを渡し、それによって
#　インスタンス変数moldを定義する。
    def rot(self,days,temp):
        self.mold=days*temp

or2=Orange1(200,"Red")
print(or2.mold)
#　メソッドrotのdaysとtempに引数を渡し、インスタンス変数moldを計算する。
or2.rot(10,37)
print(or2.mold)
