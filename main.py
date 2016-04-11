'''
Dynamic import example.

Usage:
    main [options] <command> [<args>...]
    main -h|--help

Options:
    -h, --help                 This screen
    -u, --user <username>      Username
    -p, --password <password>  Password

See 'main <command> --help' for more information on a specific command.

'''


import os
import sys
import imp
from os import path
from docopt import docopt


PLUGINS_DIR = 'plugins'


def get_plugin_list():
    ml = [path.basename(f).split('.')[0] for f in os.listdir(PLUGINS_DIR)
          if not f.startswith('_') and f.endswith('.py')]
    return ml


if __name__ == '__main__':

    # args = docopt(__doc__, options_first=True)
    args = docopt(__doc__)
    print 'Global arguments:'
    print args

    mod = args['<command>']
    argv = [mod] + args['<args>']
    # argv = [mod] + sys.argv[1:]
    print argv

    if mod in get_plugin_list():
        pkg = imp.load_module(PLUGINS_DIR, *imp.find_module(PLUGINS_DIR))
        m = imp.load_module(PLUGINS_DIR + '.' + mod, *imp.find_module(mod, pkg.__path__))
        # a = docopt(m.__doc__, argv=argv)
        # print 'Command arguments:'
        # print a
        # print 'All arguments:'
        # args.update(a)
        # print args
        print '----'
        # m.run((args, a))
        m.run(args)
        print '----'
    else:
        print 'No such command:', mod
        print 'See \'main --help\''
        sys.exit(1)
