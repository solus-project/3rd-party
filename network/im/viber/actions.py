#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf viber.deb")
    shelltools.system("tar xvf data.tar.xz")
def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
    
