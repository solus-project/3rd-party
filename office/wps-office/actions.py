#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr", "/opt"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf wps-office_%s_amd64.deb" % Version)
    shelltools.system("tar xf data.tar.xz")
    #Don't install separate menu folder entry:
    shelltools.system("rm -r etc")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    #pisitools.insinto("/", "etc")
