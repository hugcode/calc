#!/usr/bin/python

import random, sys, getopt

def usage():
    print ("%s -m <max value>" % sys.argv[0])

max = 10
begin = 0
calc_list = []

try:
    opts, args = getopt.getopt(sys.argv[1:], "hsb:m:", ["help"])
except getopt.GetoptError:
    usage()
    sys.exit(2);

for opt,arg in opts:
    if opt == "-m":
        max = int(arg)
    if opt == "-b":
        begin = int(arg)
    if opt in ("-h", "--help"):
        usage()
        sys.exit(0)

i = begin
while (i <= max):
    j = begin
    while(j <= max):
        if ((i+j) <= max):
            str = "%2d+%2d=" % (i,j)
            calc_list.append(str)
        if (j<=i):
            str = "%2d-%2d=" % (i,j)
            calc_list.append(str)
        j = j+1
    i = i+1

i = 0
total = len(calc_list)
while (i < total/2):
    tmp_i = random.randint(0,total-1)
    tmp_j = random.randint(0,total-1)
    tmp_s = calc_list[tmp_i]
    calc_list[tmp_i] = calc_list[tmp_j]
    calc_list[tmp_j] = tmp_s
    i = i+1

i = 0
while (i < total):
    print ("%-10s" % calc_list[i]),
    i = i+1
    if (i % 5 == 0):
        print("")
    if (i % 20 == 0):
        print("")
