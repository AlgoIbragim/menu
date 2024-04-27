import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((700, 500))
#back = (255, 136, 255)
#window.fill(back)
back = ()
clock = pygame.time.Clock()
pygame.display.set_caption('menu')
font = pygame.font.Font(None, 36)
game = True
game_state = 'menu'
selected_option = 0

menu_options = ['Start', 'Setting', 'Exit']
selected_options = 0

FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen.fill(BLACK)



class Button():
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height))
        
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text, text_rect)

buttons = []
for i, option in enumerate(menu_options):
    button = Button(option, 400 - 100, 200 + i * 50, 200, 50, BLACK, RED)
    buttons.append(button)

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if game_state == 'menu':
        for i, button in enumerate(buttons):
            if i == selected_option:
                button.color = GREEN
            else:
                button.color = BLACK
            button.draw(screen)




        



    pygame.display.update()
    clock.tick(FPS)