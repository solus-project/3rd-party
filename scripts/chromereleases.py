#!/usr/bin/env python

#  Copyright 2015 Ikey Doherty <ikey@evolve-os.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.


import xml.etree.ElementTree as etree
import re
import pisi.api
from distutils.version import LooseVersion
import urllib2

input = urllib2.urlopen("http://feeds.feedburner.com/GoogleChromeReleases?format=xml")

content = "\n".join(input.readlines())

root = etree.fromstring(content)

versions = list()

reg = '(\d+\.)(\d+\.)(\d+\.)(\d+)'
r = re.compile(reg)
for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
    cat = entry.findall("{http://www.w3.org/2005/Atom}category")
    if cat is None:
        continue
    if not "term" in cat[0].attrib:
        continue
    if cat[0].attrib["term"] != "Stable updates":
        continue
    content = entry.findall("{http://www.w3.org/2005/Atom}content")[0]
    for word in content.text.split(" "):
        if r.match(word):
            versions.append(word)

(meta,files) = pisi.api.info("google-chrome-stable", True)

for version in versions:
    if LooseVersion(version) > LooseVersion(meta.package.version):
        print "You must update google-chrome-stable (%s) to %s" % (meta.package.version, version)
        break


print "\nLatest Google Chrome versions:\n\n%s" % ("\n".join(versions))
