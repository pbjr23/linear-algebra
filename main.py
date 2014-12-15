import sys
from subprocess import Popen

def print_helptext():
    print """Python Linear Algebra toolkit.

    Usage:
      python main.py cli    Open command line interface
      python main.py app    Open web interface

    Options:
      -h --help    Show this screen
      --version    Show version
    """

try:
    if "-h" in sys.argv or "--help" in sys.argv:
        print_helptext()
    elif sys.argv[1] == "--version":
        print "Python Linear Algebra Toolkit 1.0.0"
    elif sys.argv[1] == "cli":
        Popen("python -i cli.py", shell=True)
    elif sys.argv[1] == "app":
        from app import app
        app.run()
    else:
        print "Unknown command: " + sys.argv[1]
        print_helptext()
except:
    print_helptext()

