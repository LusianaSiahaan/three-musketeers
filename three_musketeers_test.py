import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual(string_to_location("A1"),(0,0))
        self.assertEqual(string_to_location("B5"),(1,4))
        self.assertEqual(string_to_location("D3"),(3,2))

    def test_location_to_string(self):
        self.assertEqual(location_to_string([2,2]),"C3")
        self.assertEqual(location_to_string([3,4]),"D5")
        self.assertEqual(location_to_string([0,1]),"A2")

    def test_at(self):
        self.assertEqual(at((3,4)),get_board()[3][4])

    def test_all_locations(self):
        self.assertEqual(all_locations()[2], (0,2))
        self.assertEqual(all_locations()[10], (2,0))
        # Replace with tests

    def test_adjacent_location(self):
        self.assertEqual(adjacent_location((2,3), left), (2,2))
        self.assertEqual(adjacent_location((2,3), right), (2,4))
        self.assertEqual(adjacent_location((2,3), up), (1,3))
        self.assertEqual(adjacent_location((2,3), down), (3,3))
        
    def test_is_legal_move_by_musketeer(self):
        self.assertTrue(is_legal_move_by_musketeer((2,2),'left'))
        self.assertTrue(is_legal_move_by_musketeer((1,3),'down'))
        self.assertFalse(is_legal_move_by_musketeer((0,3),'down'))

    def test_is_legal_move_by_enemy(self):
        self.assertTrue(is_legal_move_by_enemy((1,2),'left'))
        self.assertFalse(is_legal_move_by_enemy((1,2),'right'))

    def test_is_legal_move(self):
        self.assertTrue(is_legal_move_by_musketeer((2,2),'left'))
        self.assertFalse(is_legal_move_by_musketeer((0,3),'down'))
        self.assertTrue(is_legal_move_by_enemy((1,2),'left'))
        self.assertFalse(is_legal_move_by_enemy((1,2),'right'))
        
    def test_can_move_piece_at(self):
        self.assertTrue(can_move_piece_at((2,1)))
        self.assertFalse(can_move_piece_at((0,0)))
        self.assertFalse(can_move_piece_at((0,3)))

    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        
        set_board([ [R, R, M, _, _],
                    [M, M, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('R'))
        self.assertTrue(has_some_legal_move_somewhere('M'))

    def test_possible_moves_from(self):
        self.assertEqual(sorted(possible_moves_from((0,3))),[])
        self.assertEqual(sorted(possible_moves_from((2,3))),['down','right'])
        self.assertEqual(sorted(possible_moves_from((2,2))),['left','right','up'])
        self.assertEqual(sorted(possible_moves_from((0,0))),[])
        self.assertEqual(sorted(possible_moves_from((3,1))),['down','left','right'])

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((0,3)))
        self.assertTrue(can_move_piece_at((2,2)))
        self.assertFalse(can_move_piece_at((0,4)))

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((0,0)))
        self.assertFalse(is_legal_location((0,-1)))
        self.assertFalse(is_legal_location((-2,-1)))

    def test_is_within_board(self):
        self.assertTrue(is_within_board((2,2),'left'))
        self.assertFalse(is_within_board((0,3),'up'))

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual(sorted(all_possible_moves_for('M')), [((0,3), 'left'),((0,3), 'right'),((1,4), 'up')])
        self.assertEqual(sorted(all_possible_moves_for('R')), [((0,2), 'down'),((0,2), 'left')])
        
    def test_make_move(self):
        make_move((1,2),'left')
        self.assertEqual([ [_, _, _, M, _],
                           [_, R, _, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())
        make_move((2,2),'right')
        self.assertEqual([ [_, _, _, M, _],
                           [_, R, _, M, _],
                           [_, R, _, M, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())
        
    def test_choose_computer_move(self):
        set_last_move()
        self.assertTrue(choose_computer_move('M'))
        self.assertTrue(choose_computer_move('R'))
        # Replace with tests; should work for both 'M' and 'R'

    def test_is_enemy_win(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        
        set_board([ [_, _, _, M, R],
                    [_, _, _, _, _],
                    [_, _, R, M, _],
                    [_, M, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(is_enemy_win())

        set_board([ [_, M, M, M, R],
                    [_, _, _, _, _],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        
        # Replace with tests

unittest.main()
