from random import randint

from mutations.AMutation import AMutation

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Hex(AMutation):
    """This class applies hexadecimal modification.
    """

    def __init__(self, config, logger, ip):
        super().__init__(config["dotless"], config["zeroless"], ip)

        self.overflow = config["overflow"]
        self.logger = logger

    def run(self):
        addr = self._convert(hex)

        if self.overflow:
            addr = self._addOverflow(addr)

        if self.dotless:
            addr = "0x" + addr.replace("0x", "")

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
                token = "0x" + "41" * randint(0, 5) + token.replace("0x", "")
                tmp += token + "." if i < len(tokens) - 1 else token
                i += 1

            return tmp
        else:
            return "0x" + "41" * randint(0, 5) +  addr.replace("0x", "")
