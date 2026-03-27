import pytest
from bowling_game import BowlingGame

def roll_many(game, rolls):
    """Helper to roll multiple balls in a game"""
    for pins in rolls:
        game.roll(pins)

def test_gutter_game():
    game = BowlingGame()
    roll_many(game, [0]*20)
    assert game.score() == 0

def test_all_ones():
    game = BowlingGame()
    roll_many(game, [1]*20)
    assert game.score() == 20

def test_one_spare():
    game = BowlingGame()
    game.roll(5)
    game.roll(5)  # spare
    game.roll(3)
    roll_many(game, [0]*17)
    assert game.score() == 16  # 10 + 3 + 3

def test_one_strike():
    game = BowlingGame()
    game.roll(10)  # strike
    game.roll(3)
    game.roll(4)
    roll_many(game, [0]*16)
    assert game.score() == 24  # 10 + 3 + 4 + 3 + 4

def test_perfect_game():
    game = BowlingGame()
    roll_many(game, [10]*12)
    assert game.score() == 300

def test_all_spares():
    game = BowlingGame()
    roll_many(game, [5]*21)  # 10 frames * 2 + 1 bonus
    assert game.score() == 150

def test_example_game():
    rolls = [10, 3, 6, 5, 5, 8, 1, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]
    game = BowlingGame()
    roll_many(game, rolls)
    assert game.score() == 190