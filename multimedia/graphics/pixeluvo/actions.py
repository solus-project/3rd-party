#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf pixeluvo_%s*_amd64.deb" % Version)
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    pisitools.remove("/usr/bin/pixeluvo")
    pisitools.dosym("/opt/pixeluvo/bin/Pixeluvo64", "/usr/bin/pixeluvo")
