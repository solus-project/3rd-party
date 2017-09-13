#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf gitkraken-amd64.deb")
    shelltools.system("tar xJvf data.tar.xz")
    shelltools.system("sed -i 's Icon=app Icon=gitkraken ' usr/share/applications/gitkraken.desktop")
    shelltools.system("mv usr/share/pixmaps/app.png usr/share/pixmaps/gitkraken.png")
def install():
    pisitools.insinto("/", "usr")
