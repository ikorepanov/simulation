import asyncio


async def ainput():
    return asyncio.to_thread(input)


class SomeClass:
    def __init__(self) -> None:
        self.playing = True

    def make_pause(self) -> None:
        self.playing = not self.playing

    def print_playing(self) -> None:
        print(f'Playing is {self.playing}')


some = SomeClass()

while True:
    inp = input()
    if inp == 'p':
        some.make_pause()
        some.print_playing()
    else:
        print('Use "p" letter')
