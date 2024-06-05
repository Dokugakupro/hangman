class Orange:
    def __init__(self,a,b):
        self.aaa=a
        self.bbb=b
        self.ccc=0

    def e(self):
        self.ccc=self.aaa*self.bbb

    def f(self):
        d="aaaaa"
        print("d=",d)

    def g(self):
        self.f()
        #　メソッドgに、メソッドfを入れる

pin=Orange(5,2)
print("オブジェクトpinのaaaの値は、",pin.aaa)
print("オブジェクトpinのbbbの値は、",pin.bbb)
print("オブジェクトpinのcccの値は、",pin.ccc,"\n")
#　メソッドeを使ってpin.cccを更新し、0から10に変化させる
pin.e()
print("オブジェクトpinのcccの値は、",pin.ccc,"に更新されました")
pin.f()
pin.g()
