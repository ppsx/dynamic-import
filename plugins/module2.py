'''
Dynamic import example - module2

Usage:
    main module2 [<args>...]
    main module2 -h|--help

Options:
    -h, --help                 This screen
    -u, --user <username>      Username
    -p, --password <password>  Password

Arguments:
    <args>                     Additional arguments
'''

from common.print_data import just_print
from . import module1


def show(args):
    just_print('Module 2: Awaiting orders!')
    just_print('Got args: '+ str(args))
    just_print('Calling module1...')
    module1.run(args)


def run(args):
    return show(args)
