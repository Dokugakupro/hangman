from random import shuffle

class Card:
    #変数suitsリストの定義（マーク）
    suits=["spades","hearts","diamonds","clubs"]
    #変数valuesリストの定義（数字）
    values=[None,None,
            "2","3","4","5","6","7","8","9",
            "10","Jack","Queen","King","Ace"]
    #カードを表す、２つのインスタンス変数valueとsuitを持つ。
    def __init__(self,v,s):
        """スート（マーク）も値も整数値です"""
        self.value=v
        self.suit=s

    #特殊メソッド。
    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v=self.values[self.value]+"  of  "\
           +self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()


deck=Deck()
for card in deck.cards:
    print(card)
