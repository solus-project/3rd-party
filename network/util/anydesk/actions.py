#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf anydesk_%s-1_amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
