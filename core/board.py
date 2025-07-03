import numpy as np
from core.bitboard import bb
from core.vehicle import Vehicle
from core.constants import HEIGHT, WIDTH, H, V, MAIN_LABEL
from core.solution import Move
import copy

class EnumBoard:
    def __init__(self, mask_horizontal: bb = bb(0), mask_vertical: bb = bb(0)):
        self.mask_horizontal = mask_horizontal
        self.mask_vertical = mask_vertical

    def __eq__(self, other: "EnumBoard"):
        return isinstance(other, EnumBoard) and self.mask_horizontal == other.mask_horizontal and self.mask_vertical == other.mask_vertical

    def __hash__(self):
        return hash((self.mask_horizontal, self.mask_vertical))

class Board:
    def __init__(self, char_board: list = None):
        '''
        Initialize a Board from given char_board
        Parameters:
            char_board: 1D array (length: HEIGHT * WIDHT) of characters. '.' or 'o' for empty squares, another characters for vehicles.
        '''
        self.mask_horizontal = bb(0)
        self.mask_vertical = bb(0)
        self.vehicles: dict[str, Vehicle] = {}

        if char_board is not None:
            if len(char_board) != HEIGHT * WIDTH:
                print('Invalid char_board')
                return

            char_board = np.array(char_board)

            for label in np.unique(char_board):
                if label == '.' or label == 'o':
                    continue

                positions = np.where(char_board == label)[0]

                pos = positions[0]
                length = len(positions)
                stride = positions[1] - positions[0]

                new_Vehicle = Vehicle(pos, length, stride)

                self.vehicles[label] = new_Vehicle

                if stride == H:
                    self.mask_horizontal |= new_Vehicle.get_mask()
                elif stride == V:
                    self.mask_vertical |= new_Vehicle.get_mask()
        

    def get_mask(self):
        return self.mask_horizontal | self.mask_vertical
    
    def get_horizontal_mask(self):
        return self.mask_horizontal
    
    def get_vertical_mask(self):
        return self.mask_vertical
    
    def board_to_enum(self):
        return EnumBoard(self.mask_horizontal, self.mask_vertical)

    # def add_vehicle(self, label: str, new_Vehicle: Vehicle):
    #     '''
    #     Add a new Vehicle to current Board. ignore if this Vehicle exists

    #     Parameters:
    #         label: label of new Vehicle
    #         new_Vehicle: Position of new Vehicle
    #     '''
    #     if label in self.vehicles:
    #         print(f'{label} existed')
    #     else:
    #         self.vehicles[label] = new_Vehicle
    #         stride = self.vehicles[label].get_stride()
            
    #         if stride == H:
    #             self.mask_horizontal |= self.vehicles[label].get_mask()
    #         elif stride == V:
    #             self.mask_vertical |= self.vehicles[label].get_mask()

    # def remove_Vehicle(self, label):
    #     if label in self.vehicles:
    #         stride = self.vehicles[label].get_stride()
    
    #         if stride == H:
    #             self.mask_horizontal &= ~self.vehicles[label].get_mask()
    #         elif stride == V:
    #             self.mask_vertical &= ~self.vehicles[label].get_mask()

    #         del self.vehicles[label]

    def move_vehicle(self, move: Move, generate_copy: bool = False):
        '''
        Apply a move on current board

        Parameters:
            move: Specific the movement
            generate_copy: True if you want to make a copy, else False
        
        Returns:
            new_board (Board): A new board after applying move (just return if copy = True)
        '''

        if not generate_copy:
            cur_Vehicle = self.vehicles[move.label]

            if cur_Vehicle.get_stride() == H:
                self.mask_horizontal &= ~cur_Vehicle.get_mask()
                cur_Vehicle.move(move.steps)
                self.mask_horizontal |= cur_Vehicle.get_mask()
            else:
                self.mask_vertical &= ~cur_Vehicle.get_mask()
                cur_Vehicle.move(move.steps)
                self.mask_vertical |= cur_Vehicle.get_mask()
        else:
            new_board = copy.deepcopy(self)
            new_board.move_vehicle(move, generate_copy=False)
            return new_board

    def get_cost_move(self, move: Move):
        return abs(move.steps) * self.vehicles[move.label].get_length()

    def get_legal_moves(self):
        '''
        Generate all legal single moves (moves just 1 step)

        Returns:
            legal_moves (list of moves): A list of legal moves that can be applied on current board
        '''
        legal_moves = []
        mask = self.mask_horizontal | self.mask_vertical

        for label in self.vehicles:
            pos, length, stride = self.vehicles[label].get_attributes()            

            if stride == H:
                left, right = pos - H, pos + H * length
                if left >= 0 and left // WIDTH == pos // WIDTH and not (int(mask) >> left) & 1:
                    legal_moves.append(Move(label, -1))

                if right < HEIGHT * WIDTH and right // WIDTH == pos // WIDTH and not (int(mask) >> right) & 1:
                    legal_moves.append(Move(label, 1))

            elif stride == V:
                top, bottom = pos - V, pos + V * length
                if top >= 0 and not (int(mask) >> top) & 1:
                    legal_moves.append(Move(label, -1))
                
                if bottom < HEIGHT * WIDTH and not (int(mask) >> bottom) & 1:
                    legal_moves.append(Move(label, 1))

        return legal_moves

    def is_goal(self):
        if MAIN_LABEL in self.vehicles:
            pos, length, _ = self.vehicles[MAIN_LABEL].get_attributes()
            return pos + length == WIDTH * (pos // WIDTH + 1)
        return False

    def print(self):
        new_board = [' ' for _ in range(HEIGHT * WIDTH)]

        for label in self.vehicles:
            pos, length, stride = self.vehicles[label].get_attributes()

            for _ in range(length):
                new_board[pos] = label
                pos += stride
            
        new_board = np.array(new_board).reshape((HEIGHT, WIDTH))
        print(new_board)


    def heuristic(self):
        '''
        Calculate the heuristic value of current state 
        
        Returns:
            heuristic_value: (number of vertical blocking Vehicles) + (distance of MAIN Vehicle to GOAL)
        '''
        pos, length, _ = self.vehicles[MAIN_LABEL].get_attributes()

        count = (WIDTH * (pos // WIDTH + 1) - (pos + length)) * length
        i = pos + length
        while i // WIDTH == pos // WIDTH:
            count += ((int(self.mask_vertical) >> i) & 1) << 1
            i += 1

        return count