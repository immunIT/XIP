from mutations.AMutation import AMutation

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Ipv6(AMutation):
    """This class applies decimal modification.
    """

    def __init__(self, config, logger, ip):
        super().__init__(config["dotless"], config["zeroless"], ip)

        self.overflow = config["overflow"]
        self.logger = logger

    def run(self):
        self.logger.handle("[::" + self.ip + "]", None)
        self.logger.handle("[::ffff:" + self.ip + "]", None)
