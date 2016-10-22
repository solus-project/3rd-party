#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools


NoStrip = ["/"]
IgnoreAutodep = True

def setup():
	shelltools.system("ar xf pCloud_Linux_amd64_%s.deb" % (get.srcVERSION()))
	shelltools.system("tar xf data.tar.gz")


def install():
    pisitools.insinto("/", "usr")
    pisitools.removeDir("/usr/lib")
    pisitools.removeDir("/usr/share/doc")
