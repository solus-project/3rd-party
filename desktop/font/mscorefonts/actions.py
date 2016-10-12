#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True


def setup():
    shelltools.system("cabextract --lowercase *.exe --directory=ttfs")


def install():
    pisitools.insinto("/usr/share/fonts/truetype/mscorefonts", "ttfs/*.ttf")
