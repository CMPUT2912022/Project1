import sys
from Application.application import *
from Interface.interface import *


def main():
    app = None
    # Get database argument
    if len(sys.argv) > 1:
        db = sys.argv[1]
        app = Application(db)
    else:
        app = Application()

    ui = AppUI(app)
    ui.start()
    return


main()
