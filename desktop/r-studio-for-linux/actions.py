#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf RStudio4_x64.deb")
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
