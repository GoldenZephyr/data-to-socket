#!/usr/bin/env python

import time
import sys

if __name__ == ("__main__"):
    time.sleep(1)
    for i in xrange(20):
        #sys.stdout.write(str(i))
        #sys.stdout.write('\n')
        #sys.stdout.flush()
        print(i)
        sys.stdout.flush()
        time.sleep(1)

