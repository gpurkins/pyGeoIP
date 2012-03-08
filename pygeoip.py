#!/usr/bin/env python
# pygeoip.py - simple geoIP in python

# George Purkins - 2012
# loadgeoip() -> loads compacted ipdb from file
# 
# iplookup(ip) -> takes an IP address as a string 'w.x.y.z', returns two letter country code.
# http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

import os
from bisect import bisect_right

tup = [] # tuples go here
numberlist = [] # indices go here

def loadgeoip():
  if not os.path.isfile('ipdb.txt'):
    return
  with open('ipdb.txt') as countryFile: 
    for (num, line) in enumerate(countryFile, 0): 
      tup.append(line.split(";"))
      numberlist.append(int(tup[num][0]))

def iphash(ip):
  iphash = ip.split(".")
  iphash = ((int(iphash[0])*256+int(iphash[1]))*256+int(iphash[2]))*256+int(iphash[3])
  return(iphash)


def iplookup(ip):
  return hashToState(iphash(ip)).rstrip()

def hashToState(iphash):
  # Search list with bisect()
  nmin = 0
  nmax = len(numberlist)-1
  index = bisect_right(numberlist,iphash,nmin,nmax)
  return tup[index-1][1]

# Example use:
loadgeoip()
ip = '68.45.10.100'
print iplookup(ip)
