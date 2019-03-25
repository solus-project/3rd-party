#!/usr/bin/python

# Created for Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf franz_%s_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    pisitools.dosym("/opt/Franz/franz", "/usr/bin/franz")
    pisitools.dosym("/usr/share/icons/hicolor/1024x1024/apps/franz.png", "/usr/share/icons/hicolor/scalable/apps/franz.png")
