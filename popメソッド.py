#　リストaを定義
a=["a","b","c","d","e","f","g","h","i"]
#　リストaを表示
print("a=",a)
#　forループとpopメソッドを用いて、aから4回、末尾の要素を取り除く。
for i in range(4):
    print(a.pop())
#　上の作業が終わった後のリストaを表示
print("a=",a,"\n")

b=["a","b","c","d","e","f","g","h","i"]
print("b=",b)
#　bの中の要素数が1以上のとき、リストbから末尾の要素を取り除く。
while len(b)>=1:
    b.pop()
print("b=",b)
