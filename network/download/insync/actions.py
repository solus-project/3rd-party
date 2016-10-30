#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import pisitools, shelltools

NoStrip = ["/etc", "/usr"]


def setup():
    shelltools.system("ar xf insync_1.3.12.36116-trusty_amd64.deb")
    shelltools.system("tar xvf data.tar.gz")
    shelltools.system("rmdir usr/share/icons/hicolor/64x64/emblems")

def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
        
