#!/usr/bin/env python2
import sys
try:
    while True:
        N_P_line = sys.stdin.readline().strip() #make string clean
        if not N_P_line:
            break
        else:
            NP = N_P_line.split()
            #print NP
            N = int(NP[0])
            P = int(NP[1])
            print(P)
            for _ in range(N): #_ is a throwaway variable 
            #Using a double underscore __ as your throwaway variable if better!
                #print ("read silly input")
                null = sys.stdin.readline()

except:
    pass
''' First good solution for reading input
try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        else:
            print int(line)
except:
    pass
'''

''' BAD Input: This is wrong!
try:
    lines = sys.stdin.readline().strip() # NO! This is only one line
    print lines # NO! This is only one line
    for line in lines: # NO!  "for char in line:"
        if not line:
            break
        else:
            print int(line)
except:
    pass
'''

''' Second solution for reading input: Not friendly
NOTE: If you are using Python Shell, Enter cannot trigger the output.
One have to use Ctrl+D to finish the input, and then you can see the outputs.
So this one is not friendly to Shell.

for line in sys.stdin:
    print int(line)
'''
