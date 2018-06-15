import argparse
import sys

__author__ = "Jean Lejeune <jlejeune@immunit.ch>"
__copyright__ = "Copyright 2018, ImmunIT"


class Parser():
    """This class parses the tool arguments
    """

    def init(self):
        self.config = {}

    def parse(self):
        """Parse XIP arguments.

        Return
        ------
        Configuration dictionnary
        """

        parser = argparse.ArgumentParser(description="""\
            XIP generates a list of IP addresses by applying a set of transformations used to bypass security measures e.g. blacklist filtering, WAF, etc.
        """)
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-i', type=str, help="IP address")
        group.add_argument('-iL', type=str, help="List of IP addresses")
        parser.add_argument("--hex", help="Hexadecimal mutation", action="store_true")
        parser.add_argument("--octal", help="Binary mutation", action="store_true")
        parser.add_argument("--decimal", help="Binary mutation", action="store_true")
        parser.add_argument("--dotless", help="Hexadecimal mutation", action="store_true")
        parser.add_argument("--zeroless", help="Delete digits equals to zero. Not compatible with dotless mode", action="store_true")
        parser.add_argument("--padding", help="Apply padding (octal). Not compatible with dotless mode", action="store_true")
        parser.add_argument("--overflow", help="Apply overflow (decimal|hexadecimal). Doesn't work on Linux", action="store_true")
        parser.add_argument("--ipv6", help="Apply IPv4 to IPv6 mutation", action="store_true")
        parser.add_argument("--random", help="Generate x IP addresses using random mutations", metavar='x', type=int)
        parser.add_argument("--log", help="Enable logging", action="store_true")

        if len(sys.argv) == 1:
            parser.print_help(sys.stderr)
            sys.exit(1)

        args = parser.parse_args()

        set_random_by_default = True
        for arg, val in vars(args).items():
            if arg not in ('i','iL') and val:
                set_random_by_default = False

        if set_random_by_default:
            args.random = 20

        self._loadConfig(args)

        return self.config

    def _loadConfig(self, args):
        """Load configuration from parsed arguments.

        Parameters
        ----------
        args : object
            XIP parsed arguments

        Return
        ------
        Configuration dictionnary
        """

        self.config = {
            "ip": args.i,
            "ip_list": args.iL,
            "dotless": args.dotless,
            "zeroless": args.zeroless,
            "padding": args.padding,
            "overflow": args.overflow,
            "random": args.random,
            "ipv6": args.ipv6,
            "hex": args.hex,
            "octal": args.octal,
            "decimal": args.decimal,
            "logger": args.log
        }
