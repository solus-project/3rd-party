#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf enpass_%s_amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.gz")
def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
    pisitools.removeDir("/usr/share/doc")
