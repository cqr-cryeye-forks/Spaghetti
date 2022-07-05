class Colors:
    @staticmethod
    def red(number):
        return "\033[" + str(number) + ";31m"

    @staticmethod
    def green(number):
        return "\033[" + str(number) + ";32m"

    @staticmethod
    def yellow(number):
        return "\033[" + str(number) + ";33m"

    @staticmethod
    def blue(number):
        return "\033[" + str(number) + ";34m"

    @staticmethod
    def purple(number):
        return "\033[" + str(number) + ";35m"

    @staticmethod
    def cyan(number):
        return "\033[" + str(number) + ";36m"

    @staticmethod
    def white(number):
        return "\033[" + str(number) + ";38m"

    @staticmethod
    def end():
        return "\033[0m"


class FakeColors(Colors):
    @staticmethod
    def red(number):
        return ""

    @staticmethod
    def green(number):
        return ""

    @staticmethod
    def yellow(number):
        return ""

    @staticmethod
    def blue(number):
        return ""

    @staticmethod
    def purple(number):
        return ""

    @staticmethod
    def cyan(number):
        return ""

    @staticmethod
    def white(number):
        return ""

    @staticmethod
    def end():
        return ""
