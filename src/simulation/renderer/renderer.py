"""Этот модуль содержит класс рендерера и методы для отрисовки карты."""

from simulation.coordinate import Coordinate
from simulation.game_map import Map
from simulation.renderer.color_schemes import ColorScheme
from simulation.settings import (
    ANSI_RESET,
    ANSI_STYLE_END,
    BACKGROUND_256,
    EMPTY_TILE,
    ESC,
)


class Renderer:
    def __init__(self, color_scheme: ColorScheme):
        self.color_scheme = color_scheme

    def render(self, game_map: Map) -> None:
        """Построчно отрисовывает карту в терминале."""
        for y in range(game_map.height):
            print(self._build_row_string(y, game_map))

    def _build_row_string(self, y: int, game_map: Map) -> str:
        """Формирует текстовую строку для заданной строки карты (y)."""
        row = []

        for x in range(game_map.width):
            coord = Coordinate(x, y)
            is_dark = game_map.is_dark_at(coord)

            if game_map.is_empty_at(coord):
                sprite = self._apply_bg_color(
                    EMPTY_TILE,
                    is_dark,
                )
            else:
                entity = game_map.get_entity_at(coord)
                if entity:
                    sprite = self._apply_bg_color(
                        entity.get_sprite(),
                        is_dark,
                    )
            row.append(sprite)

        row.append(self._reset_style())

        return ''.join(row)

    def _apply_bg_color(self, sprite: str, is_tile_dark: bool) -> str:
        """Возвращает ANSI-последовательность для спрайта на фоне соответствующего цвета: ANSI 256-color background."""
        bg = self.color_scheme.bg_dark if is_tile_dark else self.color_scheme.bg_light
        return f'{ESC}{BACKGROUND_256}{bg}{ANSI_STYLE_END}{sprite}'

    @staticmethod
    def _reset_style() -> str:
        """Возвращает ANSI-последовательность для завершения ANSI-стилей в конце строки."""
        return ANSI_RESET + ANSI_STYLE_END
