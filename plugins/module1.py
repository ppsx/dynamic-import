'''
Dynamic import example - module1

Usage:
    main [options] module1 [<args>...]
    main module1 -h|--help

Options:
    -h, --help                 This screen
    -u, --user <username>      Username
    -p, --password <password>  Password

Arguments:
    <args>                     Additional arguments
'''


from common.print_data import just_print


def whoami(args):
    just_print('I am module 1')
    just_print('Got args:' + str(args))


def run(args):
    return whoami(args)
