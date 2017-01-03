#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("tar xf mendeleydesktop-%s-linux-x86_64.tar.bz2" % Version)

def install():
    pisitools.insinto("/opt/mendeleydesktop/", "mendeleydesktop-%s-linux-x86_64/bin" % Version)
    pisitools.insinto("/opt/mendeleydesktop/", "mendeleydesktop-%s-linux-x86_64/lib" % Version)
    pisitools.insinto("/usr", "mendeleydesktop-%s-linux-x86_64/share" % Version)
    pisitools.removeDir("/usr/share/doc")
    pisitools.dosym("/opt/mendeleydesktop/bin/mendeleydesktop", "/usr/bin/mendeleydesktop")
