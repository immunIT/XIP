import importlib

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Dispatcher():
    """This class instantiates and executes selected mutation passed as paramaters to XIP.
    """

    def __init__(self, logger):
        self.logger = logger
        self.mutations = {"hex", "octal", "decimal", "ipv6"}

    def dispatch(self, config, ip):
        """Instantiate and run selected mutation.

        Parameters
        ----------
        config : dict
            XIP parameters
        """

        for mutation in self.mutations:
            if config[mutation]:
                try:
                    self._factory(str.capitalize(mutation))(config, self.logger, ip).run()
                except:
                    pass

    def _factory(self, name):
        """Dynamicaly import mutations.

        Parameters
        ----------
        name : str
            Mutation name's

        Return
        ------
        Mutations instance's
        """

        return getattr(importlib.import_module("mutations." + name), name)
