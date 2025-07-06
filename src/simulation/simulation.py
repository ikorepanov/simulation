from typing import Any

import pygame
from pygame.sprite import AbstractGroup

from simulation.action import Action
from simulation.map import Map
from simulation.settings import BGCOLOR, FPS, GRIDCOLOR, HEIGHT, TILESIZE, TITLE, WIDTH

from simulation.action import MoveCreaturesAction, PlaceEntitiesAction


class Simulation:
    def __init__(self, map: Map) -> None:
        # Initialize pygame, game window, etc.
        pygame.init()  # initializes pygame, gets it ready to go
        pygame.mixer.init()  # the mixer handles playing all the sound effects
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # create the window
        pygame.display.set_caption(TITLE)  # "установить заголовок"
        self.clock = pygame.time.Clock()  # handles the speed and keeps track of how fast we're going
        self.running = True

        self.map = map

        self.init_actions: list[Action] = [PlaceEntitiesAction()]
        self.turn_actions: list[Action] = [MoveCreaturesAction()]

    def next_turn(self) -> None:
        for action in self.turn_actions:
            action.execute(self.map)

    def some(self) -> None:  # ?
        while True:
            self.next_turn()

    def start_simulation(self) -> None:
        pass

    def pause_simulation(self) -> None:
        pass

    def new(self) -> None:
        # Start a new game (reset the game, not the whole program)
        self.all_sprites: AbstractGroup[Any] = pygame.sprite.Group()  # collection of sprites

        # for action in self.init_actions:
        #     action.execute(self.map)

        for entity in self.map.entities.values():
            self.all_sprites.add(entity)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for closing window
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self) -> None:
        # Game Loop - Update
        self.all_sprites.update()

    def draw_line(self, start_pos: tuple[int, int], end_pos: tuple[int, int]) -> None:
        pygame.draw.line(self.screen, GRIDCOLOR, start_pos, end_pos)

    def draw_grid(self) -> None:
        for x in range(0, WIDTH, TILESIZE):
            self.draw_line((x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            self.draw_line((0, y), (WIDTH, y))

    def draw(self) -> None:
        # Game Loop - Draw (render)
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()  # *after* drawing everything, flip the display

    def show_start_screen(self) -> None:
        # Game splash/start screen
        pass

    def show_go_screen(self) -> None:
        # Game over/continue
        pass
