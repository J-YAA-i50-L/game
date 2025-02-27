from GeneralFunctions import *


class LevelDoor(pygame.sprite.Sprite):  # дверь для выбора уровня
    # Открываем изображение и маштабируем
    door = load_image("Door0.png", cat='Door')
    door_image = pygame.transform.scale(door, (door.get_width() * 0.25 * (WIDTH / 1280),
                                        door.get_height() * 0.25 * (HEIGHT / 720)))
    open_door = load_image("Door1.png", cat='Door')
    open_door_image = pygame.transform.scale(open_door, (open_door.get_width() * 0.25 * (WIDTH / 1280),
                                             open_door.get_height() * 0.25 * (HEIGHT / 720)))
    open_door = load_image("Door2.png", cat='Door')
    bloc_door_image = pygame.transform.scale(open_door, (open_door.get_width() * 0.25 * (WIDTH / 1280),
                                             open_door.get_height() * 0.25 * (HEIGHT / 720)))

    def __init__(self, group, x, y, predmet):
        super().__init__(group)
        self.predmet = predmet
        spicok = read_progress()
        for i in spicok:
            if spicok[i] == [False, False, False]:
                com = i
                break
        if spicok[self.predmet] == [False, False, False] and self.predmet != com:
            self.image = LevelDoor.bloc_door_image
            self.flag = False
        else:
            self.image = LevelDoor.door_image
            self.flag = True
        self.rect = self.image.get_rect()
        # Координаты левого верхнего угла с учетом размера экранна
        self.rect.x = x * (WIDTH / 1280)
        self.rect.y = y * (HEIGHT / 720)
        self.button_play = True

    def update(self, *args):
        if self.flag:
            if args:
                if self.rect.collidepoint(args[0].pos):
                    self.image = LevelDoor.open_door_image
                    if self.button_play:
                        button_sound.play()
                        self.button_play = False
                else:
                    self.image = LevelDoor.door_image
                    self.button_play = True
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                if self.predmet == 'tex':
                    signal_input('lvl1')
                elif self.predmet == 'bio':
                    signal_input('lvl2')
                elif self.predmet == 'lit':
                    signal_input('lvl3')
                elif self.predmet == 'fiz':
                    signal_input('lvl4')
                elif self.predmet == 'xim':
                    signal_input('lvl5')
