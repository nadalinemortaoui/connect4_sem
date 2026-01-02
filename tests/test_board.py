from src.connect4.board import Board

def test_is_valid_move_in_bounds():
    b = Board()
    assert b.is_valid_move(0) is True
    assert b.is_valid_move(6) is True

def test_is_valid_move_out_of_bounds():
    b = Board()
    assert b.is_valid_move(-1) is False
    assert b.is_valid_move(7) is False

def test_drop_stone_places_on_bottom_row():
    b = Board()
    b.drop_stone(0, 1)
    assert b.grid[5][0] == 1

def test_drop_stone_stacks_two_stones():
    b = Board()
    b.drop_stone(0, 1)
    b.drop_stone(0, 2)
    assert b.grid[5][0] == 1
    assert b.grid[4][0] == 2

def test_check_win_horizontal():
    b = Board()
    for c in range(4):
        b.drop_stone(c, 1)
    assert b.check_win(1) is True

def test_check_win_vertical():
    b = Board()
    for _ in range(4):
        b.drop_stone(0, 2)
    assert b.check_win(2) is True
