import pygame as pg

from simulation.settings import BLACK, FPS, HEIGHT, TITLE, WIDTH


class Game:
    def __init__(self) -> None:
        # Initialize pygame, game window, etc.
        pg.init()  # initializes pygame, gets it ready to go
        pg.mixer.init()  # the mixer handles playing all the sound effects
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))  # create the window
        pg.display.set_caption(TITLE)  # "установить заголовок"
        self.clock = pg.time.Clock()  # handles the speed and keeps track of how fast we're going
        self.running = True

    def new(self) -> None:
        # Start a new game (reset the game, not the whole program)
        self.all_sprites = pg.sprite.Group()  # type: ignore
        self.run()

    def run(self) -> None:
        # NB! Game Loop
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)  # keep loop running at the right speed

    def events(self) -> None:
        # Game Loop - Events (process input)
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Check for closing window
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self) -> None:
        # Game Loop - Update
        self.all_sprites.update()

    def draw(self) -> None:
        # Game Loop - Draw (render)
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()  # *after* drawing everything, flip the display

    def show_start_screen(self) -> None:
        # Game splash/start screen
        pass

    def show_go_screen(self) -> None:
        # Game over/continue
        pass
