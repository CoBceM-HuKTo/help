import pygame

k = 0


def print_text(text, x, y, color=(0, 0, 0), type=None, size=30):
    font_type = pygame.font.Font(type, size)
    text = font_type.render(text, True, color)
    screen.blit(text, (x, y))


def draw_img(file, x, y, width=100, height=100):
    img = pygame.image.load(file)
    img = pygame.transform.rotozoom(img, width, height)
    screen.blit(img, (x, y))


class Button():
    def __init__(self, x, y, width, background, active_back, height=None, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background = background
        self.active_back = active_back
        self.action = action
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed(3)

    def draw_square(self, x, y, text=None, image=None, color=(0, 0, 0), width=None, height=None, size=30, round=0):
        if self.x <= self.mouse[0] <= self.x + self.width:
            if self.y <= self.mouse[1] <= self.y + self.width:
                pygame.draw.rect(screen, self.active_back, (self.x, self.y, self.width, self.height),
                                 border_radius=round)
                if self.click[0] == 1:
                    pygame.mixer.Sound.play(button)
                    pygame.time.delay(100)
                    if self.action == 'close':
                        exit()
                    elif self.action == 'returne':
                        game()
                    elif self.action == 'pause':
                        pause(self.x, self.y, self.width, self.height)
                    else:
                        pass
        else:
            pygame.draw.rect(screen, self.background, (self.x, self.y, self.width, self.height), border_radius=round)
        if text is not None:
            print_text(text=text, x=self.x + x, y=self.y + y, color=color, size=size)
        elif not image:
            draw_img(image, x + self.x, y + self.y, width=100, height=100)


def is_click(pos_x, pos_y, width, height):
    click = pygame.mouse.get_pressed()
    pos_mouse = pygame.mouse.get_pos()
    if click[0] == 1:
        if pos_x <= pos_mouse[0] <= pos_x + width:
            if pos_y <= pos_mouse[1] <= pos_y + height:
                return True
    else:
        return False


def pause(x, y, width, height):
    paused = True
    while paused:
        print_text('Paused...', 800, 100, color='white', size=90)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if is_click(pos_x=x, pos_y=y, width=width, height=height):
            pygame.draw.rect(screen, 'black', (500, 0, 1000, 200))
            paused = False

        pygame.display.update()


def game():
    global k
    running = True
    print(12341234123)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            close = Button(x=200, y=200, width=170, height=70, background='white', active_back='grey', action='close')
            close.draw_square(x=35, y=23, text='CLOSE', color='black', size=40, round=10)

            returne = Button(x=400, y=200, width=170, height=70, background='white', active_back='grey',
                             action='returne')
            returne.draw_square(x=22, y=23, text='RETURNE', size=40, round=10)

            pause_click = Button(x=600, y=200, width=170, height=70, background='white', active_back='grey',
                                 action='pause')
            pause_click.draw_square(x=40, y=23, text='PAUSE', size=40, round=10)

            sound = Button(x=800, y=200, width=170, height=70, background='white', active_back='grey',
                           action='sound')
            sound.draw_square(x=40, y=23, text='SOUND', size=40, round=100)
            if is_click(600, 200, 170, 70):
                pause(600, 200, 170, 70)
            if is_click(800, 200, 170, 70):
                k += 1
            if k % 2 != 0:
                button.set_volume(0.0)
            else:
                button.set_volume(1.0)

        pygame.display.flip()
    pygame.quit()


pygame.init()
screen = pygame.display.set_mode((1920, 1020))
button = pygame.mixer.Sound("data/damage.wav")
game()
