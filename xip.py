#!/usr/bin/env python3

from engine.Dispatcher import Dispatcher
from engine.Logger import Logger
from engine.Parser import Parser
from engine.Randomizer import Randomizer


__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


def welcome():
    print("""

        XXXXXXX       XXXXXXXIIIIIIIIIIPPPPPPPPPPPPPPPPP
        X:::::X       X:::::XI::::::::IP::::::::::::::::P
        X:::::X       X:::::XI::::::::IP::::::PPPPPP:::::P
        X::::::X     X::::::XII::::::IIPP:::::P     P:::::P
        XXX:::::X   X:::::XXX  I::::I    P::::P     P:::::P
           X:::::X X:::::X     I::::I    P::::P     P:::::P
            X:::::X:::::X      I::::I    P::::PPPPPP:::::P
             X:::::::::X       I::::I    P:::::::::::::PP
             X:::::::::X       I::::I    P::::PPPPPPPPP
            X:::::X:::::X      I::::I    P::::P
           X:::::X X:::::X     I::::I    P::::P
        XXX:::::X   X:::::XXX  I::::I    P::::P
        X::::::X     X::::::XII::::::IIPP::::::PP
        X:::::X       X:::::XI::::::::IP::::::::P
        X:::::X       X:::::XI::::::::IP::::::::P
        XXXXXXX       XXXXXXXIIIIIIIIIIPPPPPPPPPP

    """)

if __name__ == "__main__":
    welcome()

    config = Parser().parse()
    logger = Logger(config["logger"])
    dispatcher = Dispatcher(logger)
    randomizer = Randomizer(logger, config["random"])

    if config["ip"] is not None:
        dispatcher.dispatch(config, config["ip"]) if not config["random"] else randomizer.randomize(config["ip"])
    elif config["ip_list"] is not None:
        with open(config["ip_list"], 'r') as fd:
            for ip in fd:
                dispatcher.dispatch(config, ip) if not config["random"] else randomizer.randomize(ip)

    print("")
