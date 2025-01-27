import pygame

from simulation.params import WINDOW_WIDTH, WINDOW_HEIGHT


class Window:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def clear_window(self, background_color: tuple[int, int, int]) -> None:
        self.window.fill(background_color)

    def update_window(self) -> None:
        pygame.display.update()

    def draw_entity(self, image: pygame.surface.Surface, x: int, y: int) -> None:
        self.window.blit(image, (x, y))
