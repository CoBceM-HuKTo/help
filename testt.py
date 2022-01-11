import pygame

k = 0


def print_text(text, x, y, color=(0, 0, 0), type='data/FONT_TYPE.ttf', size=20):
    font_type = pygame.font.Font(type, size - 5)
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


def game():
    global k
    running = True
    print(12341234123)
    need_input1 = False
    input_text1 = ''
    need_input2 = False
    input_text2 = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if need_input1 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text1 = input_text1[:-1]
                else:
                    if len(input_text1) < 15:
                        input_text1 += event.unicode

            keys = pygame.key.get_pressed()

            if is_click(1350, 800, 500, 50):
                need_input1 = True

            pygame.draw.rect(screen, 'white', (1350, 800, 500, 70), border_radius=5)
            if input_text1 == '':
                print_text('Player1', 1360, 810, color='grey', size=50)

            if need_input1 is True:
                need_input2 = False
                pygame.draw.rect(screen, 'white', (1350, 800, 500, 70), border_radius=5)
                print_text(input_text1, 1360, 810, color='black', size=50)
            else:
                pass





            if need_input2 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text2 = input_text2[:-1]
                else:
                    if len(input_text2) < 15:
                        input_text2 += event.unicode

            keys = pygame.key.get_pressed()

            if is_click(1350, 900, 500, 50):
                need_input2 = True

            pygame.draw.rect(screen, 'white', (1350, 900, 500, 70), border_radius=5)
            if input_text2 == '':
                print_text('Player2', 1360, 910, color='grey', size=50)

            if need_input2 is True:
                need_input1 = False
                pygame.draw.rect(screen, 'white', (1350, 900, 500, 70), border_radius=5)
                print_text(input_text2, 1360, 910, color='black', size=50)
            else:
                pass

            close = Button(x=200, y=200, width=170, height=70, background='white', active_back='grey', action='close')
            close.draw_square(x=40, y=18, text='CLOSE', color='black', size=40, round=10)

            returne = Button(x=400, y=200, width=170, height=70, background='white', active_back='grey',
                             action='returne')
            returne.draw_square(x=25, y=18, text='RETURNE', size=40, round=10)

            sound = Button(x=800, y=200, width=170, height=70, background='white', active_back='grey',
                           action='sound')
            sound.draw_square(x=40, y=18, text='SOUND', size=40, round=100)
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
