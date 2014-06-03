#!/usr/bin/python
##################
# Sebastien CAPS #
# Guardis   2014 #
##################
# Usage:
#   cat data.json | python cmd-line-json-parser.py key subkey subkeyIndex subsubkey
#
# Example:
#   cat data.json | python cmd-line-json-parser.py DBInstances 0 Endpoint Address

import json,sys
keys    = sys.argv
data_in = sys.stdin

a=json.load(data_in)

for key in keys:
   if key != sys.argv[0]:
        if key.isdigit():
                key=int(key)
        a=a[key]
print a

# EOF
