import sys
import optparse


def print_helptext():
    print """Python Linear Algebra toolkit.

    Usage:
      python main.py cli    Open command line interface
      python main.py app    Open web interface

    Options:
      -h --help     Show this screen
      -d --debug    Start webapp in debug mode
      --version     Show version
    """

parser = optparse.OptionParser(add_help_option=False)
parser.add_option('-h', '--help', action="store_true")
parser.add_option('--version', action="store_true")
parser.add_option('-d', '--debug', action="store_true")
options, args = parser.parse_args()

try:
    if options.version:
        print "Python Linear Algebra Toolkit 1.0.0"
    elif sys.argv[1] == "cli":
        import cli
    elif sys.argv[1] == "app":
        from app.app import app
        app.run(debug=options.debug)
    elif options.help:
        print_helptext()
    else:
        print "Unknown command: " + " ".join(sys.argv[1:])
        print_helptext()
except:
    print_helptext()
