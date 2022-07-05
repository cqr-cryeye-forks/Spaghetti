import os
import sys

from utils.arguments import cli_arguments
from utils.colors import FakeColors, Colors


class Banner:
    def __init__(self, use_colors: bool = True):
        used_colors = FakeColors()
        if cli_arguments.no_color:
            used_colors = FakeColors()
        if use_colors:
            used_colors = Colors()
        self.RED = used_colors.red(1)
        self.YELLOW = used_colors.yellow(9)
        self.DARK_YELLOW = used_colors.yellow(0)
        self.WHITE = used_colors.white(0)
        self.END = used_colors.end()

    def banner(self):
        print(f"{self.DARK_YELLOW}  _____             _       _   _   _ {self.END}\n"
              f"{self.DARK_YELLOW} |   __|___ ___ ___| |_ ___| |_| |_|_|{self.END}\n"
              f"{self.DARK_YELLOW} |__   | . | .'| . |   | -_|  _|  _| |{self.END}\n"
              f"{self.DARK_YELLOW} |_____|  _|__,|_  |_|_|___|_| |_| |_|{self.END}\n"
              f"{self.DARK_YELLOW}       |_|     |___|          {self.RED}v0.1.4\n{self.END}\n"
              f"{self.WHITE}~/#{self.END} Spaghetti - Web Application Security Scanner{self.END}\n"
              f"{self.WHITE}~/#{self.END} Codename - {self.YELLOW}MR.R0B0T{self.END}\n"
              f"{self.WHITE}~/#{self.END} Momo Outaadi (@M4ll0k){self.END}\n"
              f"{self.WHITE}~/#{self.END} https://github.com/cqr-cryeye-forks/Spaghetti\n{self.END}\n")

    def usage(self, is_exit: bool = False):
        name = os.path.basename(sys.argv[0])
        self.banner()
        print("Usage:\n"
              "\t-u --url\tTarget URL (eg: http://example.com)\n"
              "\t-s --scan\tScan Options (default=0):\n\n"
              "\t\t0:\tFull Scan\n"
              "\t\t1:\tBruteforce (dirs,files,..)\n"
              "\t\t2:\tDisclosure (ip,emails,..)\n"
              "\t\t3:\tAttacks (sql,lfi,..)\n"
              "\t\t4:\tOthers (webdav,..)\n"
              "\t\t5:\tVulnerabilities (shellshock,..)\n"
              "\t\t6:\tFingerprint only\n\n"
              "\t--crawler\tDeep crawling (slow)\n"
              "\t--agent\t\tUse the specified user-agent\n"
              # "\t--random-agent\tUse a random user-agent\n"
              "\t--redirect\tRedirect target URL, default=True\n"
              "\t--timeout\tSet timeout, default=None\n"
              "\t--cookie\tSet cookie, default=None\n"
              "\t--proxy\t\tSet proxy, (host:port)\n"
              "\t--verbose\tVerbose output\n"
              "\t--version\tShow version\n""\t--help\t\tShow this help and exit\n\n"
              "Examples:\n\n"
              f"\t{name} --url http://example.com\n"
              f"\t{name} --url http://example.com --scan [0-6]\n"
              f"\t{name} --url http://example.com --scan 1 --crawler\n\n")
        if is_exit:
            sys.exit(0)

    def version(self, is_exit: bool = False):
        self.banner()
        print("~/# Spaghetti - Web Application Security Scanner (v0.1.3\n")
        if is_exit:
            sys.exit(0)
