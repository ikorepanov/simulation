from simulation.game import Game


def main() -> None:
    game = Game()
    game.show_start_screen()
    game.new()


if __name__ == '__main__':
    main()
