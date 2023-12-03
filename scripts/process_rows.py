# This script is handy to parse input data.
# For example, params like so: -b=\' -a=\', -ba=\[ -aa=\]
# will wrap each row between ' ' and the wrap the whole file with [ ]
# Basically, this example will parse a file with many lines into a single string array.
#
# I suggest you to put your input and output files in scripts/tmp to keep them un-commitable

import argparse

parser = argparse.ArgumentParser(
  description='Manipulate a file adding given chars before and after each row'
)

parser.add_argument('filename', type=str)

# ---- Row manipulation
parser.add_argument('-a', '--after', default='', help='to be added after each row', type=str)
parser.add_argument('-b', '--before', default='', help='to be added before each row', type=str)
parser.add_argument('-ncr', '--no-carriage-return', action='store_false', dest='has_return', help='prevent carriage return after each row of the original files')

# ---- All file manipulation
parser.add_argument('-o', '--output', default='tmp/o.py', help='output destination', type=str)
parser.add_argument('-aa', '--after-all', default='', help='to be added after the whole file', type=str)
parser.add_argument('-ba', '--before-all', default='', help='to be added after the whole file', type=str)

# ----
args = parser.parse_args()
print('All params >>{}<<'.format(args)) # TODO: remove this
# ----

with open(args.filename, 'r') as file:
  with open(args.output, 'w') as o:
    if args.before_all: 
      o.write(args.before_all)
      o.write('\n')

    for line in file:
      o.write('{0}{1}{2}'.format(args.before, line.strip(), args.after))
      if args.has_return: o.write('\n')
    
    if args.after_all: o.write(args.after_all)