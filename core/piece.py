from bitboard import bb
from constants import HEIGHT, WIDTH, H, V

class Piece:
    def __init__(self, position, length, stride):
        '''
        Arguments:
            position (0 - 35): Top-Left position
            length (2 or 3): Length size
            stride (1 or 6) --> Horizontal or Vertical

        Return:
            value: 16-bit
                bit   0-7: position
                bit   8-9: length
                bit 10-12: stride
        '''
        self.value = position | (length << 8) | (stride << 10)
        self.mask = bb(sum((1 << (position + i * stride)) for i in range(length)))

    def get_position(self):
        return self.value & 0x00FF

    def get_length(self):
        return (self.value >> 8) & 0b11

    def get_stride(self):
        return (self.value >> 10) & 0b111
    
    def get_attributes(self):
        return self.value & 0x00FF, (self.value >> 8) & 0b11, (self.value >> 10) & 0b111
    
    def get_mask(self):
        return bb(self.mask)

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
