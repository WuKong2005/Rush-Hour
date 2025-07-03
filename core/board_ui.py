import pygame
from vehicle import Vehicle

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CELL_SIZE = 80
GRID_SIZE = 2
BOARD_SIZE = CELL_SIZE * 6 + GRID_SIZE * 7
BORDER_WIDTH = 1
MARGIN = 4
VEHICLE_COLOR = "dodgerblue3"
CELL_COLOR = "beige"

VehicleInfo = tuple[int, int, int, int, int, int]

def render_board_grid(screen: pygame.Surface, init_middle_x, init_middle_y):
    board_x = init_middle_x - BOARD_SIZE // 2
    board_y = init_middle_y - BOARD_SIZE // 2
    board_rect = pygame.Rect(board_x - BORDER_WIDTH, board_y - BORDER_WIDTH, BOARD_SIZE + BORDER_WIDTH * 2, BOARD_SIZE + BORDER_WIDTH * 2)
    pygame.draw.rect(screen, "black", board_rect)
    
    for c in range(6):
        for r in range(6):
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

def construct_list_vehicels(board_x: int, board_y: int, vehicles: dict[str, Vehicle]):
    list_vehicle = dict()
    
    for label in vehicles:
        pos = vehicles[label].get_position()
        length = vehicles[label].get_length()
        stride = vehicles[label].get_stride()
        
        c = pos % 6
        r = pos // 6
        len_vertical = 1 if stride == 1 else length
        len_horizontal = length if stride == 1 else 1
        color = "red" if label == "A" else VEHICLE_COLOR
        
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