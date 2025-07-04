import pygame
import sys
import random
from gui.animated_rect import *
from gui.map_sample import *
from gui.board_ui import *
from gui.util import *
from core.solver import Solver

# constants
ALGO_NAME = list(Solver().algo_map.keys())

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rush Hour solver")
clock = pygame.time.Clock()
running = True
dt = 0
        
# font 
font = pygame.font.Font("gui/font/Roboto-VariableFont_wdth,wght.ttf", 20)
font_big = pygame.font.Font("gui/font/Roboto-VariableFont_wdth,wght.ttf", 42)
font_light = pygame.font.Font("gui/font/Roboto-Light.ttf", 20)

# global states, update for each loop
mode = 0
maps = get_random_maps("core/rush_db.txt", MAXIMUM_MAPS)
map_index = 0
board = init_board(maps, map_index)

sol = Solver()

animation_list = []
fixed_vehicle = []
list_cost = []

anim_state = 0
anim_index = 0

pause_game = False
# help = False
choose_algo = 1
algo_index = 0

init_middle_x = (screen.get_width() * 11) / 16
init_middle_y = (screen.get_height() * 17) / 36
board_x, board_y = render_board_grid(screen, init_middle_x, init_middle_y)

arrow_w, arrow_h = 10, 20
table_start_x = screen.get_width() / 8
table_start_y = board_y

map_text_x = table_start_x + 3 * TABLE_SIZE_WIDTH / 4
map_text_y = table_start_y + TABLE_SIZE_HEIGHT / 12
algo_text_x = table_start_x + 3 * TABLE_SIZE_WIDTH / 4
algo_text_y = table_start_y + 3 * TABLE_SIZE_HEIGHT / 12
steps_text_x = table_start_x + 3 * TABLE_SIZE_WIDTH / 4
steps_text_y = table_start_y + 5 * TABLE_SIZE_HEIGHT / 12
time_text_x = table_start_x + 3 * TABLE_SIZE_WIDTH / 4
time_text_y = table_start_y + 7 * TABLE_SIZE_HEIGHT / 12
cost_text_x = table_start_x + 3 * TABLE_SIZE_WIDTH / 4
cost_text_y = table_start_y + 9 * TABLE_SIZE_HEIGHT / 12
memory_text_x = table_start_x + 3 * TABLE_SIZE_WIDTH / 4
memory_text_y = table_start_y + 11 * TABLE_SIZE_HEIGHT / 12

MAP_ARROW_LEFT = pygame.Rect(map_text_x - 74, map_text_y - arrow_h // 2, arrow_w, arrow_h)
MAP_ARROW_RIGHT = pygame.Rect(map_text_x + 74 - arrow_w, map_text_y - arrow_h // 2, arrow_w, arrow_h)
ALGO_ARROW_LEFT = pygame.Rect(algo_text_x - 74, algo_text_y - arrow_h // 2, arrow_w, arrow_h)
ALGO_ARROW_RIGHT = pygame.Rect(algo_text_x + 74 - arrow_w, algo_text_y - arrow_h // 2, arrow_w, arrow_h)
STEP_ARROW_LEFT = pygame.Rect(steps_text_x - 74, steps_text_y - arrow_h // 2, arrow_w, arrow_h)
STEP_ARROW_RIGHT = pygame.Rect(steps_text_x + 74 - arrow_w, steps_text_y - arrow_h // 2, arrow_w, arrow_h)
MEMO_ARROW_LEFT = pygame.Rect(memory_text_x - 74, memory_text_y - arrow_h // 2, arrow_w, arrow_h)
MEMO_ARROW_RIGHT = pygame.Rect(memory_text_x + 74 - arrow_w, memory_text_y - arrow_h // 2, arrow_w, arrow_h)

SOLVE_BOX = pygame.Rect(table_start_x, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, TABLE_SIZE_WIDTH, TABLE_SIZE_HEIGHT / 8)
START_BOX = pygame.Rect(board_x + BOARD_SIZE * 3 // 8, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, BOARD_SIZE // 4, TABLE_SIZE_HEIGHT / 8)
FINISH_BOX = pygame.Rect(board_x, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, BOARD_SIZE // 4, TABLE_SIZE_HEIGHT / 8)
PAUSE_BOX = pygame.Rect(board_x + BOARD_SIZE * 3 // 4, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, BOARD_SIZE // 4, TABLE_SIZE_HEIGHT / 8)

while running:
    # limits FPS to 120
    # dt is delta time in seconds since last frame.
    dt = clock.tick(120) / 1000
    
    # local states, check for each loop
    restart = False
    next_move = False
    prev_move = False
    finish_solving = False
    change_map = 0
    change_algo = 0
    start_solving = False
    measure_memory = False
    
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                pause_game = pause_game ^ 1
            elif event.key == pygame.K_r:
                restart = True
            elif event.key == pygame.K_RIGHT:
                next_move = True
            elif event.key == pygame.K_LEFT:
                prev_move = True
            elif event.key == pygame.K_ESCAPE:
                finish_solving = True
            # elif event.key == pygame.K_h:
            #     help = help ^ 1
            elif event.key == pygame.K_KP_ENTER:
                change_map = 1
            elif event.key == pygame.K_SPACE:
                if choose_algo < 2:
                    choose_algo += 1
            elif event.key == pygame.K_EQUALS:
                change_algo = 1
            elif event.key == pygame.K_s:
                start_solving = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ALGO_ARROW_LEFT.collidepoint(event.pos):
                change_algo = -1
            elif ALGO_ARROW_RIGHT.collidepoint(event.pos):
                change_algo = 1
            elif MAP_ARROW_LEFT.collidepoint(event.pos):
                change_map = -1
            elif MAP_ARROW_RIGHT.collidepoint(event.pos):
                change_map = 1
            elif STEP_ARROW_LEFT.collidepoint(event.pos):
                prev_move = True
            elif STEP_ARROW_RIGHT.collidepoint(event.pos):
                next_move = 1
            elif MEMO_ARROW_LEFT.collidepoint(event.pos):
                pass
            elif MEMO_ARROW_RIGHT.collidepoint(event.pos):
                pass
            elif SOLVE_BOX.collidepoint(event.pos):
                if choose_algo == 1:
                    choose_algo = 2
            elif START_BOX.collidepoint(event.pos):
                start_solving = True
            elif PAUSE_BOX.collidepoint(event.pos):
                pause_game = pause_game ^ 1
            elif FINISH_BOX.collidepoint(event.pos):
                finish_solving = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BACKGROUND_COLOR)
    
    # if help == True:
    #     # Help screen, explain how to interact with this program
    #     # TODO: make guide
        
    #     pygame.display.flip()
    #     continue
    
    # Render main board 
    board_x, board_y = render_board_grid(screen, init_middle_x, init_middle_y)

    # Information table
    # draw
    pygame.draw.rect(screen, TABLE_BACKGROUND_COLOR, rect=pygame.Rect(table_start_x, table_start_y, TABLE_SIZE_WIDTH, TABLE_SIZE_HEIGHT))
    pygame.draw.rect(screen, "black", rect=pygame.Rect(table_start_x, table_start_y, TABLE_SIZE_WIDTH, TABLE_SIZE_HEIGHT), width=3)
    for i in range(6):
        pygame.draw.rect(screen, "black", rect=pygame.Rect(table_start_x, table_start_y + i * TABLE_SIZE_HEIGHT / 6, TABLE_SIZE_WIDTH / 2, TABLE_SIZE_HEIGHT / 6), width=1)
        pygame.draw.rect(screen, "black", rect=pygame.Rect(table_start_x + TABLE_SIZE_WIDTH / 2, table_start_y + i * TABLE_SIZE_HEIGHT / 6, TABLE_SIZE_WIDTH / 2, TABLE_SIZE_HEIGHT / 6), width=1)

    render_text_center(screen, font, "MAP", table_start_x + TABLE_SIZE_WIDTH / 4, table_start_y + TABLE_SIZE_HEIGHT / 12, 0, 0)
    render_text_center(screen, font, "ALGORITHM", table_start_x + TABLE_SIZE_WIDTH / 4, table_start_y + 3 * TABLE_SIZE_HEIGHT / 12, 0, 0)
    render_text_center(screen, font, "STEPS", table_start_x + TABLE_SIZE_WIDTH / 4, table_start_y + 5 * TABLE_SIZE_HEIGHT / 12, 0, 0)
    render_text_center(screen, font, "TIME(s)", table_start_x + TABLE_SIZE_WIDTH / 4, table_start_y + 7 * TABLE_SIZE_HEIGHT / 12, 0, 0)
    render_text_center(screen, font, "COST", table_start_x + TABLE_SIZE_WIDTH / 4, table_start_y + 9 * TABLE_SIZE_HEIGHT / 12, 0, 0)
    render_text_center(screen, font, "HEURISTIC", table_start_x + TABLE_SIZE_WIDTH / 4, table_start_y + 11 * TABLE_SIZE_HEIGHT / 12, 0, 0)
    
    #draw arrow
    pygame.draw.polygon(screen, "black", [
        (map_text_x - 74, map_text_y),
        (map_text_x - 74 + arrow_w, map_text_y - arrow_h // 2),
        (map_text_x - 74 + arrow_w, map_text_y + arrow_h // 2)
    ])
    pygame.draw.polygon(screen, "black", [
        (map_text_x + 74, map_text_y),
        (map_text_x + 74 - arrow_w, map_text_y - arrow_h // 2),
        (map_text_x + 74 - arrow_w, map_text_y + arrow_h // 2)
    ])

    pygame.draw.polygon(screen, "black", [
        (algo_text_x - 74, algo_text_y),
        (algo_text_x - 74 + arrow_w, algo_text_y - arrow_h // 2),
        (algo_text_x - 74 + arrow_w, algo_text_y + arrow_h // 2)
    ])
    pygame.draw.polygon(screen, "black", [
        (algo_text_x + 74, algo_text_y),
        (algo_text_x + 74 - arrow_w, algo_text_y - arrow_h // 2),
        (algo_text_x + 74 - arrow_w, algo_text_y + arrow_h // 2)
    ])
    
    pygame.draw.polygon(screen, "black", [
        (steps_text_x - 74, steps_text_y),
        (steps_text_x - 74 + arrow_w, steps_text_y - arrow_h // 2),
        (steps_text_x - 74 + arrow_w, steps_text_y + arrow_h // 2)
    ])
    pygame.draw.polygon(screen, "black", [
        (steps_text_x + 74, steps_text_y),
        (steps_text_x + 74 - arrow_w, steps_text_y - arrow_h // 2),
        (steps_text_x + 74 - arrow_w, steps_text_y + arrow_h // 2)
    ])

    # pygame.draw.polygon(screen, "black", [
    #     (memory_text_x - 74, memory_text_y),
    #     (memory_text_x - 74 + arrow_w, memory_text_y - arrow_h // 2),
    #     (memory_text_x - 74 + arrow_w, memory_text_y + arrow_h // 2)
    # ])
    # pygame.draw.polygon(screen, "black", [
    #     (memory_text_x + 74, memory_text_y),
    #     (memory_text_x + 74 - arrow_w, memory_text_y - arrow_h // 2),
    #     (memory_text_x + 74 - arrow_w, memory_text_y + arrow_h // 2)
    # ])

    render_text_center(screen, font_big, "RUSH HOUR SOLVER", screen.get_width() / 2, board_y / 2, 0, 0)

    # button
    pygame.draw.rect(screen, "black", SOLVE_BOX, width=3)
    render_text_center(screen, font, "SOLVE", table_start_x, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, TABLE_SIZE_WIDTH, TABLE_SIZE_HEIGHT / 8, "black", (80,255,70))

    pygame.draw.rect(screen, "black", START_BOX, width=3)
    render_text_center(screen, font, ("START" if mode == 0 else "RESET"), board_x + BOARD_SIZE * 3 // 8, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, BOARD_SIZE // 4, TABLE_SIZE_HEIGHT / 8, "black", (80,255,70))

    pygame.draw.rect(screen, "black", FINISH_BOX, width=3)
    render_text_center(screen, font, "FINISH", board_x, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, BOARD_SIZE // 4, TABLE_SIZE_HEIGHT / 8, "black", (255, 80, 80))

    pygame.draw.rect(screen, "black", PAUSE_BOX, width=3)
    render_text_center(screen, font, "PAUSE", board_x + BOARD_SIZE * 3 // 4, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, BOARD_SIZE // 4, TABLE_SIZE_HEIGHT / 8, "black", (255, 120, 120))
    render_text_center(screen, font_light, "#" + f"{map_index:02d}", map_text_x, map_text_y, 0, 0)
    
    if mode == 1 or choose_algo >= 1:
        # render_text_center(screen, font, "ALGORITHM", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82, 214, 85)
        render_text_center(screen, font_light, ALGO_NAME[algo_index], algo_text_x, algo_text_y, 0, 0)
    
    # if mode == 1 or choose_algo >= 2:
    #     pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 2, 425, 85), width=3)
    
    # if mode == 1 or choose_algo >= 3:
    #     pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 3, 214, 85), width=3)
    #     pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 4, 214, 85), width=3)
    #     pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82 * 3, 214, 85), width=3)
    #     pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82 * 4, 214, 85), width=3)
    
    if mode == 0:
        list_vehicle = construct_list_vehicles(board_x, board_y, board.vehicles)
        static_render(screen, board_x, board_y, list_vehicle)

        if change_map != 0 and choose_algo < 3:
            map_index = (len(maps) + map_index + change_map) % len(maps)
            board = init_board(maps, map_index)
        elif choose_algo == 1:
            algo_index = (len(ALGO_NAME) + algo_index + change_algo) % len(ALGO_NAME) 
        elif choose_algo == 2:
            render_text_center(screen, font, "SEARCHING...", table_start_x, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, TABLE_SIZE_WIDTH, TABLE_SIZE_HEIGHT / 8, "black", "pink")
            pygame.display.flip()
            sol = Solver(board, ALGO_NAME[algo_index])
            sol.solve()
            choose_algo = 3                

        elif choose_algo == 3:
            if sol.is_solvable():
                render_text_center(screen, font, "FOUND A SOLUTION! START?", table_start_x, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, TABLE_SIZE_WIDTH, TABLE_SIZE_HEIGHT / 8, "black", (80,255,70))
                
                num_step = sol.get_solution_length()
                time_required = sol.get_measurements()[0]
                
                render_text_center(screen, font_light, str(num_step), steps_text_x, steps_text_y, 0, 0)
                render_text_center(screen, font_light, str(round(sol.time, 3)), time_text_x, time_text_y, 0, 0)
                
                if finish_solving:
                    choose_algo = 1
                elif start_solving:
                    animation_list, fixed_vehicle = create_animation_list(sol.solution.get_solution(), list_vehicle)
                    list_cost = sol.get_list_cost()
                    print(len(sol.solution.get_solution()), len(animation_list))
                    
                    pause_game = False
                    mode = 1
                    anim_state = 0
                    anim_index = 0
            else:
                render_text_center(screen, font, "NOT SOLUTION...", table_start_x, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, TABLE_SIZE_WIDTH, TABLE_SIZE_HEIGHT / 8, "black", "red")
                if finish_solving:
                    choose_algo = 1
    
    elif mode == 1:
        if start_solving:
            restart = True
        
        if finish_solving == True:
            mode = 0
            choose_algo = 1
            algo_index = 0
        else:
            static_render(screen, board_x, board_y, fixed_vehicle)
            if pause_game == True:
                if restart == True:
                    for anim in animation_list:
                        anim.reset_animation()
                    anim_index = 0
                    anim_state = 0
                    pause_game = False
                elif prev_move == True:
                    if anim_state == 2:
                        anim_index -= 1
                        animation_list[anim_index].reset_animation()
                        anim_state = 0
                    elif anim_state == 1:
                        animation_list[anim_index].reset_animation()
                        anim_state = 0
                    else:
                        if anim_index == 0:
                            pass
                        else:
                            anim_index -= 1
                            animation_list[anim_index].reset_animation()    
                    prev_move = False
                elif next_move == True:
                    if anim_state == 2:
                        pass
                    else:
                        animation_list[anim_index].start_animation()
                        animation_list[anim_index].update(1.0)
                        anim_index += 1
                        if anim_index == len(animation_list):
                            anim_state = 2
                        else:
                            anim_state = 0   
                    next_move = False
                
                order = init_animation_order(animation_list)
                render_animation(animation_list, order, 0, anim_index, screen, render_vehicle)
                
            else:
                order = init_animation_order(animation_list)
                result = render_animation(animation_list, order, dt, anim_index, screen, render_vehicle)
                if result == True:
                    anim_index += 1
                    if anim_index == len(animation_list):
                        anim_state = 2
                    else:
                        anim_state = 0
                if anim_state == 0:
                    animation_list[anim_index].start_animation()
                    anim_state = 1
                    
        render_text_center(screen, font_light, ALGO_NAME[algo_index], algo_text_x, algo_text_y, 0, 0)
        render_text_center(screen, font_light, str(round(sol.time, 3)), time_text_x, time_text_y, 0, 0)
        render_text_center(screen, font_light, "SOLVING...", table_start_x, table_start_y + TABLE_SIZE_HEIGHT * 13 // 12, TABLE_SIZE_WIDTH, TABLE_SIZE_HEIGHT / 8, "black", "cyan")
        render_text_center(screen, font_light, str(anim_index) + "/" + str(len(animation_list)), steps_text_x, steps_text_y, 0, 0, "black", "green")
        render_text_center(screen, font_light, str(list_cost[anim_index][0]), cost_text_x, cost_text_y, 0, 0)
        render_text_center(screen, font_light, str(list_cost[anim_index][1]), memory_text_x, memory_text_y, 0, 0)

    pygame.display.flip()

pygame.quit()
sys.exit()