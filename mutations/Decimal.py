import math

from mutations.AMutation import AMutation

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Decimal(AMutation):
    """This class applies decimal modification.
    """

    def __init__(self, config, logger, ip):
        super().__init__(config["dotless"], config["zeroless"], ip)

        self.overflow = config["overflow"]
        self.logger = logger

    def run(self):
        addr = self.ip

        if self.dotless:
            tokens = addr.split('.')
            tmp = 0
            i = len(tokens) - 1

            for token in tokens:
                tmp += int(round(int(token) * math.pow(256, i))) if i > 0 else int(token)
                i -= 1

            addr = tmp

        if self.overflow:
            addr = self._addOverflow(addr)

        if self.zeroless and not self.dotless:
            addr = self._trimZeros(addr)

        self.logger.handle(addr, None)

    def _addOverflow(self, addr):
        """Applies overflow.

        Parameters
        ----------
        addr : string
            IP address

        Return
        ------
        The mutated string
        """

        if not self.dotless:
            tokens = addr.split('.')
            tmp = ""
            i = 0

            for token in tokens:
                tmp += str(int(token) + 256) + "." if i < len(tokens) - 1 else str(int(token) + 256)
                i += 1

            return tmp
        else:
            return str(round(int(addr) + math.pow(256, 4)))
