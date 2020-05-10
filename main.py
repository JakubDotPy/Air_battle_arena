# copyright

import constants as const
import logging
from game import Game

log = logging.getLogger(const.LOGGER_NAME)


if __name__ == '__main__':
    log.info(const.BANNER_START)

    # create the game object
    g = Game()
    g.show_start_screen()
    g.new()
    g.run()
    g.show_go_screen()

    log.info(const.BANNER_END)
