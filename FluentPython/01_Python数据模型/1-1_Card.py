#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from random import choice
# 构建了一个简单类。类名为Card, 有两处属性 rank, suit
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # 设置版的数字
    suits = 'spqdes diamonds clubs hearts'.split() # 设置牌的花色

    def __init__(self):
        # 通过列表简单类和列表推导式，生成一套52张版的列表。
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    # 由于现实了__getitem__方法，所以类自然支持迭代
    def __getitem__(self, position):
        return self._cards[position]


def main():
    deck = FrenchDeck()
    for card in deck:
        print(FrenchDeck.ranks.index(card.rank))


if __name__ == '__main__':
    main()
