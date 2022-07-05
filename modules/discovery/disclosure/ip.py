from utils import parser, output


def print_ip(content):
    list_ip = parser.Parser(content).getip()
    if len(list_ip) > 1:
        output.Output().plus(f"Found Private IP: {str(list_ip).split('[')[1].split(']')[0]}")

    elif len(list_ip) == 1:
        output.Output().plus(f'Found Private IP: {list_ip[0]}')
