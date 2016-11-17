#!/usr/bin/python

import random, sys, getopt, time

def usage():
    print ("%s -m <max value>" % sys.argv[0])

max     = 10
begin   = 0
flag_e  = 0
flag_i  = 0
calc_list = []
stat_list = {}

try:
    opts, args = getopt.getopt(sys.argv[1:], "heib:m:", ["help", "interactive"])
except getopt.GetoptError:
    usage()
    sys.exit(2);

for opt,arg in opts:
    if opt == "-m":
        max = int(arg)
    if opt == "-b":
        begin = int(arg)
    if opt == "-e":
        flag_e = 1
    if opt in ("-i", "--interactive"):
        flag_i = 1
    if opt in ("-h", "--help"):
        usage()
        sys.exit(0)

def create_table():
    i = begin
    while (i <= max):
        j = begin
        if (flag_e == 1):
            max_j = i
        else:
            max_j = max
        while(j <= max_j):
            if ((i+j) <= max):
                calc_list.append((i,'+',j))
            if (j<=i):
                calc_list.append((i,'-',j))
            j = j+1
        i = i+1

def random_table():
    i = 0
    total = len(calc_list)
    while (i < total):
        tmp_i = random.randint(0,total-1)
        tmp_j = random.randint(0,total-1)
        tmp_s = calc_list[tmp_i]
        calc_list[tmp_i] = calc_list[tmp_j]
        calc_list[tmp_j] = tmp_s
        i = i+1

def show_table():
    i = 0
    total = len(calc_list)
    while (i < total):
        elm = calc_list[i]
        str = "%d%s%d=" % (elm[0],elm[1],elm[2])
        print ("%10s" % str),
        i = i+1
        if (i % 5 == 0):
            print("")
        if (i % 20 == 0):
            print("")

def calc_table():
    i = 0
    total = len(calc_list)
    while (i < total):
        elm = calc_list[i]
        i = i+1

        str = "%d%s%d=" % (elm[0],elm[1],elm[2])
        if (elm[1] == '+'):
            res = elm[0] + elm[2]
        elif (elm[1] == '-'):
            res = elm[0] - elm[2]
        else:
            sys.exit(2)

        print ("%10s" % str),
        time_b = time.time()
        ans = raw_input("")
        time_e = time.time()
        time_s = time_e - time_b

        ans = unicode(ans, 'utf-8')
        if (ans == 'q'):
            return
        elif (ans.isnumeric() and int(ans) == res):
            print ("correct! spend %ds" % time_s)
        else:
            time_s = 10000
            print ("wrong, correct result is %d" % res)
        stat_list[str] = time_s

def show_slow():
    slow_list = sorted(stat_list.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    for k,v in slow_list:
        print ("%s spend %ds" % (k, v))

def main():
    create_table()
    random_table()
    if (flag_i == 0):
        show_table()
    else:
        calc_table()
        show_slow()

main()
