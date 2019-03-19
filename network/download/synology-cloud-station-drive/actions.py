#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools


NoStrip = ["/"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf synology-cloud-station-drive-4435.x86_64.deb")
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
