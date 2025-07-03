import pygame

# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text) and text[i] != '\n':
            i += 1
        print("initial", i, text[:i])

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1
            
        print("wrap", i, text[:i])

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        if i < len(text) and text[i] == '\n':
            i += 1
        text = text[i:]

    return text

text = "This is a really long sentence with a couple of breaks. \nSometimes it will break even if there isn't a break " \
       "in the sentence, but that's because the text is too long to fit the screen. \nIt can look strange sometimes. \n" \
       "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
       "text will disappear underneath the surface"
       
def render_text_center(screen, font: pygame.font.Font, short_text, left, top, width, height, color = "black", background_color = None, border = 2):
    font_width, font_height = font.size(short_text)
    text_surface = font.render(short_text, True, color)
    if background_color is not None:
        pygame.draw.rect(screen, background_color, pygame.Rect(left + border, top + border, width - border * 2, height - border * 2))
    screen.blit(text_surface, (left + (width - font_width) / 2, top + (height - font_height) / 2))
