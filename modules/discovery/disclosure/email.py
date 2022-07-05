from utils import parser, output


def print_emails(content):
    list_email = parser.Parser(content).getmail()
    if len(list_email) > 1:
        output.Output().plus(f"Found Emails: {str(list_email).split('[')[1].split(']')[0]}")

    elif len(list_email) == 1:
        output.Output().plus(f'Found Email: {list_email[0]}')
