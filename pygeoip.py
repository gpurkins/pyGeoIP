#!/usr/bin/env python
"""
pygeoip.py - simple geoIP in python

George Purkins - 2012
"""
# pygeoip.py - simple geoIP in python

# George Purkins - 2012
# loadgeoip() -> loads compacted ipdb from file
# 
# iplookup(ip) -> takes an IP address as a string 'w.x.y.z', returns two letter country code.
# http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

import os
from bisect import bisect_right

#where is the ipdb.txt file located?  The following assumes the same place as this script.
ipdb_file="ipdb.txt"

tup = [] # tuples go here
numberlist = [] # indices go here

def loadgeoip():
  """
  Loads compacted ipdb from file.  ipdb contains a list of hashed IP ranges associated with country codes.
  """
  if not os.path.isfile(ipdb_file):
    return
  with open(ipdb_file) as countryFile: 
    for (num, line) in enumerate(countryFile, 0): 
      tup.append(line.split(";"))
      numberlist.append(int(tup[num][0]))

def iphash(ip):
  """
  Takes an IP address (ip) and hashes it.
  """
  iphash = ip.split(".")
  iphash = ((int(iphash[0])*256+int(iphash[1]))*256+int(iphash[2]))*256+int(iphash[3])
  return(iphash)


def iplookup(ip):
  """
  Takes an IP address as a string 'w.x.y.z', returns two letter country code.

  http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
  """
  return hashToState(iphash(ip)).rstrip()

def hashToState(iphash):
  """
  Search list with bisect().  This is essentially a binary search on the ipdb after the requested ip to look up has been hashed.

  This function is solely used by iplookup(ip)
  """
  # Search list with bisect()
  nmin = 0
  nmax = len(numberlist)-1
  index = bisect_right(numberlist,iphash,nmin,nmax)
  return tup[index-1][1]

if __name__ == '__main__':
  import sys,inspect

  # Example use:
  from CountryCodes import CountryCodes
  loadgeoip()
  ip = '68.45.10.100'
  print "%s is located in %s" % (ip,CountryCodes(iplookup(ip)).country)
