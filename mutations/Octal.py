from random import randint

from mutations.AMutation import AMutation

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Octal(AMutation):
    """This class applies octal modification.
    """

    def __init__(self, config, logger, ip):
        super().__init__(config["dotless"], config["zeroless"], ip)

        self.padding = config["padding"]
        self.logger = logger

    def run(self):
        addr = self._convert(oct)

        if self.padding:
            tokens = addr.split('.')
            tmp = ""
            i = 0

            for token in tokens:
                tmp += self._addPadding(token) + "." if not self.dotless and i < len(tokens) - 1 else self._addPadding(token)
                i += 1
            addr = tmp

        if self.dotless:
            self.logger.handle("0" + addr.replace("0o", ""), None)
        else:
            if self.zeroless:
                addr = self._trimZeros(addr)
            self.logger.handle(addr.replace("o", ""), None)

    def _addPadding(self, token):
        """Applies padding.

        Parameters
        ----------
        token : string
            IP address digit.

        Return
        ------
        The padded token
        """

        return "0" * randint(1, 5) + token
