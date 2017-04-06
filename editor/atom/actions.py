#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf atom-amd64.deb")
    shelltools.system("tar xvf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.removeDir("/usr/share/lintian")
