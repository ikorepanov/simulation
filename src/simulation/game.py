import pygame as pg

from simulation.settings import BLACK, FPS, HEIGHT, TITLE, WIDTH


class Game:
    def __init__(self) -> None:
        # Initialize game window, etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self) -> None:
        # Start a new game (reset the game, not the whole program)
        self.all_sprites = pg.sprite.Group()  # type: ignore
        self.run()

    def run(self) -> None:
        # Game Loop
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def events(self) -> None:
        # Game Loop - events
        for event in pg.event.get():
            # Check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self) -> None:
        # Game Loop - Update
        self.all_sprites.update()

    def draw(self) -> None:
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everythin, flip the display
        pg.display.flip()

    def show_start_screen(self) -> None:
        # Game splash/start screen
        pass

    def show_go_screen(self) -> None:
        # Game over/continue
        pass
