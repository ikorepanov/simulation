"""Этот модуль содержит класс рендерера и методы для отрисовки карты."""

import sys

from simulation.coordinate import Coordinate
from simulation.game_map import Map
from simulation.renderer.color_schemes import ColorScheme
from simulation.settings import (
    ANSI_BACKGROUND_256,
    ANSI_ESC,
    ANSI_RESET,
    ANSI_STYLE_END,
    EMPTY_COORD_SPRITE,
)


class Renderer:
    def __init__(self, color_scheme: ColorScheme):
        self.color_scheme = color_scheme

    def render(self, game_map: Map) -> None:
        """Построчно отрисовывает карту, каждый раз перенося курсор на новую строку"""
        for y in range(game_map.height):
            sys.stdout.write(f'{self._build_row_string(y, game_map)}\n')

    def _build_row_string(self, y: int, game_map: Map) -> str:
        """Формирует текстовую строку для заданной строки карты (y)."""
        row = []

        for x in range(game_map.width):
            coord = Coordinate(x, y)
            is_dark = game_map.is_dark_at(coord)

            if game_map.is_empty_at(coord):
                sprite = self._apply_bg_color(
                    EMPTY_COORD_SPRITE,
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

    def _apply_bg_color(self, sprite: str, is_coord_dark: bool) -> str:
        """Возвращает ANSI-последовательность для спрайта на фоне соответствующего цвета: ANSI 256-color background."""
        bg = self.color_scheme.bg_dark if is_coord_dark else self.color_scheme.bg_light
        return ANSI_ESC + ANSI_BACKGROUND_256 + str(bg) + ANSI_STYLE_END + sprite

    @staticmethod
    def _reset_style() -> str:
        """Возвращает ANSI-последовательность для завершения ANSI-стилей в конце строки."""
        return ANSI_ESC + ANSI_RESET + ANSI_STYLE_END
