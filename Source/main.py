from Application.application import *
from Interface.interface import *


def main():
    app = Application()
    ui = AppUI(app)

    ui.start()

    return


main()
