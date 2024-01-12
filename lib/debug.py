#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    g1 = Game("Chess")
    p1 = Player("Peanut")
    r1 = Result(p1, g1, 10)

    ipdb.set_trace()
