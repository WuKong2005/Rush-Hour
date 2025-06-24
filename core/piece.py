from bitboard import bb
import numpy as np

height = 3
width = 3

H = 1
V = width

class piece:
    def __init__(self, position, length, stride):
        '''
        Arguments:
            position: Top-Left position (0 - 35)
            length: Length size (2 - 3)
            stride: 0 or 1 --> Horizontal or Vertical

        Return:
            value: 16-bit
                bit   0-7: position
                bit   8-9: length
                bit 10-12: stride
        '''
        self.value = position | (length << 8) | (stride << 10)

        self.mask = self.update_mask()

    def get_position(self):
        return self.value & 0x00FF

    def get_length(self):
        return (self.value >> 8) & 0b11

    def get_stride(self):
        return (self.value >> 10) & 0b111
    
    def get_mask(self):
        return bb(self.mask)

    def update_mask(self):
        pos = self.get_position()
        length = self.get_length()
        stride = self.get_stride()

        mask = sum((1 << (pos + i * stride)) for i in range(length))

        return bb(mask)

    def move(self, steps):
        pos = self.get_position()
        stride = self.get_stride()

        offset = steps * stride
        pos += offset

        self.value = (self.value & 0xFF00) | pos

        if offset >= 0:
            self.mask = bb(int(self.mask) << offset)
        else:
            self.mask = bb(int(self.mask) >> -offset)
