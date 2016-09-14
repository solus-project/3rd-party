#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf google-webdesigner_current_amd64.deb")
    shelltools.system("tar xf data.tar.*")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
