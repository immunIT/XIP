from random import randint

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Randomizer():

    def __init__(self, logger, loop):
        self.mutations = [self._hex, self._octal]
        self.loop = loop
        self.logger = logger

    def randomize(self, ip):
        """Randomizer entrypoint.

        Parameters
        ----------
        ip : string
            IP address
        """

        for x in range(0, self.loop):
            self._generate(ip)

    def _generate(self, ip):
        """Generates random IP address.

        Parameters
        ----------
        ip : string
            IP address
        """

        tokens = ip.split('.')
        addr = ""
        i = 0

        for token in tokens:
            index = randint(0, 3)
            dotless = False if randint(0, 100) % 2 == 0 else True

            try:
                token = self.mutations[index](token)
            except:
                pass

            addr += str(token) + "." if not dotless and i < len(tokens) - 1 else str(token)

            i += 1

        self.logger.handle(addr, None)

    def _octal(self, token):
        """Converts to octal.

        Parameters
        ----------
        token : string
            IP address digit

        Return
        ------
        The mutated digit
        """

        tmp = str(oct(int(token))).replace("o", "")

        return "0" * randint(0, 5) + tmp if randint(0, 100) % 2 == 0 else tmp

    def _hex(self, token):
        """Converts to hexadecimal.

        Parameters
        ----------
        token : string
            IP address digit

        Return
        ------
        The mutated digit
        """

        return str(hex(int(token)))
