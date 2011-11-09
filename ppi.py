#!/usr/bin/env python26
# -*- coding: utf-8 -*-
import sys, math

def usage():
	print "Usage: %s [width resolution in pixels] [height resolution in pixels] [diagnonal size in inch]" % (sys.argv[0])

def compare():
	print 
	print "examples:"
	print "lenovo x220:	1366x768 12.50 \" ->\t125.367427987 ppi"
	print "macbook air: 	1440x900 13.30 \" ->\t127.677940133 ppi"
	print "nexus s:   	 480x800  4.00 \" ->\t233.238075794 ppi"
	print "galaxy nexus:	1280x720  4.65 \" ->\t315.828984958 ppi"
	print "iphone 4s: 	 960x640  3.50 \" ->\t329.650402328 ppi"
	print "#########################################################"

if __name__ == '__main__':
	if (len(sys.argv) < 4):
		usage()
	else:
		(w, h, di) = (sys.argv[1], sys.argv[2], sys.argv[3])
		dp = math.sqrt((float(w) * float(w)) + (float(h) * float(h)))
		ppi = (dp/float(di))
		compare()
		print "your entry:	%s ->\t%s ppi" % (w+"x"+h+" "+di+" \"", ppi)
		print
