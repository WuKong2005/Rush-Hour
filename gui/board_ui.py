import pygame
from core.vehicle import Vehicle
from core.constants import *
from gui.util import *

pygame.init()

DISPLAY = pygame.display.Info()
SCALE = 0.8
SCREEN_WIDTH = SCALE * DISPLAY.current_w
SCREEN_HEIGHT = SCALE * DISPLAY.current_h
CELL_SIZE = SCALE * 78
GRID_SIZE = SCALE * 2
BOARD_SIZE = CELL_SIZE * 6 + GRID_SIZE * 7
BORDER_WIDTH = SCALE * 2
MARGIN = SCALE * 4
TABLE_SIZE_WIDTH = SCALE * 400
TABLE_SIZE_HEIGHT = SCALE * 480
VEHICLE_COLOR = "dodgerblue3"
CELL_COLOR = "beige"
TABLE_BACKGROUND_COLOR = CELL_COLOR
BACKGROUND_COLOR = (222, 233, 232)

# (stride, color, init_x, init_y, height, width)
VehicleInfo = tuple[int, int, int, int, int, int]

def render_board_grid(screen: pygame.Surface, init_middle_x, init_middle_y):
    board_x = init_middle_x - BOARD_SIZE // 2
    board_y = init_middle_y - BOARD_SIZE // 2
    board_rect = pygame.Rect(board_x - BORDER_WIDTH, board_y - BORDER_WIDTH, BOARD_SIZE + BORDER_WIDTH * 2, BOARD_SIZE + BORDER_WIDTH * 2)
    pygame.draw.rect(screen, "black", board_rect)
    
    for c in range(WIDTH):
        for r in range(HEIGHT):
            cell_x = board_x + GRID_SIZE * (c + 1) + CELL_SIZE * c
            cell_y = board_y + GRID_SIZE * (r + 1) + CELL_SIZE * r
            pygame.draw.rect(screen, CELL_COLOR, pygame.Rect(cell_x, cell_y, CELL_SIZE, CELL_SIZE))
    
    exit_middle_x = board_x + GRID_SIZE * (5 + 1) + CELL_SIZE * (5 + 1) + GRID_SIZE
    exit_middle_y = board_y + GRID_SIZE * (2 + 1) + CELL_SIZE * 2 + CELL_SIZE * (1/2)
    exit_A = (exit_middle_x, exit_middle_y - 10)
    exit_B = (exit_middle_x, exit_middle_y + 10)
    exit_C = (exit_middle_x + 10, exit_middle_y)
    pygame.draw.polygon(screen, "black", [exit_A, exit_B, exit_C])
    
    return board_x, board_y

def construct_list_vehicles(board_x: int, board_y: int, vehicles: dict[str, Vehicle]) -> dict[str, VehicleInfo]:
    list_vehicle = dict()
    
    for label in vehicles:
        pos, length, stride = vehicles[label].get_attributes()
        
        c = pos % WIDTH
        r = pos // HEIGHT
        len_vertical = 1 if stride == H else length
        len_horizontal = length if stride == H else 1
        color = "red" if label == MAIN_LABEL else VEHICLE_COLOR
        
        init_x = board_x + GRID_SIZE * (c + 1) + CELL_SIZE * c + MARGIN
        init_y = board_y + GRID_SIZE * (r + 1) + CELL_SIZE * r + MARGIN
        height = CELL_SIZE * len_vertical + GRID_SIZE * (len_vertical - 1) - 2 * MARGIN
        width = CELL_SIZE * len_horizontal + GRID_SIZE * (len_horizontal - 1) - 2 * MARGIN
        list_vehicle[label] = (stride, color, init_x, init_y, height, width)

    return list_vehicle

def render_vehicle(screen: pygame.Surface, x: int, y: int, width: int, height: int, color: str):
    border_rect = pygame.Rect(x, y, width, height)
    inside_rect = pygame.Rect(x + BORDER_WIDTH, y + BORDER_WIDTH, width - 2 * BORDER_WIDTH, height - 2 * BORDER_WIDTH)
    pygame.draw.rect(screen, "black", border_rect, border_radius=8)
    pygame.draw.rect(screen, color, inside_rect, border_radius=8)
            
def static_render(screen: pygame.Surface, board_x: int, board_y: int, list_vehicle: dict[str, VehicleInfo]):
    for label, info in list_vehicle.items():
        _, color, x, y, height, width = info
        render_vehicle(screen, x, y, width, height, color)