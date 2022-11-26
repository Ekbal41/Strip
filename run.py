from parse import parse

import sys, variables

variables.init()
filename = None
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("You must provide a filename")
    sys.exit()

with open(filename, 'r') as f:
    parse(f.read())
