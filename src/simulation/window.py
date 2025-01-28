import pygame

from simulation.params import WHITE, WINDOW_HEIGHT, WINDOW_WIDTH


class Window:
    def __init__(self) -> None:
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def clear_window(self, background_color: tuple[int, int, int]) -> None:
        self.surface.fill(background_color)

    def update_window(self) -> None:
        pygame.display.update()

    def draw_entity(self, image: pygame.surface.Surface, x: int, y: int) -> None:
        self.surface.blit(image, (x, y))

    def draw_grid(self, block_size: int) -> None:
        for x in range(0, WINDOW_WIDTH, block_size):
            for y in range(0, WINDOW_HEIGHT, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(self.surface, WHITE, rect, 1)
