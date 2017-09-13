#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf moneydance_linux_amd64.deb")
    shelltools.system("tar xf data.tar.bz2")
    shelltools.system("sed -i 's 512 32 ' opt/Moneydance/resources/moneydance.desktop")

def install():
    pisitools.insinto("/", "opt")
    pisitools.dosym("/opt/Moneydance/Moneydance", "/usr/bin/moneydance")
    pisitools.dosym("/opt/Moneydance/resources/moneydance.desktop", "/usr/share/applications/moneydance.desktop")
    pisitools.dosym("/opt/Moneydance/resources/moneydance_icon32.png", "/usr/share/pixmaps/moneydance_icon32.png")
