from abc import ABC, abstractmethod

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class AMutation(ABC):
    """Mutation abstract class.
    """

    def __init__(self, dotless, zeroless, ip):
        self.ip = ip
        self.dotless = dotless
        self.zeroless = zeroless

    @abstractmethod
    def run(self):
        """Mutation entrypoint.
        """

        pass

    def _convert(self, func):
        """Converts IP address bytes.

        Parameters
        ----------
        func : object
            Function to apply

        Return
        ------
        The mutated string
        """

        tokens = self.ip.split(".")
        addr = ""
        i = 0

        for token in tokens:
            addr += func(int(token)) + "." if not self.dotless and i < len(tokens) - 1 else func(int(token))
            i += 1

        return addr

    def _trimZeros(self, addr):
        """Delete digits equals to zero.

        Parameters
        ----------
        addr : string
            IP address

        Return
        ------
        The mutated string
        """

        tokens = addr.split('.')
        tmp = ""
        i = 0

        for token in tokens:
            val = int(token, 0)
            if val != 0:
                tmp += token + "." if i < len(tokens) - 1 else token
            i += 1

        return tmp
