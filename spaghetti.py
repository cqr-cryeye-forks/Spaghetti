#!/usr/bin/env python3.10
# -*- coding:utf-8 -*-
#
# @name:    Spaghetti - Web Application Security Scanner
# @repo:    https://github.com/cqr-cryeye-forks/Spaghetti
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt'

import sys
import time

from request import urlparser, ragent
from utils import manager
from utils.arguments import cli_arguments
from utils.banner import Banner
from utils.output import Output


class Spaghetti:

    def __init__(self):
        self.banner = Banner(cli_arguments.no_color)
        self.print_results = Output()
        self.parser = urlparser
        self.run_manager = manager

        self.agent = cli_arguments.agent or ragent.random_agent()
        self.url = self.target(cli_arguments.url)
        self.scan = cli_arguments.scan
        self.redirect = cli_arguments.redirect
        self.timeout = cli_arguments.timeout
        self.proxy = cli_arguments.proxy
        self.cookie = cli_arguments.cookies

    def main(self):
        if cli_arguments.version:
            self.banner.version(True)
        # if cli_arguments.help:
        #     self.banner.usage(True)

        # starting
        self.banner.banner()
        self.strftime()
        if self.scan == 0:
            self.print_results.info(f'Used default scan option: value {self.scan}')
        if self.scan != 6:
            self.run_manager.fingerprints(self.agent, self.proxy, self.redirect, self.timeout, self.url, self.cookie)
        # crawler
        urls = []
        if self.scan in [0, 3]:
            print("")
            urls = self.run_manager.crawling(*self.default_arguments)
        if not urls:
            urls.append(self.url)
        # scan options
        if self.scan == 0:
            self.run_manager.bruteforce(*self.default_arguments)
            self.run_manager.disc(*self.default_arguments)
            self.run_manager.attacks(
                self.agent, self.proxy, self.redirect, self.timeout, urls, self.cookie)
            self.run_manager.others(*self.default_arguments)
            self.run_manager.vuln(*self.default_arguments)
        elif self.scan == 1:
            self.run_manager.bruteforce(*self.default_arguments)
        elif self.scan == 2:
            self.run_manager.disc(*self.default_arguments)
        elif self.scan == 3:
            self.run_manager.attacks(*self.default_arguments)
        elif self.scan == 4:
            self.run_manager.others(*self.default_arguments)
        elif self.scan == 5:
            self.run_manager.vuln(*self.default_arguments)
        elif self.scan == 6:
            self.run_manager.fingerprints(*self.default_arguments)
            print("")
        else:
            self.print_results.info(f'Unknown scan option: {self.scan}!')

    def strftime(self):
        self.print_results.plus(f'URL: {self.url}')
        self.print_results.plus(f"Started: {str(time.strftime('%d/%m/%Y %H:%M:%S'))}")
        print("")

    def target(self, url):
        if url is None:
            self.banner.usage()
            sys.exit(self.print_results.less('Url not found, please try with target url!'))
        u = self.parser.UrlParser(url).host_path()
        if u is None:
            sys.exit(self.print_results.less('Url not found, please try with target url!'))
        return str(u)

    @property
    def default_arguments(self):
        return [self.agent, self.proxy, self.redirect, self.timeout, self.url, self.cookie]


if __name__ == "__main__":
    try:
        Spaghetti().main()
    except KeyboardInterrupt:
        sys.exit(Output().less('Keyboard Interrupt by User!!'))
