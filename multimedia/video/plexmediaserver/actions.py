#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/"]
KeepSpecial = ["python"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf plexmediaserver_%s-*_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xvf data.tar.*")
    shelltools.system("sed -i 's/x-www-browser/xdg-open/' usr/share/applications/plexmediaserver.desktop")

def install():
    pisitools.insinto("/opt", "usr/lib/plexmediaserver")
    pisitools.insinto("/usr", "usr/share")
    pisitools.insinto("/usr/lib", "lib/udev")
