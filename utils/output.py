from utils.arguments import cli_arguments
from utils.colors import FakeColors, Colors


class Output:

    def __init__(self, use_colors: bool = True):
        used_colors = FakeColors()
        if cli_arguments.no_color:
            used_colors = FakeColors()
        elif use_colors:
            used_colors = Colors()
        self.RED = used_colors.red(0)
        self.GREEN = used_colors.green(0)
        self.DARK_YELLOW = used_colors.yellow(0)
        self.BLUE = used_colors.blue(0)
        self.WHITE = used_colors.white(0)
        self.END = used_colors.end()

    def plus(self, string: str):
        print(f'{self.GREEN}[+]{self.END} {self.WHITE}{string}{self.END}')

    def less(self, string: str):
        print(f'{self.RED}[-]{self.END} {self.WHITE}{string}{self.END}')

    def test(self, string: str):
        print(f'{self.BLUE}[i]{self.END} {self.WHITE}{string}{self.END}')

    def info(self, string: str):
        print(f'{self.DARK_YELLOW}[i]{self.END} {self.WHITE}{string}{self.END}')
