#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools


NoStrip = ["/"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf synology-cloud-station-drive-%s.x86_64.deb" % (get.srcVERSION()))
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
