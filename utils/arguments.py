import argparse


def create_parser():
    # try:
    #     opts, arg = getopt.getopt(
    #         argv, 'u:s:', ['url=', 'scan=', 'crawler', 'agent=', 'random-agent', 'redirect=',
    #                        'timeout=', 'cookie=', 'proxy=', 'verbose', 'version', 'help']
    #     )
    # except getopt.error as e:
    #     self.banner.usage(True)

    #     if o in ('--redirect'):
    #         redir = a
    #     if o in ('--timeout'):
    #         time = a
    #     if o in ('--cookie'):
    #         cookie = a
    #     if o in ('--proxy'):
    #         proxy = a
    #     if o in ('--help'):
    #         self.banner.usage(True)
    parser = argparse.ArgumentParser(description='Spaghetti - Web Application Security Scanner')
    parser.add_argument('-u', '--url', type=str,
                        help='Target URL (eg: http://example.com)')
    parser.add_argument('-s', '--scan', type=int, default=0,
                        help="Scan Options (default=0):\n\n"
                             "\t\t0:\tFull Scan\n"
                             "\t\t1:\tBruteforce (dirs,files,..)\n"
                             "\t\t2:\tDisclosure (ip,emails,..)\n"
                             "\t\t3:\tAttacks (sql,lfi,..)\n"
                             "\t\t4:\tOthers (webdav,..)\n"
                             "\t\t5:\tVulnerabilities (shellshock,..)\n"
                             "\t\t6:\tFingerprint only\n\n")
    parser.add_argument('-a', '--agent', type=str, default=None,
                        help='Use the specified user-agent. Else will be used random agent')
    parser.add_argument('-t', '--timeout', type=int, default=None,
                        help='Set timeout, default=None')
    parser.add_argument('-ck', '--cookies', type=str, default=None,
                        help='Set cookie, default=None')
    parser.add_argument('-p', '--proxy', type=str, default=None,
                        help='Set proxy, (host:port)')
    parser.add_argument('-c', '--crawler', default=False, action='store_true',
                        help='Deep crawling (slow)')
    parser.add_argument('-r', '--redirect', default=True, action='store_true',
                        help='Redirect target URL, default=True')
    parser.add_argument('-v', '--verbose', default=False, action='store_true',
                        help='Verbose output')
    parser.add_argument('-tv', '--version', default=False, action='store_true',
                        help="Show tool version")
    parser.add_argument('-n', '--no-color', default=False, action='store_true',
                        help="Print results without color")
    return parser.parse_args()


cli_arguments = create_parser()
