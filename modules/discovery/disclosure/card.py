from utils import parser, output


def print_credit_cards(content):
    cc = parser.Parser(content).get_cards()
    if len(cc) > 1:
        output.Output().plus(f"Found Credit Cards: {str(cc).split('[')[1].split(']')[0]}")

    elif len(cc) == 1:
        output.Output().plus(f'Found Credit Card: {cc[0]}')
