from dataclasses import dataclass


@dataclass
class ColorScheme:
    bg_dark: int
    bg_light: int


color_schemes = {
    'industrial': ColorScheme(8, 7),
    'midnight': ColorScheme(18, 27),
    'ocean': ColorScheme(4, 12),
    'savanna': ColorScheme(3, 11),
    'twilight': ColorScheme(5, 13),
    'glacier': ColorScheme(30, 51),
    'abyss': ColorScheme(23, 66),
}
