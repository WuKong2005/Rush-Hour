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
font = pygame.font.Font("gui/font/Roboto-VariableFont_wdth,wght.ttf", 30)
font_big = pygame.font.Font("gui/font/Roboto-VariableFont_wdth,wght.ttf", 42)
font_light = pygame.font.Font("gui/font/Roboto-Light.ttf", 30)

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
choose_algo = False
algo_index = 0

while running:
    # limits FPS to 120
    # dt is delta time in seconds since last frame.
    dt = clock.tick(120) / 1000
    
    # local states, check for each loop
    restart = False
    next_move = False
    prev_move = False
    finish_solving = False
    change_map = False
    change_algo = False
    start_solving = False
    
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
                change_map = True
            elif event.key == pygame.K_SPACE:
                if choose_algo < 2:
                    choose_algo += 1
            elif event.key == pygame.K_EQUALS:
                change_algo = True
            elif event.key == pygame.K_s:
                start_solving = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    # if help == True:
    #     # Help screen, explain how to interact with this program
    #     # TODO: make guide
        
    #     pygame.display.flip()
    #     continue
    
    init_middle_x = (screen.get_width() / 2) + 225
    init_middle_y = (screen.get_height() / 2) + 30
    board_x, board_y = render_board_grid(screen, init_middle_x, init_middle_y)
    
    pygame.draw.rect(screen, CELL_COLOR, rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y, 425, BOARD_SIZE))
    pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y, 425, BOARD_SIZE), width=3)
    pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y, 214, 85), width=3)
    pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82, 214, 85), width=3)
    pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y, 214, 85), width=3)
    pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82, 214, 85), width=3)
    
    pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y - 100, 450 + BOARD_SIZE, 85), width=3)
    render_text_center(screen, font_big, "RUSH HOUR SOLVER", init_middle_x - BOARD_SIZE // 2 - 450, board_y - 100, 450 + BOARD_SIZE, 85, "black", CELL_COLOR)

    render_text_center(screen, font, "MAP", init_middle_x - BOARD_SIZE // 2 - 450, board_y, 214, 85)
    render_text_center(screen, font_light, "#" + f"{map_index:02d}", init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y, 214, 85)
    
    if mode == 1 or choose_algo >= 1:
        render_text_center(screen, font, "ALGORITHM", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82, 214, 85)
        render_text_center(screen, font_light, ALGO_NAME[algo_index], init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82, 214, 85)
    
    if mode == 1 or choose_algo >= 2:
        pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 2, 425, 85), width=3)
    
    if mode == 1 or choose_algo >= 3:
        pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 3, 214, 85), width=3)
        pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 4, 214, 85), width=3)
        pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82 * 3, 214, 85), width=3)
        pygame.draw.rect(screen, "black", rect=pygame.Rect(init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82 * 4, 214, 85), width=3)
    
    if mode == 0:
        list_vehicle = construct_list_vehicles(board_x, board_y, board.vehicles)
        static_render(screen, board_x, board_y, list_vehicle)

        if change_map and choose_algo < 3:
            map_index = (map_index + 1) % len(maps)
            board = init_board(maps, map_index)
        elif choose_algo == 1:
            algo_index = (algo_index + change_algo) % len(ALGO_NAME) 
        elif choose_algo == 2:
            render_text_center(screen, font, "SEARCHING...", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 2, 425, 85, "black", "pink")
            pygame.display.flip()
            sol = Solver(board, ALGO_NAME[algo_index])
            sol.solve()
            choose_algo = 3                

        elif choose_algo == 3:
            if sol.is_solvable():
                render_text_center(screen, font, "FOUND A SOLUTION!", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 2, 425, 85, "black", "green")
                
                num_step = sol.get_solution_length()
                time_required = sol.get_measurements()[0]
                
                render_text_center(screen, font, "STEP", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 3, 214, 85)
                render_text_center(screen, font, "TIME(s)", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 4, 214, 85)
                render_text_center(screen, font_light, str(num_step), init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82 * 3, 214, 85)
                render_text_center(screen, font_light, str(round(sol.time, 3)), init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82 * 4, 214, 85)
                render_text_center(screen, font, "START?", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 5, 425, 85)
                
                if finish_solving:
                    choose_algo = 0
                elif start_solving:
                    animation_list, fixed_vehicle = create_animation_list(sol.solution.get_solution(), list_vehicle)
                    list_cost = sol.get_list_cost()
                    print(len(sol.solution.get_solution()), len(animation_list))
                    
                    pause_game = False
                    mode = 1
                    anim_state = 0
                    anim_index = 0
            else:
                render_text_center(screen, font, "NOT SOLUTION...", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 2, 425, 85, "black", "red")
                if finish_solving:
                    choose_algo = 0
    
    elif mode == 1:
        if finish_solving == True:
            mode = 0
            choose_algo = False
            algo_index = 0
        else:
            static_render(screen, board_x, board_y, fixed_vehicle)
            if pause_game == True:
                if restart == True:
                    for anim in animation_list:
                        anim.reset_animation()
                    anim_index = 0
                    anim_state = 0
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
                    
        render_text_center(screen, font, "STEP " + str(anim_index) + "/" + str(len(animation_list)), init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 2, 425, 85, "black", "green")
        render_text_center(screen, font, "g cost", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 3, 214, 85)
        render_text_center(screen, font, "h cost", init_middle_x - BOARD_SIZE // 2 - 450, board_y + 82 * 4, 214, 85)
        render_text_center(screen, font_light, str(list_cost[anim_index][0]), init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82 * 3, 214, 85)
        render_text_center(screen, font_light, str(list_cost[anim_index][1]), init_middle_x - BOARD_SIZE // 2 - 450 + 211, board_y + 82 * 4, 214, 85)
        
    pygame.display.flip()

pygame.quit()
sys.exit()