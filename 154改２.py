class Orange:
    def __init__(self,w,c):
        """weight（重さ）はグラム"""
        self.weight=w
        self.color=c
        # moldの引数はこのメソッドでは渡していないが、self.はつける必要がある。
        self.mold=0
        print("Created!")

    def rot(self,days,temp):
        """temp（温度）は摂氏"""
        self.mold=days*temp

orange=Orange(200,"orange")
print(orange.mold)
orange.rot(10,37)
print(orange.mold)
print(orange.weight)
print(orange.color)
