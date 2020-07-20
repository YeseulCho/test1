#! /usr/bin/env python

import sys

if len(sys.argv) != 2 :
    print("#usage: python {sys.argv[0]} [txt]")
    sys.exit()

num = int(sys.argv[1])
try :
    print(10 / num)
except ZeroDivisioError :
    print("0 X")
