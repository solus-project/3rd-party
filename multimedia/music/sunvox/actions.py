#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr", "/opt"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("unzip sunvox-%s" % (get.srcVERSION()))

def install():
    pisitools.insinto("/opt/sunvox/", "sunvox/sunvox/linux_x86_64/sunvox")
    pisitools.insinto("/opt/sunvox/", "sunvox/examples")
    pisitools.insinto("/opt/sunvox/", "sunvox/instruments")
    pisitools.dosym("/opt/sunvox/sunvox", "/usr/bin/sunvox")
