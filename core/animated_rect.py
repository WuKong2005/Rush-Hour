import pygame
import copy
from solution import Move
from board_ui import CELL_SIZE, GRID_SIZE, VehicleInfo

def ease_linear(t):
    """No easing - constant speed"""
    return t

def ease_in_out_cubic(t):
    """Smooth acceleration and deceleration"""
    if t < 0.5:
        return 4 * t * t * t
    else:
        return 1 - pow(-2 * t + 2, 3) / 2
    
class AnimatedVehicle:
    def __init__(self, label, start_pos, end_pos, width, height, color, duration=0.5, easing_func=ease_in_out_cubic):
        self.label = label
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.duration = duration
        self.easing_func = easing_func
        self.elapsed_time = 0
        self.is_animating = False
        self.current_pos = self.start_pos
        
        # Rectangle properties
        self.width = width
        self.height = height
        self.color = color
    
    def reset_animation(self):
        """Reset this animation into its initial state"""
        self.elapsed_time = 0
        self.is_animating = False
        self.current_pos = self.start_pos
    
    def start_animation(self):
        """Start the animation"""
        # if self.is_animating == True or self.is_finished() == True:
        #     return
        self.elapsed_time = 0
        self.is_animating = True
        self.current_pos = self.start_pos
    
    def update(self, dt):
        """Update animation - dt is delta time in seconds"""
        if not self.is_animating:
            return
            
        self.elapsed_time += dt
        
        # Calculate progress (0.0 to 1.0)
        progress = min(self.elapsed_time / self.duration, 1.0)
        
        # Apply easing function
        eased_progress = self.easing_func(progress)
        
        # Interpolate position
        self.current_pos = self.interpolate_position(eased_progress)
        
        # Check if animation is finished
        if progress >= 1.0:
            self.is_animating = False
            self.current_pos = self.end_pos
    
    def is_finished(self):
        return self.is_animating == False and self.current_pos == self.end_pos
    
    def interpolate_position(self, t):
        """Linear interpolation between start and end positions"""
        x = self.start_pos[0] + (self.end_pos[0] - self.start_pos[0]) * t
        y = self.start_pos[1] + (self.end_pos[1] - self.start_pos[1]) * t
        return (x, y)
    
    def render(self, screen, render_func):
        """Draw the rectangle"""
        render_func(screen, self.current_pos[0], self.current_pos[1], self.width, self.height, self.color)
        
def create_animation_list(moves: list[Move], list_vehicle: dict[str, VehicleInfo]):
    clone_list_vehicle = copy.deepcopy(list_vehicle)
    animation_list: list[AnimatedVehicle] = []
    for move in moves:
        label = move.label
        step = move.steps
        stride, color, init_x, init_y, height, width = clone_list_vehicle[label]
        dx = (CELL_SIZE + GRID_SIZE) * (step if stride == 1 else 0)
        dy = (CELL_SIZE + GRID_SIZE) * (0 if stride == 1 else step)
        
        new_vehicle = (stride, color, init_x + dx, init_y + dy, height, width)
        anim = AnimatedVehicle(label, (init_x, init_y), (init_x + dx, init_y + dy), width, height, color)
        animation_list.append(anim)
        clone_list_vehicle[label] = new_vehicle
    
    fixed_vehicle: dict[str, VehicleInfo] = dict()
    for label, info in clone_list_vehicle.items():
        if not any([anim.label == label for anim in animation_list]):
            fixed_vehicle[label] = clone_list_vehicle[label]
    
    return animation_list, fixed_vehicle

def init_animation_order(animation_list: list[AnimatedVehicle]):
    finish = dict[str, int]()
    not_finish = dict[str, int]()
    for index, anim in enumerate(animation_list):
        if anim.is_finished():
            finish[anim.label] = index
            continue
        if not_finish.get(anim.label) is None:
            not_finish[anim.label] = index
        
    return finish | not_finish 

def render_animation(animation_list: list[AnimatedVehicle], anim_order: dict[str, int], 
                     dt: float, anim_index: int, screen: pygame.Surface, render_func):
    finish = False
    for index in anim_order.values():
        anim = animation_list[index]
        anim.update(dt)
        anim.render(screen, render_func)
        if index == anim_index and anim.is_finished():
            finish = True
    return finish