import pygame

def render_text_center(screen, font: pygame.font.Font, short_text, left, top, width, height, color = "black", background_color = None, border = 2):
    font_width, font_height = font.size(short_text)
    text_surface = font.render(short_text, True, color)
    if background_color is not None:
        pygame.draw.rect(screen, background_color, pygame.Rect(left + border, top + border, width - border * 2, height - border * 2))
    screen.blit(text_surface, (left + (width - font_width) / 2, top + (height - font_height) / 2))
