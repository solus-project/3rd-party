#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Changes a lot i reckon
Suffix = ".g9b85d43.7-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf spotify-client_%s%s_amd64.deb" % (get.srcVERSION(), Suffix))
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
